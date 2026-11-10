"""Los seis pasos del workflow, en orden (3.1.3). La interfaz sólo llama a procesar().

    1. validar el formulario   4. validar el JSON      (poc/generador.py)
    2. ingerir los archivos    5. reintento
    3. generar con el modelo   6. registrar y mostrar
"""

from dataclasses import dataclass, field

from poc import config, generador, ingesta, registro
from poc.formulario import validar_formulario


@dataclass
class Pedido:
    formulario: dict
    errores_formulario: list = field(default_factory=list)
    ingesta: ingesta.Ingesta = None
    resultado: dict = None
    ruta_registro: str = None
    aviso_registro: str = None


def procesar(cliente, formulario, general=(), por_tema=None, modelo=None):
    """general: archivos de la materia; por_tema: {tema: archivos}. Todos como (nombre, bytes)."""
    pedido = Pedido(formulario)
    pedido.errores_formulario = validar_formulario(formulario)
    if pedido.errores_formulario:
        return pedido

    modelo = modelo or config.modelo()
    pedido.ingesta = ingesta.ingerir(general, por_tema)
    pedido.resultado = generador.generar(cliente, modelo, formulario, pedido.ingesta)

    try:
        pedido.ruta_registro = str(registro.guardar(formulario, pedido.ingesta, pedido.resultado, modelo))
    except OSError as e:  # no poder registrar no tiene que tirar el plan que ya se generó
        pedido.aviso_registro = f"No se pudo guardar el registro: {e}"
    return pedido
