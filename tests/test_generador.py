import json
import pathlib
import tempfile
import unittest
from unittest import mock

from poc import pipeline, prompts
from poc.generador import generar
from tests.datos_de_prueba import (
    FORMULARIO,
    PLAN_VALIDO,
    ClienteFalso,
    con_contenido,
    copia,
    error_de_api,
    ingesta_con,
)

CON_MATERIAL = ingesta_con(general=[("temario.txt", "Capa de enlace. Enrutamiento.")])
SIN_MATERIAL = ingesta_con()


def js(x):
    return json.dumps(x, ensure_ascii=False)


def plan_con_prioridad_invertida():
    p = copia(PLAN_VALIDO)
    p["plan"][0]["bloques"] = [
        {"tema": "Capa de enlace", "minutos": 100},
        {"tema": "Enrutamiento", "minutos": 20},
    ]
    return p


class TestGenerar(unittest.TestCase):
    def test_valido_al_primer_intento_hace_una_llamada(self):
        c = ClienteFalso([js(PLAN_VALIDO)])
        r = generar(c, "m", FORMULARIO, CON_MATERIAL)
        self.assertTrue(r["valido"])
        self.assertEqual(r["intentos"], 1)
        self.assertEqual(len(c.llamadas), 1)
        self.assertEqual(r["tokens"], 100)
        self.assertIsNone(r["error_api"])

    def test_pide_json_mode_y_usa_el_modelo_indicado(self):
        c = ClienteFalso([js(PLAN_VALIDO)])
        generar(c, "modelo-x", FORMULARIO, CON_MATERIAL)
        self.assertEqual(c.llamadas[0]["model"], "modelo-x")
        self.assertEqual(c.llamadas[0]["response_format"], {"type": "json_object"})

    def test_reintenta_una_vez_con_los_errores_concretos(self):
        mal = copia(PLAN_VALIDO)
        mal["plan"][1]["bloques"][0]["minutos"] = 90
        c = ClienteFalso([js(mal), js(PLAN_VALIDO)])
        r = generar(c, "m", FORMULARIO, CON_MATERIAL)
        self.assertTrue(r["valido"])
        self.assertEqual(r["intentos"], 2)
        self.assertEqual(r["tokens"], 200)
        ultimo = c.llamadas[1]["messages"][-1]["content"]
        self.assertIn("90 min planificados, 60 disponibles", ultimo)

    def test_no_reintenta_mas_de_una_vez_y_no_oculta_el_plan(self):
        mal = copia(PLAN_VALIDO)
        mal["plan"][1]["bloques"][0]["minutos"] = 90
        c = ClienteFalso([js(mal), js(mal), js(PLAN_VALIDO)])
        r = generar(c, "m", FORMULARIO, CON_MATERIAL)
        self.assertFalse(r["valido"])
        self.assertEqual(r["intentos"], 2)
        self.assertEqual(len(c.llamadas), 2)
        self.assertIsNotNone(r["respuesta"])
        self.assertTrue(r["errores"])

    def test_respuesta_que_no_es_json_se_reintenta(self):
        c = ClienteFalso(["esto no es json", js(PLAN_VALIDO)])
        r = generar(c, "m", FORMULARIO, CON_MATERIAL)
        self.assertTrue(r["valido"])
        self.assertEqual(r["intentos"], 2)
        self.assertIn("JSON inválido", c.llamadas[1]["messages"][-1]["content"])

    def test_prioridad_incoherente_dispara_el_reintento(self):
        c = ClienteFalso([js(plan_con_prioridad_invertida()), js(PLAN_VALIDO)])
        r = generar(c, "m", FORMULARIO, CON_MATERIAL)
        self.assertEqual(r["intentos"], 2)
        self.assertEqual(r["errores_prioridad"], [])

    def test_prioridad_que_no_se_corrige_queda_informada(self):
        mal = js(plan_con_prioridad_invertida())
        r = generar(ClienteFalso([mal, mal]), "m", FORMULARIO, CON_MATERIAL)
        self.assertTrue(r["errores_prioridad"])
        self.assertTrue(r["valido"])  # la estructura está bien; la prioridad se informa aparte

    def test_error_de_la_api_no_levanta_y_se_informa(self):
        r = generar(ClienteFalso([error_de_api("sin crédito")]), "m", FORMULARIO, CON_MATERIAL)
        self.assertFalse(r["valido"])
        self.assertIn("sin crédito", r["error_api"])
        self.assertIsNone(r["respuesta"])
        self.assertEqual(r["intentos"], 1)

    def test_error_de_la_api_en_el_reintento_conserva_el_primer_plan(self):
        mal = copia(PLAN_VALIDO)
        mal["plan"][1]["bloques"][0]["minutos"] = 90
        r = generar(ClienteFalso([js(mal), error_de_api("timeout")]), "m", FORMULARIO, CON_MATERIAL)
        self.assertFalse(r["valido"])
        self.assertIn("timeout", r["error_api"])
        self.assertIsNotNone(r["respuesta"])
        self.assertTrue(r["errores"])


