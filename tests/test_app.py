"""La interfaz renderiza sin excepciones y muestra los resultados. Sin red ni API real."""

import json
import os
import pathlib
import unittest
from unittest import mock

from streamlit.testing.v1 import AppTest

from poc import pipeline
from tests.datos_de_prueba import (
    FORMULARIO,
    PLAN_VALIDO,
    ClienteFalso,
    con_contenido,
    copia,
    error_de_api,
)

# AppTest resuelve las rutas relativas contra este archivo, no contra el cwd.
APP = str(pathlib.Path(__file__).resolve().parent.parent / "poc" / "app.py")


def _app(**entorno):
    # AppTest corre el script en este mismo proceso: el entorno se controla desde acá.
    with mock.patch.dict(os.environ, entorno, clear=False):
        at = AppTest.from_file(APP, default_timeout=30)
        at.run()
    return at


def _boton(at, etiqueta):
    return next(b for b in at.button if b.label == etiqueta)


def _pedido(respuestas, formulario=None, general=None, por_tema=None):
    with mock.patch("poc.registro.guardar", return_value="registro/x.json"):
        return pipeline.procesar(
            ClienteFalso([json.dumps(r) if not isinstance(r, str) else r for r in respuestas]),
            copia(formulario or FORMULARIO),
            general=[("temario.txt", b"Capa de enlace")] if general is None else general,
            por_tema=por_tema,
            modelo="m",
        )


def _texto(at):
    return " ".join(m.value for m in at.markdown)


class TestFormulario(unittest.TestCase):
    def test_renderiza_sin_excepciones(self):
        at = _app(OPENAI_API_KEY="clave-de-prueba")
        self.assertEqual(len(at.exception), 0, [e.value for e in at.exception])
        self.assertEqual(at.title[0].value, "Study Copilot")

    def test_las_tres_opciones_de_contenido_estan_y_solo_preguntas_viene_marcada(self):
        at = _app(OPENAI_API_KEY="clave-de-prueba")
        marcadas = {c.label: c.value for c in at.checkbox}
        self.assertEqual(
            marcadas,
            {
                "Preguntas de autoevaluación": True,
                "Ejercicios prácticos": False,
                "Preguntas tipo parcial": False,
            },
        )

    def test_cada_tema_tiene_su_propio_uploader_de_archivos(self):
        at = _app(OPENAI_API_KEY="clave-de-prueba")
        # 3 temas iniciales (cada uno con el suyo) + el material general de la barra lateral.
        self.assertEqual(len(at.get("file_uploader")), 4)

    def test_agregar_y_quitar_un_tema(self):
        at = _app(OPENAI_API_KEY="clave-de-prueba")
        _boton(at, "Agregar tema").click().run()
        self.assertEqual(len(at.get("file_uploader")), 5)
        quitar = [b for b in at.button if b.key and b.key.startswith("quitar_")]
        quitar[0].click().run()
        self.assertEqual(len(at.get("file_uploader")), 4)

    def test_no_se_puede_quitar_el_ultimo_tema(self):
        at = _app(OPENAI_API_KEY="clave-de-prueba")
        for _ in range(5):
            quitar = [b for b in at.button if b.key and b.key.startswith("quitar_")]
            quitar[0].click().run()
        self.assertEqual(len([b for b in at.button if b.key and b.key.startswith("quitar_")]), 1)

    def test_sin_clave_avisa_y_deshabilita_el_boton(self):
        with mock.patch("dotenv.load_dotenv"):
            with mock.patch.dict(os.environ, clear=False):
                os.environ.pop("OPENAI_API_KEY", None)
                at = AppTest.from_file(APP, default_timeout=30)
                at.run()
        self.assertTrue(any("OPENAI_API_KEY" in e.value for e in at.error))
        self.assertTrue(_boton(at, "Generar plan").disabled)

    def test_formulario_vacio_muestra_los_errores_sin_llamar_a_la_api(self):
        at = _app(OPENAI_API_KEY="clave-de-prueba")
        with mock.patch("openai.OpenAI") as cliente:
            _boton(at, "Generar plan").click().run()
            cliente.return_value.chat.completions.create.assert_not_called()
        mensajes = [e.value for e in at.error]
        self.assertTrue(any("materia" in m for m in mensajes), mensajes)
        self.assertTrue(any("tema" in m for m in mensajes), mensajes)


