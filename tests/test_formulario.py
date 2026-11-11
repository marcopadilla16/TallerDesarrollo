import unittest

from poc.formulario import tipos_pedidos, validar_formulario
from tests.datos_de_prueba import FORMULARIO, copia


class TestFormulario(unittest.TestCase):
    def test_formulario_valido(self):
        self.assertEqual(validar_formulario(copia(FORMULARIO)), [])

    def test_materia_vacia(self):
        f = copia(FORMULARIO)
        f["nombre_materia"] = "  "
        self.assertTrue(any("materia" in e for e in validar_formulario(f)))

    def test_sin_temas(self):
        f = copia(FORMULARIO)
        f["temas"] = {}
        self.assertTrue(any("tema" in e for e in validar_formulario(f)))

    def test_nivel_invalido(self):
        f = copia(FORMULARIO)
        f["temas"]["Enrutamiento"] = "altísimo"
        self.assertTrue(any("nivel" in e for e in validar_formulario(f)))

    def test_objetivo_invalido(self):
        f = copia(FORMULARIO)
        f["objetivo"] = "zafar"
        self.assertTrue(any("objetivo" in e for e in validar_formulario(f)))

    def test_dia_posterior_al_examen(self):
        f = copia(FORMULARIO)
        f["disponibilidad"]["2026-11-12"] = 2  # el día del examen no cuenta
        self.assertTrue(any("anterior al examen" in e for e in validar_formulario(f)))

    def test_horas_negativas(self):
        f = copia(FORMULARIO)
        f["disponibilidad"]["2026-11-09"] = -1
        self.assertTrue(any("entre 0 y 24" in e for e in validar_formulario(f)))

    def test_todo_en_cero(self):
        f = copia(FORMULARIO)
        f["disponibilidad"] = {"2026-11-09": 0, "2026-11-10": 0}
        self.assertTrue(any("0 horas" in e for e in validar_formulario(f)))

    def test_fecha_de_examen_invalida(self):
        f = copia(FORMULARIO)
        f["fecha_examen"] = "mañana"
        self.assertTrue(any("fecha del examen" in e for e in validar_formulario(f)))

    def test_contenido_desconocido(self):
        f = copia(FORMULARIO)
        f["contenido"] = ["preguntas", "chistes"]
        self.assertTrue(any("chistes" in e for e in validar_formulario(f)))

    def test_contenido_vacio_o_ausente_es_valido(self):
        f = copia(FORMULARIO)
        f["contenido"] = []
        self.assertEqual(validar_formulario(f), [])
        del f["contenido"]
        self.assertEqual(validar_formulario(f), [])


class TestTiposPedidos(unittest.TestCase):
    def test_conserva_el_orden_y_saca_repetidos_y_desconocidos(self):
        f = {"contenido": ["parcial", "preguntas", "parcial", "chistes"]}
        self.assertEqual(tipos_pedidos(f), ["parcial", "preguntas"])

    def test_sin_clave(self):
        self.assertEqual(tipos_pedidos({}), [])


if __name__ == "__main__":
    unittest.main()
