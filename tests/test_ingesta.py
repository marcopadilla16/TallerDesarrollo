import unittest

from poc import config
from poc.ingesta import (
    Documento,
    archivos_del_banco,
    buscar_casi_duplicados,
    ingerir,
    leer_archivo,
    materias_del_banco,
    origen_por_tema,
)
from tests.datos_de_prueba import ingesta_con


class TestLeerArchivo(unittest.TestCase):
    def test_txt_legible(self):
        doc, rechazo = leer_archivo("apuntes.txt", "Hola, ¿qué tal?".encode("utf-8"))
        self.assertIsNone(rechazo)
        self.assertEqual(doc.nombre, "apuntes.txt")
        self.assertIsNone(doc.tema)
        self.assertIn("¿qué tal?", doc.texto)

    def test_el_documento_recuerda_su_tema(self):
        doc, _ = leer_archivo("guia.txt", b"contenido", tema="Matrices")
        self.assertEqual(doc.tema, "Matrices")
        self.assertEqual(doc.etiqueta, "Matrices › guia.txt")

    def test_txt_vacio_se_rechaza(self):
        doc, rechazo = leer_archivo("vacio.txt", b"   \n ")
        self.assertIsNone(doc)
        self.assertIn("no tiene texto", rechazo)

    def test_formato_no_admitido(self):
        doc, rechazo = leer_archivo("foto.png", b"\x89PNG")
        self.assertIsNone(doc)
        self.assertIn("formato no admitido", rechazo)

    def test_sin_extension(self):
        doc, rechazo = leer_archivo("archivo", b"hola")
        self.assertIsNone(doc)
        self.assertIn("formato no admitido", rechazo)

    def test_pdf_corrupto_se_rechaza_sin_romper(self):
        doc, rechazo = leer_archivo("roto.pdf", b"esto no es un pdf")
        self.assertIsNone(doc)
        self.assertIn("no se pudo abrir", rechazo)

    def test_extension_en_mayusculas(self):
        doc, _ = leer_archivo("APUNTES.TXT", b"contenido")
        self.assertIsNotNone(doc)


class TestIngerir(unittest.TestCase):
    def test_mezcla_de_archivos_buenos_y_malos(self):
        r = ingerir([("a.txt", b"texto util"), ("b.png", b"x"), ("c.txt", b"")])
        self.assertEqual([d.nombre for d in r.general], ["a.txt"])
        self.assertEqual(len(r.rechazados), 2)
        self.assertTrue(r.hay_material)

    def test_sin_archivos(self):
        r = ingerir()
        self.assertFalse(r.hay_material)
        self.assertEqual(r.rechazados, [])
        self.assertEqual(r.documentos, [])

    def test_si_no_queda_nada_legible_no_hay_material(self):
        self.assertFalse(ingerir([("x.png", b"x")]).hay_material)

    def test_archivos_por_tema(self):
        r = ingerir(por_tema={"Matrices": [("m.txt", b"matrices")], "Autovalores": [("a.txt", b"autovalores")]})
        self.assertEqual([d.nombre for d in r.por_tema["Matrices"]], ["m.txt"])
        self.assertEqual(r.por_tema["Autovalores"][0].tema, "Autovalores")
        self.assertEqual(r.general, [])
        self.assertEqual(len(r.documentos), 2)

    def test_general_y_por_tema_juntos(self):
        r = ingerir([("temario.txt", b"temario")], {"Matrices": [("m.txt", b"matrices")]})
        self.assertEqual(len(r.documentos), 2)
        self.assertTrue(r.hay_material)

    def test_el_rechazo_de_un_archivo_de_tema_dice_de_que_tema_era(self):
        r = ingerir(por_tema={"Matrices": [("foto.png", b"x")]})
        self.assertFalse(r.hay_material)
        self.assertTrue(r.rechazados[0].startswith("Matrices ›"))
        self.assertIn("foto.png", r.rechazados[0])

    def test_un_tema_con_todos_los_archivos_rechazados_no_figura(self):
        r = ingerir(por_tema={"Matrices": [("foto.png", b"x")]})
        self.assertNotIn("Matrices", r.por_tema)


class TestOrigen(unittest.TestCase):
    def test_cuenta_archivos_propios_y_generales(self):
        ing = ingesta_con(general=[("temario", "x")], por_tema={"A": [("a1", "x"), ("a2", "x")]})
        self.assertEqual(
            origen_por_tema(["A", "B"], ing),
            {"A": {"propios": 2, "general": 1}, "B": {"propios": 0, "general": 1}},
        )

    def test_sin_archivos(self):
        self.assertEqual(origen_por_tema(["A"], ingesta_con()), {"A": {"propios": 0, "general": 0}})


class TestCasiDuplicados(unittest.TestCase):
    TEXTO = "protocolo enrutamiento direccionamiento subredes capas transporte aplicacion"

    def test_dos_versiones_casi_iguales(self):
        a = Documento("v1.txt", self.TEXTO)
        b = Documento("v2.txt", self.TEXTO + " agregado nuevo")
        avisos = buscar_casi_duplicados([a, b])
        self.assertEqual(len(avisos), 1)
        self.assertIn("v1.txt", avisos[0])

    def test_documentos_distintos_no_avisan(self):
        a = Documento("a.txt", self.TEXTO)
        b = Documento("b.txt", "simplex dualidad transporte asignacion sensibilidad programacion lineal")
        self.assertEqual(buscar_casi_duplicados([a, b]), [])

    def test_un_solo_documento(self):
        self.assertEqual(buscar_casi_duplicados([Documento("a.txt", self.TEXTO)]), [])

    def test_el_mismo_archivo_en_dos_temas_se_avisa_con_el_tema(self):
        r = ingerir(por_tema={"A": [("guia.txt", self.TEXTO.encode())], "B": [("guia.txt", self.TEXTO.encode())]})
        self.assertEqual(len(r.casi_duplicados), 1)
        self.assertIn("A › guia.txt", r.casi_duplicados[0])
        self.assertIn("B › guia.txt", r.casi_duplicados[0])


@unittest.skipUnless(config.BANCO.exists(), "no está la carpeta datos/")
class TestBanco(unittest.TestCase):
    """3.1.5: 0 archivos del banco rompen la ingesta: cada uno da texto o un mensaje."""

    def test_cada_archivo_da_un_documento_o_un_mensaje(self):
        total = 0
        for materia in materias_del_banco():
            for nombre, contenido in archivos_del_banco(materia):
                doc, rechazo = leer_archivo(nombre, contenido)
                self.assertTrue((doc is None) != (rechazo is None), nombre)
                total += 1
        self.assertGreater(total, 0)

    def test_redes_tiene_el_par_de_casi_duplicados_de_la_celda_10(self):
        # Los dos compendios de Redes: Jaccard 0,33 en el EDA.
        r = ingerir(archivos_del_banco("redes"))
        self.assertTrue(any("examen_01" in a and "examen_02" in a for a in r.casi_duplicados))


if __name__ == "__main__":
    unittest.main()
