"""Interfaz de la PoC (Streamlit). Sin lógica de negocio: arma el formulario, llama a
pipeline.procesar() y muestra el resultado.

Uso, desde la raíz del repo:
    streamlit run poc/app.py

Streamlit vuelve a ejecutar este script en cada interacción, así que el pedido se guarda
en st.session_state: cambiar de pestaña no vuelve a llamar al modelo.

Distribución: la barra lateral tiene lo del examen y lo que se quiere generar; el cuerpo
tiene los temas (cada uno con sus archivos), las horas y el resultado.
"""

import datetime as dt
import os
import sys
from pathlib import Path

# `streamlit run poc/app.py` pone poc/ en el path, no la raíz: sin esto no se importa `poc`.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402
from dotenv import load_dotenv  # noqa: E402

from poc import config, ingesta, pipeline  # noqa: E402
from poc.formulario import tipos_pedidos  # noqa: E402

load_dotenv(config.RAIZ / ".env")

st.set_page_config(page_title="Study Copilot", page_icon=":material/school:", layout="wide")


# ------------------------------------------------------------------------ barra lateral

def barra_lateral():
    """Examen, qué generar y material general. Devuelve esos datos y los archivos generales."""
    with st.sidebar:
        st.header("Tu examen")
        materia = st.text_input("Materia", placeholder="Ej.: Álgebra")
        fecha_examen = st.date_input("Fecha del examen", value=dt.date.today() + dt.timedelta(days=7))
        objetivo = st.selectbox("Objetivo", config.OBJETIVOS)

        st.header("Qué generar")
        st.caption("Además del plan. Se genera aunque no subas ningún archivo.")
        contenido = [
            tipo
            for tipo, etiqueta in config.TIPOS_CONTENIDO.items()
            if st.checkbox(etiqueta, value=tipo in config.CONTENIDO_POR_DEFECTO, key=f"contenido_{tipo}")
        ]

        st.header("Material general")
        st.caption("Temario o parciales que abarcan varios temas. Los archivos de un tema van en su tarjeta.")
        subidos = st.file_uploader(
            "PDF o TXT",
            accept_multiple_files=True,
            key="archivos_generales",
            label_visibility="collapsed",
        )
        # Sin `type=`: así un archivo que no es PDF ni TXT llega a la ingesta y se rechaza con
        # un mensaje, en vez de que el navegador lo bloquee sin explicar.
        banco = st.selectbox(
            "Atajo para probar: material de una materia del banco del equipo",
            ["(ninguna)"] + ingesta.materias_del_banco(),
        )
        st.caption(
            "El texto de los archivos se envía a OpenAI tal cual, sin anonimizar. "
            "En esta PoC sólo corresponde usar el banco de pruebas."
        )

    general = [(a.name, a.getvalue()) for a in subidos]
    if banco != "(ninguna)":
        general += ingesta.archivos_del_banco(banco)
    return materia, fecha_examen, objetivo, contenido, general


# ------------------------------------------------------------------------------ temas

def _agregar_tema():
    st.session_state["temas_ids"].append(st.session_state["proximo_id"])
    st.session_state["proximo_id"] += 1


def _quitar_tema(id_):
    if len(st.session_state["temas_ids"]) > 1:
        st.session_state["temas_ids"].remove(id_)


def _tarjeta_tema(id_):
    with st.container(border=True):
        c_nombre, c_nivel, c_quitar = st.columns([5, 4, 1], vertical_alignment="bottom")
        nombre = c_nombre.text_input("Tema", key=f"tema_{id_}", placeholder="Ej.: Autovalores")
        nivel = c_nivel.select_slider("Mi nivel", options=list(config.NIVELES), value="medio", key=f"nivel_{id_}")
        c_quitar.button(
            "", icon=":material/delete:", key=f"quitar_{id_}", help="Quitar este tema",
            on_click=_quitar_tema, args=(id_,),
        )
        archivos = st.file_uploader(
            "Archivos de este tema (opcional)", accept_multiple_files=True, key=f"archivos_{id_}"
        )
    return nombre.strip(), nivel, [(a.name, a.getvalue()) for a in archivos]


def seccion_temas():
    """Tarjetas de temas. Devuelve ({tema: nivel}, {tema: archivos}, errores)."""
    st.subheader("Temas")
    st.caption("Poné cada tema con tu nivel y, si tenés, los archivos que lo cubren.")
    st.session_state.setdefault("temas_ids", [0, 1, 2])
    st.session_state.setdefault("proximo_id", 3)

    temas, por_tema, errores = {}, {}, []
    for id_ in list(st.session_state["temas_ids"]):
        nombre, nivel, archivos = _tarjeta_tema(id_)
        if not nombre:  # una tarjeta vacía es ruido, no un tema sin nombre
            continue
        if nombre in temas:
            errores.append(f"El tema «{nombre}» está repetido.")
        temas[nombre] = nivel
        por_tema.setdefault(nombre, []).extend(archivos)
    st.button("Agregar tema", icon=":material/add:", on_click=_agregar_tema)
    return temas, por_tema, errores


