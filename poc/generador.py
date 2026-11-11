"""Generación, validación y reintento (pasos 3, 4 y 5 del workflow, 3.1.3).

generar() recibe el cliente ya armado, así los tests lo reemplazan por uno simulado.
Si el plan no pasa la validación después del reintento, se devuelve igual con sus
errores: no se oculta (3.1.3, paso 5).
"""

import json
import time

from poc import prompts
from poc.validacion import errores_prioridad, validar


def _llamar(cliente, modelo, mensajes):
    inicio = time.perf_counter()
    r = cliente.chat.completions.create(
        model=modelo,
        messages=mensajes,
        response_format={"type": "json_object"},
    )
    segundos = time.perf_counter() - inicio
    tokens = r.usage.total_tokens if r.usage else 0
    return r.choices[0].message.content, segundos, tokens


def _parsear(texto):
    try:
        return json.loads(texto)
    except (json.JSONDecodeError, TypeError):
        return None


def _intento(cliente, modelo, mensajes, f):
    """Una llamada validada. Un error de la API no levanta: queda como error del intento."""
    import openai

    try:
        texto, segundos, tokens = _llamar(cliente, modelo, mensajes)
    except openai.OpenAIError as e:
        return {
            "texto": None, "respuesta": None, "segundos": 0.0, "tokens": 0,
            "errores": [], "prioridad": None, "error_api": f"{type(e).__name__}: {e}",
        }
    respuesta = _parsear(texto)
    errores = validar(respuesta, f) if respuesta is not None else ["JSON inválido"]
    return {
        "texto": texto, "respuesta": respuesta, "segundos": segundos, "tokens": tokens,
        "errores": errores, "prioridad": errores_prioridad(respuesta, f),
        "error_api": None,
    }


def generar(cliente, modelo, f, ingesta):
    """Corre el workflow y devuelve un dict con el plan y todo lo que hace falta registrar.

    Claves: respuesta, valido, errores, errores_prioridad (None si no se pudo medir),
    intentos, segundos, tokens, error_api (None si la API respondió).
    """
    msgs = prompts.mensajes(f, ingesta)
    intento = _intento(cliente, modelo, msgs, f)
    intentos, segundos, tokens = 1, intento["segundos"], intento["tokens"]

    a_corregir = intento["errores"] + (intento["prioridad"] or [])
    if a_corregir and intento["texto"] is not None:
        msgs = prompts.mensajes_de_reintento(msgs, intento["texto"], a_corregir)
        nuevo = _intento(cliente, modelo, msgs, f)
        intentos += 1
        segundos += nuevo["segundos"]
        tokens += nuevo["tokens"]
        # Si el reintento cayó por la API, se conserva el primer plan con sus errores.
        intento = {**intento, "error_api": nuevo["error_api"]} if nuevo["error_api"] else nuevo

    return {
        "respuesta": intento["respuesta"],
        "valido": intento["error_api"] is None and not intento["errores"],
        "errores": intento["errores"],
        "errores_prioridad": intento["prioridad"],
        "intentos": intentos,
        "segundos": round(segundos, 1),
        "tokens": tokens,
        "error_api": intento["error_api"],
    }
