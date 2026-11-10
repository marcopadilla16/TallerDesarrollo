"""Validación del formulario (paso 1 del workflow, 3.1.3).

El formulario es un dict:
    {"nombre_materia": str, "fecha_examen": "AAAA-MM-DD", "objetivo": str,
     "temas": {tema: nivel}, "disponibilidad": {"AAAA-MM-DD": horas},
     "contenido": ["preguntas", "ejercicios", "parcial"]}   # opcional, puede ir vacío
"""

import datetime as dt

from poc.config import NIVELES, OBJETIVOS, TIPOS_CONTENIDO


def _fecha(texto):
    try:
        return dt.date.fromisoformat(texto)
    except (TypeError, ValueError):
        return None


def tipos_pedidos(f):
    """Tipos de contenido que se van a generar, sin repetidos ni desconocidos."""
    return [t for t in dict.fromkeys(f.get("contenido") or []) if t in TIPOS_CONTENIDO]


def validar_formulario(f):
    """Lista de errores para mostrarle al usuario; vacía si el formulario sirve."""
    errores = []

    if not str(f.get("nombre_materia", "")).strip():
        errores.append("Falta el nombre de la materia.")
    if f.get("objetivo") not in OBJETIVOS:
        errores.append(f"El objetivo tiene que ser uno de: {', '.join(OBJETIVOS)}.")
    for tipo in f.get("contenido") or []:
        if tipo not in TIPOS_CONTENIDO:
            errores.append(f"No sé generar «{tipo}». Opciones: {', '.join(TIPOS_CONTENIDO)}.")

    examen = _fecha(f.get("fecha_examen"))
    if examen is None:
        errores.append("La fecha del examen no es válida.")

    temas = f.get("temas") or {}
    if not temas:
        errores.append("Cargá al menos un tema.")
    for tema, nivel in temas.items():
        if not str(tema).strip():
            errores.append("Hay un tema sin nombre.")
        if nivel not in NIVELES:
            errores.append(f"El nivel de «{tema}» tiene que ser uno de: {', '.join(NIVELES)}.")

    dias = f.get("disponibilidad") or {}
    if not dias:
        errores.append("Cargá la disponibilidad de al menos un día.")
    for fecha, horas in dias.items():
        dia = _fecha(fecha)
        if dia is None:
            errores.append(f"La fecha de disponibilidad {fecha!r} no es válida.")
            continue
        if examen and dia >= examen:
            errores.append(f"{fecha}: la disponibilidad tiene que ser anterior al examen.")
        if isinstance(horas, bool) or not isinstance(horas, (int, float)) or not 0 <= horas <= 24:
            errores.append(f"{fecha}: las horas tienen que estar entre 0 y 24.")

    horas_validas = [h for h in dias.values() if isinstance(h, (int, float)) and not isinstance(h, bool)]
    if dias and not any(h > 0 for h in horas_validas):
        errores.append("Todos los días tienen 0 horas: no hay tiempo para armar un plan.")
    return errores