class TestResultado(unittest.TestCase):
    def _mostrar(self, pedido):
        at = _app(OPENAI_API_KEY="clave-de-prueba")
        at.session_state["pedido"] = pedido
        at.run()
        self.assertEqual(len(at.exception), 0, [e.value for e in at.exception])
        return at

    def test_muestra_un_plan_valido_con_pestanas(self):
        at = self._mostrar(_pedido([PLAN_VALIDO]))
        etiquetas = [t.label for t in at.tabs]
        self.assertEqual(etiquetas, ["Plan", "Por qué", "Preguntas de autoevaluación"])
        texto = _texto(at)
        self.assertIn("2026-11-09", texto)
        self.assertIn("Capa de enlace", texto)
        self.assertTrue(any("pasó la validación" in s.value for s in at.success))

    def test_una_pestana_por_cada_tipo_pedido(self):
        f, p = con_contenido("preguntas", "ejercicios", "parcial")
        at = self._mostrar(_pedido([p], formulario=f))
        self.assertEqual(
            [t.label for t in at.tabs],
            ["Plan", "Por qué", "Preguntas de autoevaluación", "Ejercicios prácticos", "Preguntas tipo parcial"],
        )

    def test_sin_contenido_pedido_solo_hay_plan_y_explicacion(self):
        f, p = con_contenido()
        at = self._mostrar(_pedido([p], formulario=f))
        self.assertEqual([t.label for t in at.tabs], ["Plan", "Por qué"])

    def test_el_contenido_se_muestra_como_borrador(self):
        at = self._mostrar(_pedido([PLAN_VALIDO]))
        self.assertTrue(any("Borrador a revisar" in c.value for c in at.caption))
        self.assertIn("¿Qué hace Ethernet?", _texto(at))

    def test_sin_archivos_el_contenido_se_genera_y_se_marca_como_conocimiento_general(self):
        f, p = con_contenido("ejercicios")
        at = self._mostrar(_pedido([p], formulario=f, general=[]))
        self.assertTrue(any("No subiste archivos legibles" in i.value for i in at.info))
        self.assertIn("Sin archivos", _texto(at))
        self.assertIn("ejercicios de Enrutamiento", _texto(at))

    def test_el_origen_distingue_archivos_del_tema_de_los_generales(self):
        at = self._mostrar(
            _pedido(
                [PLAN_VALIDO],
                general=[("temario.txt", b"temario general")],
                por_tema={"Enrutamiento": [("rutas.txt", b"rutas")]},
            )
        )
        texto = _texto(at)
        self.assertIn("Apoyado en 1 archivo(s) de este tema y 1 de material general", texto)
        self.assertIn("este tema no tiene archivos propios", texto)

    def test_plan_invalido_se_muestra_con_sus_errores(self):
        mal = copia(PLAN_VALIDO)
        mal["plan"][1]["bloques"][0]["minutos"] = 90
        at = self._mostrar(_pedido([mal, mal]))
        self.assertTrue(any("no pasó la validación" in w.value for w in at.warning))
        self.assertIn("2026-11-10", _texto(at))

    def test_error_de_api_se_muestra_sin_romper(self):
        with mock.patch("poc.registro.guardar", return_value="registro/x.json"):
            pedido = pipeline.procesar(
                ClienteFalso([error_de_api("sin crédito")]), copia(FORMULARIO), modelo="m"
            )
        at = self._mostrar(pedido)
        self.assertTrue(any("sin crédito" in e.value for e in at.error))

    def test_archivo_rechazado_se_avisa(self):
        at = self._mostrar(_pedido([PLAN_VALIDO], general=[("foto.png", b"x")]))
        self.assertTrue(any("foto.png" in w.value for w in at.warning))

    def test_las_metricas_del_pedido_se_muestran(self):
        at = self._mostrar(_pedido([PLAN_VALIDO]))
        metricas = {m.label: m.value for m in at.metric}
        self.assertEqual(metricas["Validación"], "Aprobada")
        self.assertEqual(metricas["Intentos"], "1")


if __name__ == "__main__":
    unittest.main()
