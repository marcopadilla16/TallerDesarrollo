"""Constantes de la PoC. Lo que se quiera ajustar sin tocar la lógica va acá."""

import os
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
BANCO = RAIZ / "datos" / "ing_sistemas"
REGISTRO = RAIZ / "registro"

# 3.1.1: el modelo se fija por versión y se cambia con OPENAI_MODEL, sin tocar código.
MODELO_POR_DEFECTO = "gpt-5.4-mini-2026-03-17"


def modelo():
    return os.environ.get("OPENAI_MODEL") or MODELO_POR_DEFECTO


NIVELES = ("bajo", "medio", "alto")
ORDEN_NIVEL = {n: i for i, n in enumerate(NIVELES)}
OBJETIVOS = ("aprobar", "sacar más de 8", "preparar final")

REPASO = "Repaso general"
FORMATOS_ADMITIDOS = (".pdf", ".txt")

# 3.1.2: umbral de la celda 10 del EDA para avisar de dos versiones del mismo material.
UMBRAL_CASI_DUPLICADO = 0.30

# Cuánto se espera a la API antes de mostrar un mensaje de error en lugar de colgarse.
TIMEOUT_API_SEGUNDOS = 120

# Tipos de contenido que el estudiante puede pedir, con su etiqueta en pantalla.
# La clave es también la del JSON que devuelve el modelo.
TIPOS_CONTENIDO = {
    "preguntas": "Preguntas de autoevaluación",
    "ejercicios": "Ejercicios prácticos",
    "parcial": "Preguntas tipo parcial",
}
# Qué se pide por defecto cuando el estudiante no elige nada.
CONTENIDO_POR_DEFECTO = ("preguntas",)
# Cuántos ítems se le piden al modelo por tema y por tipo. La validación exige al menos 1.
CANTIDAD_POR_TIPO = {"preguntas": 3, "ejercicios": 2, "parcial": 2}
