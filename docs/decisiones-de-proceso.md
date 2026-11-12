# Decisiones de proceso — Study Copilot

Exploraciones sobre cómo trabajar, con lo que se decidió y por qué, como insumo
para el informe final. Las decisiones sobre el producto no van acá: están en la
sección 3 de [`definicion-de-la-poc.md`](hito_3/definicion-de-la-poc.md).

## Correcciones del Hito 2, subidas como parte del Hito 3

**Fecha:** 2026-11-03 · **Estado:** aplicada

**Decisión.** Los errores de hecho de los documentos del Hito 2 se corrigen en esos
documentos, subiendo su versión, y se suben como commits del Hito 3, sin tags nuevos.
Las decisiones de aquel momento no se reescriben.

**Qué se corrigió.**

- **Cifras que no se reproducían.** Al correr el notebook daba 170.810 caracteres y 58%
  de compilaciones de estudiantes, contra los 158.120 y 55% citados. La causa es la
  versión de `pypdf`, que no estaba fijada y cambia cuántos espacios y saltos de línea
  extrae: las versiones probadas dieron entre 158.120 y 171.458 caracteres, y sin contar
  esos espacios, entre 137.095 y 137.291. `pypdf==6.15.0` reproduce exactamente las
  cifras de los documentos, así que se fijó esa versión en `requirements.txt` y las
  cifras no cambiaron.
- **Notebook.** Sus textos seguían comparando contra el nivel original. Ahora cada celda
  aclara si compara contra el nivel original o el vigente, y mide lo que el EDA le
  atribuye y no calculaba: los orígenes del banco y el total por tipo de documento. Se
  corrigió también la conclusión sobre la partición, que contradecía al EDA.
- **EDA.** Se quitó la referencia a una "advertencia metodológica" que no existe.
- **Mapa de fuentes y encabezados.** Se completaron el equipo y los responsables.

**Lo que se dejó como está.** Un error de tipeo en el datasheet ("resuúmenes"), a
propósito.

**Segunda tanda (2026-11-11).** El notebook y los documentos del Hito 1 se movieron a
`docs/hito_1/`, `docs/hito_2/` y `docs/` (commit `829e7fd`), y eso rompió dos cosas:

- **El notebook no corría.** Leía `datos/` con una ruta relativa, y Jupyter lo ejecuta
  desde su propia carpeta. Ahora busca `datos/` subiendo desde donde se ejecuta. Se
  corrió desde `docs/hito_2/` con `pypdf==6.15.0`, y las cifras citadas se reproducen
  sin cambios.
- **EDA (v5).** La ruta del notebook en el encabezado.

**Tercera tanda (2026-11-12).** Una revisión de coherencia de todo el repo encontró
cuatro errores de hecho:

- **Datasheet (v4).** Decía «6 de 14 archivos sin fecha en metadatos»: la celda 3
  da 6 *con* fecha, así que son 8 sin. Los 6 de 14 son los archivos sin fecha
  *determinable* (celda 5), que es otra cifra.
- **EDA (v6).** La fila de confiabilidad decía «Nombres de persona en metadatos:
  5 de 14», y el mismo EDA dice más abajo que son 2. Los 5 son archivos con campo
  de autor (celda 7), y 2 de ellos tienen nombre de persona.
- **Veredicto (v5).** Atribuía los formatos y los orígenes a las celdas 2 y 3;
  salen de la celda 6.
- **Mapa de fuentes (v6).** En las secciones 3 y 4, la fila 7 hablaba de los
  sintéticos, que en la sección 1 son la fuente 8, y el LLM (fuente 7) no tenía
  fila. Se agregó la fila del LLM con lo que se sabía al entregar el Hito 2.

## Extensión de la definición de la PoC por encima del tope de la plantilla

**Fecha:** 2026-11-12 · **Momento del proyecto:** Hito 3, antes del tag ·
**Estado:** aplicada