# ------------------------------------------------------------------------- disponibilidad

def _numero(x):
    """Horas como int si son enteras, para que el prompt diga «2 h» y no «2.0 h»."""
    x = float(x)
    return int(x) if x == int(x) else x


def seccion_disponibilidad(fecha_examen):
    st.subheader("Horas disponibles por día")
    horas_base = st.number_input(
        "Horas por día para rellenar la tabla", min_value=0.0, max_value=24.0, value=2.0, step=0.5
    )
    hoy = dt.date.today()
    ultimo = min(fecha_examen - dt.timedelta(days=1), hoy + dt.timedelta(days=13))
    dias = [hoy + dt.timedelta(days=i) for i in range((ultimo - hoy).days + 1)]
    base = pd.DataFrame({"fecha": dias, "horas": [horas_base] * len(dias)})
    editado = st.data_editor(
        base,
        key=f"disponibilidad_{fecha_examen}_{horas_base}",  # al cambiar fecha u horas, se rearma
        num_rows="dynamic",
        hide_index=True,
        width="stretch",
        column_config={
            "fecha": st.column_config.DateColumn("Día", format="YYYY-MM-DD"),
            "horas": st.column_config.NumberColumn("Horas", min_value=0, max_value=24, step=0.5),
        },
    )
    disponibilidad, errores = {}, []
    for _, fila in editado.iterrows():
        if pd.isna(fila["fecha"]):
            continue
        fecha = pd.to_datetime(fila["fecha"]).date().isoformat()
        if fecha in disponibilidad:
            errores.append(f"El día {fecha} está repetido.")
        disponibilidad[fecha] = 0 if pd.isna(fila["horas"]) else _numero(fila["horas"])
    return disponibilidad, errores


# ---------------------------------------------------------------------------- resultado

def _bloques(dia):
    if not isinstance(dia, dict):
        return []
    return [b for b in (dia.get("bloques") or []) if isinstance(b, dict)]


def _minutos(b):
    m = b.get("minutos")
    return m if isinstance(m, (int, float)) and not isinstance(m, bool) else 0


def _origen(o):
    """Texto que dice en qué se apoyó el contenido de un tema."""
    if o["propios"]:
        extra = f" y {o['general']} de material general" if o["general"] else ""
        return f":green[Apoyado en {o['propios']} archivo(s) de este tema{extra}]"
    if o["general"]:
        return (
            f":blue[Apoyado en el material general ({o['general']} archivo(s)); "
            "este tema no tiene archivos propios]"
        )
    return ":orange[Sin archivos: lo generó el modelo con su conocimiento general. Contrastalo con tu material]"


def mostrar_avisos_de_ingesta(ing):
    for rechazo in ing.rechazados:
        st.warning(f"Archivo rechazado: {rechazo}")
    for aviso in ing.casi_duplicados:
        st.info(aviso)
    if not ing.hay_material:
        st.info(
            "No subiste archivos legibles: el contenido se generó con el conocimiento general "
            "del modelo, sin apoyarse en tu material."
        )


def mostrar_estado(r):
    ok = r["valido"] and not r["errores_prioridad"]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Validación", "Aprobada" if ok else "Con avisos")
    c2.metric("Intentos", r["intentos"])
    c3.metric("Tiempo", f"{r['segundos']} s")
    c4.metric("Tokens", f"{r['tokens']:,}".replace(",", "."))
    if r["error_api"]:
        st.error(f"No se pudo completar la llamada al modelo: {r['error_api']}")
    if r["errores"]:
        st.warning(
            "El plan no pasó la validación y se muestra igual, para que lo revises. Errores:\n\n"
            + "\n".join(f"- {e}" for e in r["errores"])
        )
    if r["errores_prioridad"]:
        st.warning(
            "El plan no respeta la prioridad por nivel:\n\n"
            + "\n".join(f"- {e}" for e in r["errores_prioridad"])
        )
    if ok:
        st.success("El plan pasó la validación: respeta las horas, cubre todos los temas y explica cada uno.")


