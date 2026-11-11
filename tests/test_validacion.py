import unittest

from poc.validacion import errores_prioridad, validar
from tests.datos_de_prueba import FORMULARIO, PLAN_VALIDO, con_contenido, copia


class TestValidar(unittest.TestCase):
    def test_plan_valido(self):
        self.assertEqual(validar(copia(PLAN_VALIDO), FORMULARIO), [])

    def test_sin_lista_plan(self):
        self.assertEqual(
            validar({"explicaciones": {}}, FORMULARIO),
            ["la respuesta no tiene la lista 'plan'"],
        )

    def test_respuesta_que_no_es_dict(self):
        self.assertTrue(validar(["x"], FORMULARIO))

    def test_se_pasa_de_las_horas(self):
        p = copia(PLAN_VALIDO)
        p["plan"][1]["bloques"][0]["minutos"] = 90  # el 10/11 hay 60 min
        errores = validar(p, FORMULARIO)
        self.assertTrue(any("90 min planificados, 60 disponibles" in e for e in errores))

    def test_fecha_no_disponible(self):
        p = copia(PLAN_VALIDO)
        p["plan"][1]["fecha"] = "2026-11-11"
        self.assertTrue(any("fecha no disponible" in e for e in validar(p, FORMULARIO)))

    def test_tema_inventado(self):
        p = copia(PLAN_VALIDO)
        p["plan"][0]["bloques"].append({"tema": "Criptografía", "minutos": 10})
        self.assertTrue(any("no está en el formulario" in e for e in validar(p, FORMULARIO)))

    def test_repaso_general_no_es_tema_inventado(self):
        errores = validar(copia(PLAN_VALIDO), FORMULARIO)
        self.assertFalse(any("Repaso general" in e for e in errores))

    def test_tema_sin_tiempo(self):
        p = copia(PLAN_VALIDO)
        p["plan"][0]["bloques"] = [{"tema": "Enrutamiento", "minutos": 100}]
        self.assertTrue(any("tema sin tiempo asignado: Capa de enlace" in e
                            for e in validar(p, FORMULARIO)))

    def test_tema_renombrado_cuenta_como_inventado_y_sin_tiempo(self):
        p = copia(PLAN_VALIDO)
        p["plan"][0]["bloques"][0]["tema"] = "Enlace y Ethernet"
        errores = validar(p, FORMULARIO)
        self.assertTrue(any("Enlace y Ethernet" in e for e in errores))
        self.assertTrue(any("tema sin tiempo asignado: Capa de enlace" in e for e in errores))

    def test_tema_sin_explicacion(self):
        p = copia(PLAN_VALIDO)
        p["explicaciones"]["Enrutamiento"] = " "
        self.assertTrue(any("sin explicación: Enrutamiento" in e for e in validar(p, FORMULARIO)))

    def test_minutos_no_numericos(self):
        p = copia(PLAN_VALIDO)
        p["plan"][0]["bloques"][0]["minutos"] = "40"
        self.assertTrue(any("sin minutos válidos" in e for e in validar(p, FORMULARIO)))


class TestContenido(unittest.TestCase):
    def test_tema_sin_preguntas_cuando_se_pidieron(self):
        f, p = con_contenido("preguntas")
        del p["preguntas"]["Enrutamiento"]
        self.assertTrue(any("sin preguntas de autoevaluación" in e and "Enrutamiento" in e
                            for e in validar(p, f)))

    def test_clave_ausente_cuenta_como_error_en_todos_los_temas(self):
        f, p = con_contenido("ejercicios")
        del p["ejercicios"]
        errores = [e for e in validar(p, f) if "ejercicios" in e]
        self.assertEqual(len(errores), len(f["temas"]))

    def test_items_vacios_no_cuentan(self):
        f, p = con_contenido("parcial")
        p["parcial"]["Enrutamiento"] = ["", "  "]
        self.assertTrue(any("sin preguntas tipo parcial" in e for e in validar(p, f)))

    def test_los_tres_tipos_validos(self):
        f, p = con_contenido("preguntas", "ejercicios", "parcial")
        self.assertEqual(validar(p, f), [])

    def test_cada_tipo_se_valida_por_separado(self):
        f, p = con_contenido("preguntas", "ejercicios")
        del p["ejercicios"]["Capa de enlace"]
        errores = validar(p, f)
        self.assertEqual(len(errores), 1)
        self.assertIn("ejercicios prácticos", errores[0])

    def test_sin_contenido_pedido_no_se_exige_nada(self):
        f, p = con_contenido()
        self.assertEqual(validar(p, f), [])

    def test_lo_que_no_se_pidio_no_se_valida(self):
        f, p = con_contenido("preguntas")
        p["ejercicios"] = "basura"
        self.assertEqual(validar(p, f), [])


class TestPrioridad(unittest.TestCase):
    def test_prioridad_coherente(self):
        self.assertEqual(errores_prioridad(copia(PLAN_VALIDO), FORMULARIO), [])

    def test_prioridad_invertida(self):
        p = copia(PLAN_VALIDO)
        p["plan"][0]["bloques"] = [
            {"tema": "Capa de enlace", "minutos": 100},  # alto con más tiempo que bajo
            {"tema": "Enrutamiento", "minutos": 20},
        ]
        errores = errores_prioridad(p, FORMULARIO)
        self.assertEqual(len(errores), 1)
        self.assertIn("nivel bajo", errores[0])

    def test_no_se_puede_medir_si_falta_un_tema(self):
        p = copia(PLAN_VALIDO)
        p["plan"][0]["bloques"] = [{"tema": "Enrutamiento", "minutos": 100}]
        self.assertIsNone(errores_prioridad(p, FORMULARIO))

    def test_no_se_puede_medir_si_el_plan_es_ilegible(self):
        self.assertIsNone(errores_prioridad(None, FORMULARIO))
        self.assertIsNone(errores_prioridad({"plan": "nada"}, FORMULARIO))


if __name__ == "__main__":
    unittest.main()
