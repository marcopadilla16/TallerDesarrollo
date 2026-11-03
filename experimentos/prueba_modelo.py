"""Prueba del modelo para el registro 3.1.1 de la definición de la PoC.

Compara, con el mismo modelo de OpenAI, dos formas de generar el plan:

- baseline: una llamada única con el formulario y el material, como haría
  el estudiante con un chatbot genérico (sólo se le pide formato JSON para
  poder verificarlo).
- workflow: reglas explícitas en el prompt, validación del plan por código
  (estructura y prioridad) y un reintento con los errores concretos.

Los formularios son sintéticos (no existe ninguno real); el material sale
del banco de pruebas en datos/. La validez se verifica por código: el plan
respeta las horas de cada día, cubre todos los temas, no inventa temas y
explica cada uno. La prioridad se mide aparte: el promedio de minutos por
nivel cumple bajo >= medio >= alto, sólo en planes que cubren todos los temas.

Configuración: copiar .env.example a .env en la raíz del repo y completar
OPENAI_API_KEY (y, opcionalmente, OPENAI_MODEL). El .env no se commitea.

Uso, desde la raíz del repo:
    python experimentos/prueba_modelo.py --listar-modelos
    python experimentos/prueba_modelo.py --modelo <id> --repeticiones 3
"""

import argparse
import datetime as dt
import json
import os
import pathlib
import statistics
import sys
import time

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DATOS = RAIZ / "datos" / "ing_sistemas"
RESULTADOS = RAIZ / "experimentos" / "resultados"

MAX_CARACTERES_MATERIAL = 30_000
REPASO = "Repaso general"
ORDEN_NIVEL = {"bajo": 0, "medio": 1, "alto": 2}
ORDEN_CARPETA = {"temario": 0, "examenes": 1, "practicas": 2}

# Sintéticos, declarados. Uno por materia del banco: con temario (Gestión de
# Datos), sin temario (Investigación Operativa) y uno con pocas horas para
# muchos temas (Redes).
FORMULARIOS = [
    {
        "id": "gd-con-temario",
        "materia": "gestion_de_datos",
        "nombre_materia": "Gestión de Datos",
        "temas": {
            "Modelo entidad-relación": "alto",
            "Modelo relacional y restricciones": "medio",
            "SQL: consultas y subconsultas": "bajo",
            "Normalización": "bajo",
            "Transacciones y concurrencia": "medio",
        },
        "fecha_examen": "2026-11-16",
        "disponibilidad": {
            "2026-11-09": 2, "2026-11-10": 3, "2026-11-11": 1,
            "2026-11-12": 2, "2026-11-13": 0, "2026-11-14": 4,
            "2026-11-15": 3,
        },
        "objetivo": "aprobar",
    },
    {
        "id": "io-sin-temario",
        "materia": "investigacion_operativa",
        "nombre_materia": "Investigación Operativa",
        "temas": {
            "Programación lineal: modelado": "medio",
            "Método simplex": "bajo",
            "Dualidad y análisis de sensibilidad": "bajo",
            "Problemas de transporte y asignación": "alto",
        },
        "fecha_examen": "2026-11-14",
        "disponibilidad": {
            "2026-11-09": 3, "2026-11-10": 2, "2026-11-11": 3,
            "2026-11-12": 1, "2026-11-13": 2,
        },
        "objetivo": "sacar más de 8",
    },
    {
        "id": "redes-ajustado",
        "materia": "redes",
        "nombre_materia": "Redes de Información",
        "temas": {
            "Modelo OSI y TCP/IP": "alto",
            "Direccionamiento IP y subredes": "bajo",
            "Enrutamiento": "bajo",
            "Capa de transporte: TCP y UDP": "medio",
            "Capa de enlace y Ethernet": "medio",
            "DNS y HTTP": "alto",
        },
        "fecha_examen": "2026-11-12",
        "disponibilidad": {"2026-11-09": 2, "2026-11-10": 1, "2026-11-11": 2},
        "objetivo": "preparar final",
    },
]

FORMATO = (
    '{"plan": [{"fecha": "AAAA-MM-DD", "bloques": [{"tema": "...", '
    '"minutos": 60}]}], "explicaciones": {"<tema>": "por qué se le dio ese tiempo"}}'
)

REGLAS_WORKFLOW = f"""Sos un asistente que arma planes de estudio. Reglas obligatorias:
1. Usá sólo las fechas de la disponibilidad, y en cada fecha no superes las horas
   disponibles (horas x 60 minutos). Una fecha con 0 horas no lleva bloques.
2. Cada tema del formulario tiene al menos un bloque. No agregues temas, salvo
   "{REPASO}".
3. Los temas de nivel bajo reciben más minutos que los de nivel medio, y estos
   más que los de nivel alto. El objetivo ajusta cuánto profundizar.
4. Si alcanza el tiempo, reservá un bloque de "{REPASO}" en la última fecha.
5. En "explicaciones" va una entrada por cada tema del formulario, con el
   motivo en una oración que mencione su nivel.
Respondé sólo con JSON, con esta forma: {FORMATO}"""