def mostrar_plan(respuesta, formulario):
    plan = respuesta.get("plan") if isinstance(respuesta, dict) else None
    if not isinstance(plan, list):
        st.write("El modelo no devolvió un plan que se pueda mostrar.")
        return
    for dia in plan:
        fecha = dia.get("fecha", "?") if isinstance(dia, dict) else "?"
        bloques = _bloques(dia)
        total = sum(_minutos(b) for b in bloques)
        disponibles = formulario["disponibilidad"].get(fecha)
        with st.container(border=True):
            st.markdown(f"**{fecha}**")
            if disponibles:
                st.progress(
                    min(total / (disponibles * 60), 1.0),
                    text=f"{total:g} de {disponibles * 60:g} min disponibles",
                )
            else:
                st.caption(f"{total:g} min")
            for b in bloques:
                st.markdown(f"- **{b.get('tema', '?')}** · {_minutos(b):g} min")


def mostrar_explicaciones(respuesta, formulario):
    explicaciones = respuesta.get("explicaciones") if isinstance(respuesta, dict) else None
    if not isinstance(explicaciones, dict):
        st.write("El modelo no devolvió explicaciones.")
        return
    for tema, nivel in formulario["temas"].items():
        with st.container(border=True):
            st.markdown(f"**{tema}** · nivel {nivel}")
            st.write(explicaciones.get(tema, "—"))


def mostrar_contenido(respuesta, formulario, ing, tipo):
    st.caption(
        "Borrador a revisar. Lo genera el modelo y no está verificado: contrastalo con tu material."
    )
    items = respuesta.get(tipo) if isinstance(respuesta, dict) else None
    if not isinstance(items, dict):
        st.write("El modelo no devolvió este contenido.")
        return
    origen = ingesta.origen_por_tema(formulario["temas"], ing)
    for tema in formulario["temas"]:
        lista = items.get(tema)
        if not isinstance(lista, list):
            continue
        with st.expander(f"{tema} · {len(lista)}", expanded=len(formulario["temas"]) == 1):
            st.markdown(_origen(origen[tema]))
            for i, texto in enumerate(lista, start=1):
                st.markdown(f"**{i}.** {texto}")


def mostrar_pedido(pedido):
    st.divider()
    st.subheader("Resultado")
    if pedido.errores_formulario:
        for e in pedido.errores_formulario:
            st.error(e)
        return

    r = pedido.resultado
    mostrar_avisos_de_ingesta(pedido.ingesta)
    mostrar_estado(r)

    if r["respuesta"] is not None:
        tipos = tipos_pedidos(pedido.formulario)
        pestanas = st.tabs(["Plan", "Por qué"] + [config.TIPOS_CONTENIDO[t] for t in tipos])
        with pestanas[0]:
            mostrar_plan(r["respuesta"], pedido.formulario)
        with pestanas[1]:
            mostrar_explicaciones(r["respuesta"], pedido.formulario)
        for pestana, tipo in zip(pestanas[2:], tipos):
            with pestana:
                mostrar_contenido(r["respuesta"], pedido.formulario, pedido.ingesta, tipo)

    st.caption(f"Modelo {config.modelo()}")
    if pedido.ruta_registro:
        st.caption(f"Registrado en {pedido.ruta_registro}")
    if pedido.aviso_registro:
        st.warning(pedido.aviso_registro)


# ------------------------------------------------------------------------------- main

def main():
    materia, fecha_examen, objetivo, contenido, general = barra_lateral()

    st.title("Study Copilot")
    st.caption("PoC: se ejercita con el banco de pruebas de datos/. No está pensada para usuarios finales.")

    temas, por_tema, errores_temas = seccion_temas()
    disponibilidad, errores_dias = seccion_disponibilidad(fecha_examen)
    errores_tablas = errores_temas + errores_dias

    formulario = {
        "nombre_materia": materia,
        "fecha_examen": fecha_examen.isoformat(),
        "objetivo": objetivo,
        "temas": temas,
        "disponibilidad": disponibilidad,
        "contenido": contenido,
    }

    hay_clave = bool(os.environ.get("OPENAI_API_KEY"))
    if not hay_clave:
        st.error("Falta OPENAI_API_KEY: cargala en el archivo .env de la raíz del repo y reiniciá la app.")
    for e in errores_tablas:
        st.error(e)

    pedir = st.button(
        "Generar plan",
        type="primary",
        icon=":material/auto_awesome:",
        width="stretch",
        disabled=not hay_clave or bool(errores_tablas),
    )
    if pedir:
        from openai import OpenAI

        cliente = OpenAI(timeout=config.TIMEOUT_API_SEGUNDOS)
        with st.spinner("Generando el plan..."):
            st.session_state["pedido"] = pipeline.procesar(
                cliente, formulario, general=general, por_tema=por_tema
            )

    if "pedido" in st.session_state:
        mostrar_pedido(st.session_state["pedido"])


main()
