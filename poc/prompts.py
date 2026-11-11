"""Prompts del workflow. Se editan acá, sin tocar la lógica.

Las reglas 1 a 5 son las de experimentos/prueba_modelo.py (lo medido en 3.1.1). El contenido
extra (preguntas, ejercicios, preguntas tipo parcial) es nuevo: la prueba no lo incluía.
"""

from poc.config import CANTIDAD_POR_TIPO, REPASO
from poc.formulario import tipos_pedidos

_FORMATO_BASE = (
    '"plan": [{"fecha": "AAAA-MM-DD", "bloques": [{"tema": "...", "minutos": 60}]}], '
    '"explicaciones": {"<tema>": "por qué se le dio ese tiempo"}'
)

REGLAS = f"""Sos un asistente que arma planes de estudio. Reglas obligatorias:
1. Usá sólo las fechas de la disponibilidad, y en cada fecha no superes las horas
   disponibles (horas x 60 minutos). Una fecha con 0 horas no lleva bloques.
2. Cada tema del formulario tiene al menos un bloque. No agregues temas, salvo
   "{REPASO}".
3. Los temas de nivel bajo reciben más minutos que los de nivel medio, y estos
   más que los de nivel alto. El objetivo ajusta cuánto profundizar.
4. Si alcanza el tiempo, reservá un bloque de "{REPASO}" en la última fecha.
5. En "explicaciones" va una entrada por cada tema del formulario, con el
   motivo en una oración que mencione su nivel."""

# Qué se le pide al modelo por cada tipo de contenido. {n} es la cantidad por tema.
_PEDIDO_POR_TIPO = {
    "preguntas": "{n} preguntas de autoevaluación de respuesta corta, para que el estudiante compruebe si entendió el tema",
    "ejercicios": "{n} ejercicios prácticos para resolver, con enunciado completo y sin resolverlos",
    "parcial": "{n} preguntas con el estilo y la exigencia de un parcial universitario, con enunciado completo",
}


def _regla_de_contenido(tipos):
    if not tipos:
        return ""
    lineas = [f'   - "{t}": {_PEDIDO_POR_TIPO[t].format(n=CANTIDAD_POR_TIPO[t])}.' for t in tipos]
    return (
        '\n6. Además, para cada tema del formulario devolvé una entrada en cada una de estas claves:\n'
        + "\n".join(lineas)
        + "\n   Apoyate en el material del estudiante cuando el tema lo tenga. Si un tema no tiene"
        "\n   material, usá tu conocimiento general de la materia. Todo es un borrador que el"
        "\n   estudiante va a revisar: no inventes datos ni citas."
    )


def formato(tipos):
    extra = "".join(f', "{t}": {{"<tema>": ["...", "..."]}}' for t in tipos)
    return "{" + _FORMATO_BASE + extra + "}"


def reglas(tipos):
    return f"{REGLAS}{_regla_de_contenido(tipos)}\nRespondé sólo con JSON, con esta forma: {formato(tipos)}"


def formulario_en_texto(f):
    temas = "\n".join(f"- {t}: nivel {n}" for t, n in f["temas"].items())
    dias = "\n".join(f"- {d}: {h} h" for d, h in f["disponibilidad"].items())
    return (
        f"Materia: {f['nombre_materia']}\n"
        f"Fecha del examen: {f['fecha_examen']}\n"
        f"Objetivo: {f['objetivo']}\n"
        f"Temas y mi nivel:\n{temas}\n"
        f"Horas disponibles por día:\n{dias}"
    )


def material_en_texto(ingesta):
    """Material general primero y después el de cada tema, con su encabezado."""
    partes = []
    if ingesta.general:
        docs = "\n\n".join(f"### {d.nombre}\n{d.texto}" for d in ingesta.general)
        partes.append(f"Material general de la materia:\n{docs}")
    for tema, documentos in ingesta.por_tema.items():
        docs = "\n\n".join(f"### {d.nombre}\n{d.texto}" for d in documentos)
        partes.append(f"Material del tema «{tema}»:\n{docs}")
    return "\n\n".join(partes)


def mensajes(f, ingesta):
    """Mensajes del primer intento."""
    pedido = formulario_en_texto(f)
    if ingesta.hay_material:
        pedido += f"\n\n{material_en_texto(ingesta)}"
    else:
        pedido += "\n\nNo subí material de la cursada."
    return [
        {"role": "system", "content": reglas(tipos_pedidos(f))},
        {"role": "user", "content": pedido},
    ]


def mensajes_de_reintento(anteriores, respuesta_previa, errores):
    """Mensajes del reintento: lo anterior, la respuesta del modelo y los errores concretos."""
    return anteriores + [
        {"role": "assistant", "content": respuesta_previa},
        {
            "role": "user",
            "content": "El plan tiene estos errores:\n- " + "\n- ".join(errores)
            + "\nCorregilo y devolvé el JSON completo.",
        },
    ]