def leer_material(materia):
    """Texto de los archivos de una materia del banco, y avisos de ingesta.

    El temario va primero: si el material supera el límite, lo que se recorta
    son parciales y prácticas, no el temario.
    """
    import pypdf

    archivos = sorted(
        (a for a in (DATOS / materia).rglob("*") if a.is_file()),
        key=lambda a: (ORDEN_CARPETA.get(a.parent.name, len(ORDEN_CARPETA)), a.as_posix()),
    )
    textos, avisos = [], []
    for archivo in archivos:
        nombre = archivo.relative_to(DATOS).as_posix()
        try:
            if archivo.suffix == ".pdf":
                lector = pypdf.PdfReader(archivo)
                texto = "\n".join(p.extract_text() or "" for p in lector.pages)
            elif archivo.suffix == ".txt":
                texto = archivo.read_text(encoding="utf-8", errors="replace")
            else:
                continue
        except Exception as e:
            avisos.append(f"{nombre}: no se pudo leer ({type(e).__name__})")
            continue
        if not texto.strip():
            avisos.append(f"{nombre}: sin texto")
            continue
        textos.append((nombre, f"### {nombre}\n{texto.strip()}"))

    material = ""
    for nombre, texto in textos:
        disponible = MAX_CARACTERES_MATERIAL - len(material)
        if disponible <= 0:
            avisos.append(f"{nombre}: afuera por el límite de {MAX_CARACTERES_MATERIAL} caracteres")
            continue
        if len(texto) > disponible:
            avisos.append(f"{nombre}: recortado a {disponible} de {len(texto)} caracteres")
        material += texto[:disponible] + "\n\n"
    return material.strip(), avisos


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


def mensajes_baseline(f, material):
    pedido = (
        "Soy estudiante y tengo que preparar un examen. Armame un plan de estudio.\n\n"
        f"{formulario_en_texto(f)}\n\nMaterial de la cursada:\n{material}\n\n"
        f"Respondé sólo con JSON, con esta forma: {FORMATO}"
    )
    return [{"role": "user", "content": pedido}]


def mensajes_workflow(f, material):
    pedido = f"{formulario_en_texto(f)}\n\nMaterial de la cursada:\n{material}"
    return [
        {"role": "system", "content": REGLAS_WORKFLOW},
        {"role": "user", "content": pedido},
    ]


def minutos_validos(minutos):
    return not isinstance(minutos, bool) and isinstance(minutos, (int, float)) and minutos > 0


def validar(respuesta, f):
    """Errores estructurales del plan; lista vacía si es válido."""
    if not isinstance(respuesta, dict) or not isinstance(respuesta.get("plan"), list):
        return ["la respuesta no tiene la lista 'plan'"]
    explicaciones = respuesta.get("explicaciones")
    if not isinstance(explicaciones, dict):
        explicaciones = {}

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
    return errores


