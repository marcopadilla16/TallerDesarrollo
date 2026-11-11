"""Datos y utilidades comunes a los tests."""

import copy

import openai

from poc.ingesta import Documento, Ingesta

FORMULARIO = {
    "nombre_materia": "Redes",
    "fecha_examen": "2026-11-12",
    "objetivo": "aprobar",
    "temas": {"Capa de enlace": "alto", "Enrutamiento": "bajo"},
    "disponibilidad": {"2026-11-09": 2, "2026-11-10": 1},
    "contenido": ["preguntas"],
}

PLAN_VALIDO = {
    "plan": [
        {"fecha": "2026-11-09", "bloques": [
            {"tema": "Capa de enlace", "minutos": 40},
            {"tema": "Enrutamiento", "minutos": 80},
        ]},
        {"fecha": "2026-11-10", "bloques": [{"tema": "Repaso general", "minutos": 60}]},
    ],
    "explicaciones": {
        "Capa de enlace": "Nivel alto: poco tiempo.",
        "Enrutamiento": "Nivel bajo: más tiempo.",
    },
    "preguntas": {
        "Capa de enlace": ["¿Qué hace Ethernet?"],
        "Enrutamiento": ["¿Qué es una tabla de rutas?"],
    },
}


def con_contenido(*tipos):
    """Formulario y plan válidos para exactamente los tipos de contenido indicados."""
    f = copy.deepcopy(FORMULARIO)
    f["contenido"] = list(tipos)
    p = copy.deepcopy(PLAN_VALIDO)
    p.pop("preguntas")
    for tipo in tipos:
        p[tipo] = {t: [f"{tipo} de {t}"] for t in f["temas"]}
    return f, p


def copia(x):
    return copy.deepcopy(x)


def ingesta_con(general=(), por_tema=None):
    """Ingesta ya armada, sin pasar por los archivos."""
    ing = Ingesta()
    ing.general = [Documento(n, t) for n, t in general]
    for tema, docs in (por_tema or {}).items():
        ing.por_tema[tema] = [Documento(n, t, tema) for n, t in docs]
    return ing


class _Mensaje:
    def __init__(self, content):
        self.content = content


class _Eleccion:
    def __init__(self, content):
        self.message = _Mensaje(content)


class _Uso:
    total_tokens = 100


class _Respuesta:
    def __init__(self, content):
        self.choices = [_Eleccion(content)]
        self.usage = _Uso()


class ClienteFalso:
    """Reemplaza al cliente de OpenAI. Cada llamada consume un item de `respuestas`.

    Un item puede ser un str (lo que devuelve el modelo) o una excepción (se levanta).
    """

    def __init__(self, respuestas):
        self.respuestas = list(respuestas)
        self.llamadas = []
        self.chat = self
        self.completions = self

    def create(self, **kwargs):
        self.llamadas.append(kwargs)
        item = self.respuestas.pop(0)
        if isinstance(item, Exception):
            raise item
        return _Respuesta(item)


def error_de_api(mensaje="sin crédito"):
    return openai.OpenAIError(mensaje)
