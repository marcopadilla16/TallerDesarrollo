"""Registro local por pedido (paso 6 del workflow, 3.1.2): un JSON por pedido en registro/.

Guarda el formulario, los archivos con sus avisos, el plan, los intentos, los tokens y el
tiempo. No guarda el texto de los archivos: sólo su nombre, su tema y su tamaño.
"""

import datetime as dt
import json

from poc.config import REGISTRO


def guardar(formulario, ingesta, resultado, modelo):
    """Escribe el pedido y devuelve la ruta del archivo."""
    ahora = dt.datetime.now()
    REGISTRO.mkdir(exist_ok=True)
    ruta = REGISTRO / f"{ahora:%Y-%m-%d_%H%M%S}.json"
    pedido = {
        "fecha": ahora.isoformat(timespec="seconds"),
        "modelo": modelo,
        "formulario": formulario,
        "archivos": {
            "usados": [
                {"nombre": d.nombre, "tema": d.tema, "caracteres": len(d.texto)}
                for d in ingesta.documentos
            ],
            "rechazados": ingesta.rechazados,
            "casi_duplicados": ingesta.casi_duplicados,
        },
        "resultado": resultado,
    }
    ruta.write_text(json.dumps(pedido, ensure_ascii=False, indent=2), encoding="utf-8")
    return ruta