def errores_prioridad(respuesta, f):
    """Errores de prioridad: el promedio de minutos por nivel cumple bajo >= medio >= alto.

    Devuelve None si no se puede medir: plan ilegible, o algún tema del
    formulario sin minutos (por ejemplo, porque el modelo lo renombró). Sin
    esa condición, un plan con los temas renombrados tiene todo en cero y
    pasaría por coherente.
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


def coherente(prioridad):
    return None if prioridad is None else not prioridad


def llamar(cliente, modelo, mensajes):
    inicio = time.perf_counter()
    r = cliente.chat.completions.create(
        model=modelo,
        messages=mensajes,
        response_format={"type": "json_object"},
    )
    segundos = time.perf_counter() - inicio
    tokens = r.usage.total_tokens if r.usage else None
    return r.choices[0].message.content, segundos, tokens


def parsear(texto):
    try:
        return json.loads(texto)
    except (json.JSONDecodeError, TypeError):
        return None


def intentar(cliente, modelo, mensajes, f):
    """Una llamada validada: (texto, respuesta, errores, segundos, tokens).

    Un error transitorio de la API (límite de uso, timeout, pedido rechazado)
    queda como error del intento. Uno que se repetiría en todas las corridas
    (clave inválida, modelo inexistente o sin permiso) corta la prueba.
    """
    import openai

    try:
        texto, segundos, tokens = llamar(cliente, modelo, mensajes)
    except (openai.AuthenticationError, openai.PermissionDeniedError, openai.NotFoundError):
        raise
    except openai.APIError as e:
        return None, None, [f"error de la API: {type(e).__name__}: {e}"], 0.0, None
    respuesta = parsear(texto)
    errores = validar(respuesta, f) if respuesta is not None else ["JSON inválido"]
    return texto, respuesta, errores, segundos, tokens


def correr(cliente, modelo, variante, f, material):
    mensajes = (mensajes_baseline if variante == "baseline" else mensajes_workflow)(f, material)
    texto, respuesta, errores, segundos, tokens = intentar(cliente, modelo, mensajes, f)
    prioridad = errores_prioridad(respuesta, f)
    valido_primer_intento = not errores
    coherente_primer_intento = coherente(prioridad)
    intentos = 1

    # El workflow corrige errores estructurales y de prioridad. El reintento
    # sólo tiene sentido si hubo una respuesta que corregir.
    a_corregir = errores + (prioridad or [])
    if variante == "workflow" and a_corregir and texto is not None:
        mensajes = mensajes + [
            {"role": "assistant", "content": texto},
            {"role": "user", "content": "El plan tiene estos errores:\n- " + "\n- ".join(a_corregir)
             + "\nCorregilo y devolvé el JSON completo."},
        ]
        texto2, respuesta, errores, seg2, tok2 = intentar(cliente, modelo, mensajes, f)
        prioridad = errores_prioridad(respuesta, f)
        texto = texto2 if texto2 is not None else texto
        segundos += seg2
        tokens = (tokens or 0) + (tok2 or 0)
        intentos = 2

    return {
        "formulario": f["id"],
        "variante": variante,
        "valido": not errores,
        "valido_primer_intento": valido_primer_intento,
        "errores": errores,
        "errores_prioridad": prioridad,
        "prioridad_coherente": coherente(prioridad),
        "prioridad_coherente_primer_intento": coherente_primer_intento,
        "intentos": intentos,
        "segundos": round(segundos, 1),
        "tokens": tokens,
        "respuesta": respuesta if respuesta is not None else texto,
    }


def resumen(filas):
    """Tabla de resultados. La prioridad se cuenta sobre los planes donde se puede medir."""

    def de_medibles(grupo, clave):
        medibles = [r[clave] for r in grupo if r[clave] is not None]
        return f"{sum(medibles)} de {len(medibles)}"

    lineas = [
        "| Variante | Planes válidos | Válidos al 1.er intento | Prioridad coherente "
        "| Prioridad al 1.er intento | Errores de API | Segundos (media) | Tokens (media) |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for variante in ("baseline", "workflow"):
        grupo = [r for r in filas if r["variante"] == variante]
        if not grupo:
            continue
        n = len(grupo)
        validos = sum(r["valido"] for r in grupo)
        primer = sum(r["valido_primer_intento"] for r in grupo)
        api = sum(any(e.startswith("error de la API") for e in r["errores"]) for r in grupo)
        seg = statistics.mean(r["segundos"] for r in grupo)
        tok = statistics.mean(r["tokens"] or 0 for r in grupo)
        lineas.append(
            f"| {variante} | {validos} de {n} | {primer} de {n} "
            f"| {de_medibles(grupo, 'prioridad_coherente')} "
            f"| {de_medibles(grupo, 'prioridad_coherente_primer_intento')} "
            f"| {api} | {seg:.1f} | {tok:.0f} |"
        )
    return "\n".join(lineas)


def main():
    from dotenv import load_dotenv

    # Las variables ya definidas en el entorno tienen prioridad sobre el .env.
    load_dotenv(RAIZ / ".env")

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--modelo", default=os.environ.get("OPENAI_MODEL"))
    parser.add_argument("--repeticiones", type=int, default=3)
    parser.add_argument("--listar-modelos", action="store_true")
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("Falta OPENAI_API_KEY: cargala en el archivo .env de la raíz del repo.")

    from openai import OpenAI

    cliente = OpenAI()
    if args.listar_modelos:
        for m in sorted(m.id for m in cliente.models.list()):
            print(m)
        return
    if not args.modelo:
        sys.exit("Indicá el modelo con --modelo o con OPENAI_MODEL (ver --listar-modelos).")

    RESULTADOS.mkdir(parents=True, exist_ok=True)
    marca = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    # El modelo va en el nombre para poder correr varios modelos en paralelo.
    salida = RESULTADOS / f"prueba_modelo_{marca}_{args.modelo}.json"

    def guardar(filas, ingesta):
        # Se reescribe después de cada corrida: si la prueba se corta, lo hecho queda.
        datos = {
            "fecha": marca,
            "modelo": args.modelo,
            "repeticiones": args.repeticiones,
            "max_caracteres_material": MAX_CARACTERES_MATERIAL,
            "ingesta": ingesta,
            "resumen": resumen(filas),
            "corridas": filas,
        }
        salida.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")

    filas, ingesta = [], {}
    for f in FORMULARIOS:
        material, avisos = leer_material(f["materia"])
        ingesta[f["materia"]] = {"caracteres": len(material), "avisos": avisos}
        for aviso in avisos:
            print(f"[ingesta] {aviso}")
        for rep in range(1, args.repeticiones + 1):
            for variante in ("baseline", "workflow"):
                fila = correr(cliente, args.modelo, variante, f, material)
                fila["repeticion"] = rep
                filas.append(fila)
                guardar(filas, ingesta)
                estado = "válido" if fila["valido"] else f"{len(fila['errores'])} errores"
                print(f"{f['id']} #{rep} {variante}: {estado} ({fila['segundos']} s)")

    print("\n" + resumen(filas))
    print(f"\nResultados en {salida.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
