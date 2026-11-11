"""Ingesta (paso 2 del workflow, 3.1.2 y 3.1.3).

Recibe archivos como (nombre, bytes), extrae el texto y rechaza con un mensaje lo que no
se puede usar. Nunca levanta una excepción por un archivo malo: cada archivo da un
documento o un aviso. El material va entero al modelo, sin tope ni recorte.

Los archivos pueden ser de un tema puntual o generales (temario, parciales que abarcan
varios temas). Sin archivos también es un caso válido: el modelo usa su conocimiento.
"""

import io
import itertools
import re
from dataclasses import dataclass, field

from poc.config import BANCO, FORMATOS_ADMITIDOS, UMBRAL_CASI_DUPLICADO

# Misma tokenización que la celda 10 del EDA.
_PALABRAS = re.compile(r"[a-záéíóúñ]{5,}")


@dataclass
class Documento:
    nombre: str
    texto: str
    tema: str = None  # None: material general

    @property
    def etiqueta(self):
        return f"{self.tema} › {self.nombre}" if self.tema else self.nombre


@dataclass
class Ingesta:
    general: list = field(default_factory=list)
    por_tema: dict = field(default_factory=dict)  # tema -> [Documento]
    rechazados: list = field(default_factory=list)  # mensajes: "nombre: motivo"
    casi_duplicados: list = field(default_factory=list)  # mensajes, sólo informativos

    @property
    def documentos(self):
        return self.general + [d for docs in self.por_tema.values() for d in docs]

    @property
    def hay_material(self):
        return bool(self.documentos)


def _extraer_texto(nombre, contenido):
    """Texto del archivo, o None si el formato no es admitido. Puede levantar excepciones."""
    sufijo = "." + nombre.rsplit(".", 1)[-1].lower() if "." in nombre else ""
    if sufijo == ".pdf":
        import pypdf

        lector = pypdf.PdfReader(io.BytesIO(contenido))
        return "\n".join(p.extract_text() or "" for p in lector.pages)
    if sufijo == ".txt":
        return contenido.decode("utf-8", errors="replace")
    return None


def leer_archivo(nombre, contenido, tema=None):
    """(Documento, None) si sirve; (None, mensaje) si se rechaza."""
    try:
        texto = _extraer_texto(nombre, contenido)
    except Exception as e:  # PDF corrupto, cifrado, etc.: es un rechazo, no un error del sistema.
        return None, f"{nombre}: no se pudo abrir ({type(e).__name__})."
    if texto is None:
        admitidos = " y ".join(FORMATOS_ADMITIDOS)
        return None, f"{nombre}: formato no admitido (sólo {admitidos})."
    if not texto.strip():
        return None, f"{nombre}: no tiene texto. Si es un escaneado o una foto, no se puede leer."
    return Documento(nombre, texto.strip(), tema), None


def _vocabulario(texto):
    return set(_PALABRAS.findall(texto.lower()))


def buscar_casi_duplicados(documentos):
    """Mensajes por cada par de documentos con Jaccard de vocabulario sobre el umbral."""
    vocabularios = [(d.etiqueta, _vocabulario(d.texto)) for d in documentos]
    avisos = []
    for (a, va), (b, vb) in itertools.combinations(vocabularios, 2):
        if not va or not vb:
            continue
        similitud = len(va & vb) / len(va | vb)
        if similitud > UMBRAL_CASI_DUPLICADO:
            avisos.append(
                f"{a} y {b} se parecen mucho ({similitud:.2f}): ¿son dos versiones del "
                "mismo material? Se usan las dos."
            )
    return avisos


def ingerir(general=(), por_tema=None):
    """general: iterable de (nombre, bytes). por_tema: {tema: iterable de (nombre, bytes)}."""
    resultado = Ingesta()
    for nombre, contenido in general:
        documento, rechazo = leer_archivo(nombre, contenido)
        if rechazo:
            resultado.rechazados.append(rechazo)
        else:
            resultado.general.append(documento)
    for tema, archivos in (por_tema or {}).items():
        for nombre, contenido in archivos:
            documento, rechazo = leer_archivo(nombre, contenido, tema)
            if rechazo:
                resultado.rechazados.append(f"{tema} › {rechazo}")
            else:
                resultado.por_tema.setdefault(tema, []).append(documento)
    resultado.casi_duplicados = buscar_casi_duplicados(resultado.documentos)
    return resultado


def origen_por_tema(temas, ingesta):
    """Cuántos archivos apoyan a cada tema: {tema: {"propios": n, "general": n}}."""
    general = len(ingesta.general)
    return {t: {"propios": len(ingesta.por_tema.get(t, [])), "general": general} for t in temas}


def archivos_del_banco(materia):
    """Archivos de una materia de datos/ como (nombre, bytes), para ejercitar el sistema."""
    return [
        (a.relative_to(BANCO / materia).as_posix(), a.read_bytes())
        for a in sorted((BANCO / materia).rglob("*"))
        if a.is_file()
    ]


def materias_del_banco():
    return sorted(p.name for p in BANCO.iterdir() if p.is_dir()) if BANCO.exists() else []