class TestContenidoSinArchivos(unittest.TestCase):
    """Los tres tipos de contenido se generan y se exigen aunque no se suba ningún archivo."""

    def test_sin_archivos_igual_se_piden_y_se_validan_los_tipos_elegidos(self):
        f, p = con_contenido("preguntas", "ejercicios", "parcial")
        c = ClienteFalso([js(p)])
        r = generar(c, "m", f, SIN_MATERIAL)
        self.assertTrue(r["valido"])
        sistema = c.llamadas[0]["messages"][0]["content"]
        for tipo in ("preguntas", "ejercicios", "parcial"):
            self.assertIn(f'"{tipo}"', sistema)
        self.assertIn("No subí material", c.llamadas[0]["messages"][1]["content"])
        self.assertIn("conocimiento general", sistema)

    def test_sin_archivos_falta_un_tipo_pedido_y_se_reintenta(self):
        f, p = con_contenido("ejercicios")
        incompleto = copia(p)
        del incompleto["ejercicios"]
        c = ClienteFalso([js(incompleto), js(p)])
        r = generar(c, "m", f, SIN_MATERIAL)
        self.assertEqual(r["intentos"], 2)
        self.assertTrue(r["valido"])

    def test_sin_contenido_pedido_el_prompt_no_menciona_ningun_tipo(self):
        f, p = con_contenido()
        c = ClienteFalso([js(p)])
        generar(c, "m", f, SIN_MATERIAL)
        sistema = c.llamadas[0]["messages"][0]["content"]
        for tipo in ("preguntas", "ejercicios", "parcial"):
            self.assertNotIn(f'"{tipo}"', sistema)
        self.assertNotIn("6.", sistema)

    def test_solo_se_pide_lo_elegido(self):
        f, p = con_contenido("parcial")
        sistema = prompts.reglas(["parcial"])
        self.assertIn('"parcial"', sistema)
        self.assertNotIn('"ejercicios"', sistema)
        self.assertNotIn('"preguntas"', sistema)


class TestMaterialEnElPrompt(unittest.TestCase):
    def test_el_material_va_entero_y_separado_en_general_y_por_tema(self):
        ing = ingesta_con(
            general=[("temario.txt", "TEXTO DEL TEMARIO")],
            por_tema={"Enrutamiento": [("rutas.txt", "TEXTO DE RUTAS")]},
        )
        usuario = prompts.mensajes(FORMULARIO, ing)[1]["content"]
        self.assertIn("Material general de la materia", usuario)
        self.assertIn("TEXTO DEL TEMARIO", usuario)
        self.assertIn("Material del tema «Enrutamiento»", usuario)
        self.assertIn("TEXTO DE RUTAS", usuario)

    def test_sin_general_no_aparece_el_encabezado_general(self):
        ing = ingesta_con(por_tema={"Enrutamiento": [("rutas.txt", "x")]})
        usuario = prompts.mensajes(FORMULARIO, ing)[1]["content"]
        self.assertNotIn("Material general", usuario)

    def test_el_prompt_dice_que_hacer_con_un_tema_sin_material(self):
        sistema = prompts.mensajes(con_contenido("preguntas")[0], CON_MATERIAL)[0]["content"]
        self.assertIn("Si un tema no tiene", sistema)


class TestPipeline(unittest.TestCase):
    def setUp(self):
        # Ningún test de esta clase escribe en el registro/ real.
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        parche = mock.patch("poc.registro.REGISTRO", pathlib.Path(self.tmp.name))
        parche.start()
        self.addCleanup(parche.stop)

    def test_formulario_invalido_no_llama_al_modelo(self):
        f = copia(FORMULARIO)
        f["temas"] = {}
        c = ClienteFalso([])
        p = pipeline.procesar(c, f)
        self.assertTrue(p.errores_formulario)
        self.assertIsNone(p.resultado)
        self.assertEqual(c.llamadas, [])

    def test_camino_completo_y_registro(self):
        c = ClienteFalso([js(PLAN_VALIDO)])
        p = pipeline.procesar(
            c,
            copia(FORMULARIO),
            general=[("temario.txt", b"Capa de enlace"), ("x.png", b"x")],
            por_tema={"Enrutamiento": [("rutas.txt", b"rutas")]},
            modelo="m",
        )
        self.assertTrue(p.resultado["valido"])
        self.assertEqual(len(p.ingesta.rechazados), 1)
        guardado = json.loads(pathlib.Path(p.ruta_registro).read_text(encoding="utf-8"))
        self.assertEqual(guardado["modelo"], "m")
        usados = {u["nombre"]: u for u in guardado["archivos"]["usados"]}
        self.assertIsNone(usados["temario.txt"]["tema"])
        self.assertEqual(usados["rutas.txt"]["tema"], "Enrutamiento")
        # No se guarda el texto de los archivos, sólo nombre, tema y tamaño.
        self.assertEqual(set(usados["rutas.txt"]), {"nombre", "tema", "caracteres"})
        self.assertTrue(p.ruta_registro.startswith(self.tmp.name))

    def test_si_no_se_puede_registrar_el_plan_se_devuelve_igual(self):
        c = ClienteFalso([js(PLAN_VALIDO)])
        with mock.patch("poc.registro.guardar", side_effect=OSError("disco lleno")):
            p = pipeline.procesar(c, copia(FORMULARIO), general=[("t.txt", b"hola")], modelo="m")
        self.assertTrue(p.resultado["valido"])
        self.assertIn("disco lleno", p.aviso_registro)

    def test_sin_archivos_legibles_igual_se_genera_el_contenido_pedido(self):
        f, p_ok = con_contenido("preguntas", "ejercicios")
        c = ClienteFalso([js(p_ok)])
        p = pipeline.procesar(c, f, general=[("foto.png", b"x")], modelo="m")
        self.assertFalse(p.ingesta.hay_material)
        self.assertTrue(p.resultado["valido"])


if __name__ == "__main__":
    unittest.main()
