"""Validación del JSON del modelo (paso 4 del workflow, 3.1.3).

Portada de validar() y errores_prioridad() de experimentos/prueba_modelo.py, que es lo
que se midió en 3.1.1, con una diferencia: acá también se chequean las preguntas.

La respuesta esperada es:
    {"plan": [{"fecha": "AAAA-MM-DD", "bloques": [{"tema": str, "minutos": int}]}],
     "explicaciones": {tema: str},
     "preguntas": {tema: [str, ...]},      # una clave por cada tipo que el estudiante pidió
     "ejercicios": {tema: [str, ...]},
     "parcial": {tema: [str, ...]}}
"""

import statistics

from poc.config import ORDEN_NIVEL, REPASO, TIPOS_CONTENIDO
from poc.formulario import tipos_pedidos


def minutos_validos(minutos):
    return not isinstance(minutos, bool) and isinstance(minutos, (int, float)) and minutos > 0


def validar(respuesta, f):
    """Errores estructurales del plan; lista vacía si es válido."""
    if not isinstance(respuesta, dict) or not isinstance(respuesta.get("plan"), list):
        return ["la respuesta no tiene la lista 'plan'"]
    explicaciones = respuesta.get("explicaciones")
    if not isinstance(explicaciones, dict):
        explicaciones = {}
    tipos = tipos_pedidos(f)

    errores = []
    minutos_por_dia = {}
    minutos_por_tema = {t: 0 for t in f["temas"]}
    for dia in respuesta["plan"]:
        if not isinstance(dia, dict):
            errores.append(f"día con formato inválido: {dia!r:.60}")
            continue
        fecha = dia.get("fecha")
        if not isinstance(fecha, str) or fecha not in f["disponibilidad"]:
            errores.append(f"fecha no disponible: {fecha!r:.60}")
            continue
        bloques = dia.get("bloques") or []
        if not isinstance(bloques, list):
            errores.append(f"{fecha}: 'bloques' no es una lista")
            continue
        for bloque in bloques:
            if not isinstance(bloque, dict):
                errores.append(f"{fecha}: bloque con formato inválido ({bloque!r:.60})")
                continue
            tema, minutos = bloque.get("tema"), bloque.get("minutos")
            if not isinstance(tema, str):
                errores.append(f"{fecha}: bloque sin tema ({tema!r:.60})")
                continue
            if not minutos_validos(minutos):
                errores.append(f"{fecha}: bloque sin minutos válidos ({tema})")
                continue
            minutos_por_dia[fecha] = minutos_por_dia.get(fecha, 0) + minutos
            if tema in minutos_por_tema:
                minutos_por_tema[tema] += minutos
            elif tema != REPASO:
                errores.append(f"{fecha}: tema que no está en el formulario ({tema})")

    for fecha, total in minutos_por_dia.items():
        limite = f["disponibilidad"][fecha] * 60
        if total > limite:
            errores.append(f"{fecha}: {total} min planificados, {limite} disponibles")
    for tema, total in minutos_por_tema.items():
        if total == 0:
            errores.append(f"tema sin tiempo asignado: {tema}")
        if not str(explicaciones.get(tema, "")).strip():
            errores.append(f"tema sin explicación: {tema}")
        for tipo in tipos:
            items = respuesta.get(tipo)
            if not _items_validos(items.get(tema) if isinstance(items, dict) else None):
                errores.append(f"tema sin {TIPOS_CONTENIDO[tipo].lower()}: {tema}")
    return errores


def _items_validos(lista):
    return isinstance(lista, list) and any(isinstance(p, str) and p.strip() for p in lista)


def errores_prioridad(respuesta, f):
    """Errores de prioridad: el promedio de minutos por nivel cumple bajo >= medio >= alto.

    Devuelve None si no se puede medir: plan ilegible, o algún tema del formulario sin
    minutos (por ejemplo, porque el modelo lo renombró). Sin esa condición, un plan con los
    temas renombrados tiene todo en cero y pasaría por coherente.
    """
    try:
        minutos = {t: 0 for t in f["temas"]}
        for dia in respuesta["plan"]:
            for bloque in dia.get("bloques") or []:
                tema = bloque.get("tema")
                if isinstance(tema, str) and tema in minutos and minutos_validos(bloque.get("minutos")):
                    minutos[tema] += bloque["minutos"]
    except (TypeError, KeyError, AttributeError):
        return None
    if not all(minutos.values()):
        return None

    por_nivel = {}
    for tema, nivel in f["temas"].items():
        por_nivel.setdefault(nivel, []).append(minutos[tema])
    promedios = [(n, statistics.mean(por_nivel[n])) for n in sorted(por_nivel, key=ORDEN_NIVEL.get)]
    return [
        f"prioridad: los temas de nivel {a} tienen {ma:.0f} min de promedio y los de nivel "
        f"{b} {mb:.0f}; los de nivel {a} tienen que recibir al menos lo mismo"
        for (a, ma), (b, mb) in zip(promedios, promedios[1:])
        if ma < mb
    ]