**Qué se decidió.** Recortar `docs/hito_3/definicion-de-la-poc.md` a unas 4.600
palabras, y no a las 3.000 que fija la plantilla de la cátedra
(`docs/hito_3/plantilla/`, "Extensión").

**Por qué.** Con las cuatro partes escritas, el documento tenía unas 7.500
palabras. Llegar a 3.000 obligaba a elegir entre dos cosas que el equipo no
quiso resignar:

- **Borrar lo superado.** La regla del repo (CLAUDE.md) es marcarlo como
  suspendido y conservarlo, porque el historial también se evalúa.
- **Sacar las alternativas descartadas y sus motivos.** El criterio de diseño
  del enunciado pide que cada registro evalúe al menos dos alternativas y diga
  por qué se descartó cada una.

**Cómo se recortó.** Se quitaron las repeticiones entre secciones (por ejemplo,
el *baseline* se describía en 3.1.1, 3.1.3, 2.3 y 3.2) y se acortó la prosa.
Se conservan todas las decisiones, las cifras, las referencias a celdas, las
alternativas y los textos suspendidos, con su cita textual. El conteo incluye
el historial, las tablas y el diagrama.

**Alternativas descartadas.**

- *Llegar a 3.000 moviendo el historial y los textos suspendidos a un anexo.*
  Cumplía el tope sin perder nada, pero dejaba el documento entregado sin el
  rastro de lo que cambió.

**Pendiente.** Preguntarle al docente si el tope es estricto o si cuenta las
tablas. No es una alternativa descartada: si responde que es estricto, la
opción del anexo es la salida.

**Qué se resigna.** Incumplir una indicación explícita de la plantilla, a
sabiendas.

## OpenSpec y Spec Kit para el desarrollo guiado por especificaciones

**Fecha:** 2026-11-03 · **Momento del proyecto:** Hito 3 en curso, sin código del
producto · **Estado:** descartadas para el Hito 3; OpenSpec se puede reevaluar al
empezar a construir

**Qué se exploró.** Si convenía adoptar una herramienta de desarrollo guiado por
especificaciones. El motivo: la solución de referencia del docente organiza el
detalle de su definición de la PoC con OpenSpec (`proposal.md`, `specs/`,
`design.md` y `tasks.md`, en `openspec/changes/<change>/`).

**Cómo se evaluó.** Por análisis: se compararon las herramientas con el enunciado
y con el estado del proyecto. No se instalaron ni se probaron, y tampoco se
revisaron sus versiones vigentes.

**Por qué se descartaron.**

1. **No son un requisito.** El enunciado del Hito 3 pide un solo documento, y sus
   criterios de evaluación no mencionan ninguna herramienta.
2. **No resuelven lo que falta.** Lo pendiente del Hito 3 son decisiones
   (escenarios, criterios de aceptación, registros de diseño), y ninguna
   herramienta las toma por el equipo.
3. **Duplican la fuente de verdad.** El documento del hito es el contrato. Tener
   el mismo contenido en dos lugares invita a que se contradigan, como ya pasó
   entre el canvas y el veredicto del Hito 2.
4. **Es temprano.** Su valor está en guiar la implementación y seguir los cambios,
   y todavía no hay código.
5. **Spec Kit, además, es excesivo para este equipo.** Suma un proceso propio por
   etapas y más artefactos que mantener, para dos personas y tres semanas. OpenSpec
   encaja mejor, porque las cuatro partes del documento se corresponden con sus
   cuatro archivos.

**Qué se resigna.** Especificaciones y tareas acotadas por cambio, que serían útiles
para programar con un agente de IA, y la estructura de trabajo que usa la solución
de referencia.

**Qué haría cambiar la decisión.**

- Que el docente espere OpenSpec para la construcción o para el Hito 4. Todavía no
  se le preguntó.
- Que, al programar con un agente, el plan de la sección 4.1 no alcance para
  acotarle el trabajo. En ese caso se pasarían a OpenSpec sólo la spec y las tareas
  de lo que se construye, y el documento seguiría siendo el contrato.
