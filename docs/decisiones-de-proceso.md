# Decisiones de proceso — Study Copilot

Exploraciones sobre cómo trabajar, con lo que se decidió y por qué, como insumo
para el informe final. Las decisiones sobre el producto no van acá: están en la
sección 3 de [`definicion-de-la-poc.md`](hito_3/definicion-de-la-poc.md).

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
