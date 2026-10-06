# Mapa de fuentes — Study Copilot

> **Equipo:** …
> **Integrantes:** Padilla, Marco; Sanches, Federico
> **Caso:** Study Copilot
> **Versión:** 3 · **Fecha:** 06/10/2026

## Cómo se lee

Este mapa adapta la plantilla de compartida en clases, a la
hipótesis de datos de `Study Copilot`.
Es un relevamiento inicial: lo que no fue abierto o inspeccionado se marca como pendiente, no como disponible o verificado.

**El dato del que más depende el proyecto:** datos ingresados por el estudiante
(materia, temas, fecha de examen, nivel autoevaluado por tema, tiempo disponible
y objetivo). El Canvas identifica este formulario como el dato del que más
depende el producto. Para comprobar si el plan resulta útil también hará falta
recolectar feedback de uso y, si se evalúa, resultados académicos.

## 1. Las fuentes

| # | Fuente | Familia | ¿Está disponible hoy? (quién la abrió) | ¿Qué tan complejo es obtenerla? (tiempo, esfuerzo, dinero) | ¿Es sensible, tiene dueño? (términos de uso, licencia) | Volumen estimado |
|---|---|---|---|---|---|---|
| 1 | Respuestas a la encuesta y entrevistas exploratorias sobre hábitos, tiempo de planificación, incertidumbre y priorización | Los ingresa el usuario (participantes) | No hay respuestas recolectadas ni muestra inspeccionada; relevamiento propuesto en el Canvas | Bajo/medio: preparar instrumento, convocar participantes y analizar respuestas; sin costo monetario conocido | Puede incluir opiniones y experiencias personales. Requiere informar propósito y participación voluntaria; definir resguardo antes de recolectar | Encuesta: 10-20 estudiantes; entrevistas: 6-8, según el mínimo viable del Canvas |
| 2 | Formulario de uso: materia, temas, fecha, nivel por tema, disponibilidad y objetivo | Los ingresa el usuario | No existe una muestra del producto; se generaría cuando estudiantes usen la PoC | Medio: diseñar formulario y recolectar datos durante una prueba | Datos académicos personales; el estudiante los provee. Definir consentimiento, acceso, retención y eliminación | Una respuesta por plan generado; volumen desconocido hasta probar |
| 3 | Plan generado y registro de uso (ediciones, regeneraciones, sesiones realizadas) | Los genera el sistema | No existe todavía una muestra de uso; depende de implementar e instrumentar la PoC | Medio: instrumentar la PoC y acordar qué eventos guardar | Puede revelar temas que le cuestan al estudiante y hábitos de estudio. El equipo debe limitar los datos y restringir el acceso | Un registro por plan y eventos asociados; volumen desconocido |
| 4 | Programas, temarios y contenidos de cátedras | De terceros | El Canvas indica acceso parcial, pero la tabla de datos marca «¿Lo vimos? = No»; falta abrir y revisar fuentes concretas | Medio: localizar fuentes por cátedra, comprobar vigencia y extraer los temas; costo monetario no conocido | Depende de cada sitio y material. Revisar licencias y condiciones de uso antes de copiar o redistribuir | Desconocido; depende de las materias/cátedras seleccionadas |
| 5 | Parciales y finales anteriores | De terceros | El Canvas indica acceso parcial, pero no registra una muestra inspeccionada | Medio/alto: buscar en cátedras o repositorios y verificar pertinencia y permisos | Pueden tener datos personales escritos en las copias y estar sujetos a derechos de autor o restricciones de distribución | Desconocido; depende de las materias, años y exámenes disponibles |
| 6 | Feedback posterior: utilidad del plan, adherencia y, si se decide medirlo, resultado del examen | Los ingresa el usuario (participantes) | No recolectado; sólo existiría luego de una prueba de uso y seguimiento | Medio/alto: requiere contactar participantes después de usar el plan y obtener respuestas voluntarias | Sensible: adherencia, percepción de dificultades y notas/resultados académicos. No solicitar notas si no son necesarias; definir consentimiento y resguardo | Una respuesta por participante/plan; seguimiento y tasa de respuesta desconocidos |
| 7 | Conocimiento y respuestas del modelo LLM usado para planes y materiales | De terceros | El Canvas no identifica proveedor/modelo ni registra inspección de una muestra; disponibilidad y condiciones por verificar | Medio: depende del proveedor, acceso al servicio, pruebas por materia y posibles costos de API | Revisar términos del proveedor, uso de prompts/datos y tratamiento de información enviada. Evitar cargar datos identificables de estudiantes | Desconocido; dependerá del número de pruebas/planes y límites del servicio |
| 8 | Casos sintéticos de entradas, planes y fallas para probar instrumentos, métricas y mitigaciones | Sintéticos | No creados todavía; los produciría el equipo, sin muestra empírica inspeccionada | Bajo/medio: definir escenarios, etiquetarlos y revisar que cubran casos límite | No deben incluir datos reales ni presentarse como evidencia sobre estudiantes; autoría del equipo | A definir según los casos límite y validadores que se quieran probar |

## 2. Los riesgos

| # | Completitud (qué puede faltar y por qué) | Exactitud (errores, formato, duplicados) | Actualidad (período que cubre) | Representatividad (a quién deja afuera) | Confiabilidad de las etiquetas (quién etiquetó y con qué criterio) |
|---|---|---|---|---|---|
| 1 | Puede faltar la experiencia de quienes no respondan o abandonen la encuesta | Recuerdo impreciso del tiempo y respuestas influenciadas por cómo se formule la pregunta | Describe hábitos del período consultado; no necesariamente los de otras épocas del año | Muestra de conveniencia puede concentrarse en compañeros, carreras o niveles similares | El equipo clasifica respuestas; acordar categorías y conservar las respuestas originales anonimizadas |
| 2 | El estudiante puede omitir temas, restricciones o disponibilidad | Nivel autoevaluado es subjetivo; fechas y horas pueden ingresarse mal | Refleja la situación declarada al crear cada plan; puede cambiar luego | Usuarios de la PoC no representan necesariamente a todos los estudiantes | Nivel y objetivo los declara el propio estudiante; son percepciones, no mediciones objetivas |
| 3 | El registro puede no capturar estudio fuera de la PoC o sesiones completadas sin marcar | Eventos perdidos, duplicados o acciones mal interpretadas | Se genera durante el uso; la cobertura depende del período de prueba | Sólo representa a usuarios que acepten probar la PoC y tengan acceso a ella | «Sesión realizada» debe definirse; los eventos del sistema no prueban por sí solos que hubo estudio efectivo |
| 4 | Puede faltar bibliografía, temas o ponderación de evaluación | Temarios desactualizados o diferencias entre documento y cursada real | Puede no corresponder al ciclo lectivo vigente | Las fuentes publicadas pueden cubrir sólo algunas cátedras o carreras | Las etiquetas de tema/peso las define la cátedra o el equipo; registrar origen y criterio |
| 5 | Puede haber pocos exámenes o faltar años/temas | Escaneos ilegibles, soluciones incorrectas, duplicados o versiones incompletas | Exámenes viejos pueden no reflejar el programa ni el estilo actual | Lo compartido por estudiantes puede favorecer ciertas materias y cohortes | «Tema frecuente» requiere criterio y muestra; no asumir que frecuencia histórica predice el próximo examen |
| 6 | Puede faltar respuesta de quienes no siguieron el plan o tuvieron una mala experiencia | Autorreporte y recuerdo pueden ser inexactos; las notas pueden confundirse con otros resultados | Debe recogerse después de cada uso/examen; el retraso afecta el recuerdo | Puede responder más quien quedó satisfecho; quienes abandonan pueden quedar fuera | «Útil», «adherencia» y «resultado» necesitan definiciones; el resultado no demuestra causalidad del plan |
| 7 | El modelo puede desconocer temas de nicho o contenidos específicos de una cátedra | Puede generar errores o afirmaciones plausibles pero falsas | El conocimiento puede estar desactualizado; depende del modelo/proveedor | Calidad variable por idioma, disciplina y representación en los datos de entrenamiento | Las respuestas no vienen necesariamente etiquetadas como correctas; requieren revisión con material de la cátedra |
| 8 | Los casos podrían no cubrir fallas relevantes o combinar pocos factores | El equipo puede etiquetar como «esperable» un caso discutible | Representa supuestos actuales, no cambios reales en cursos o modelos | No modela diversidad real de estudiantes salvo que se diseñe expresamente | Las etiquetas las asigna el equipo; documentar reglas y separar casos de prueba de evidencia empírica |

## 3. El plan de obtención

Las personas responsables y fechas exactas quedan **por asignar entre Marco P. y
Fede S. durante la clase**; no se presuponen tareas ya aceptadas. Prioridad
sugerida: empezar por el dato principal (fuente 2) y el mínimo viable de
validación del problema (fuente 1).

| # | Quién del equipo la consigue | Para cuándo |
|---|---|---|
| 1 | Por asignar entre Marco P. y Fede S.: preparar y aplicar encuesta/entrevistas con participación voluntaria | A definir en clase según el calendario del trimestre |
| 2 | Por asignar entre Marco P. y Fede S.: definir campos mínimos del formulario y probarlo con la PoC | A definir en clase; antes de la primera prueba de uso |
| 3 | Por asignar entre Marco P. y Fede S.: especificar eventos mínimos y registro de sesiones | A definir en clase; antes de la primera prueba de uso |
| 4 | Por asignar entre Marco P. y Fede S.: localizar y abrir al menos un temario vigente de una materia elegida | A definir en clase |
| 5 | Por asignar entre Marco P. y Fede S.: localizar y revisar permisos de una muestra de exámenes de esa materia | A definir en clase |
| 6 | Por asignar entre Marco P. y Fede S.: preparar preguntas de seguimiento y decidir si realmente hace falta recolectar notas | Después de la prueba de uso; fecha a definir |
| 7 | Por asignar entre Marco P. y Fede S.: identificar proveedor/modelo, revisar términos y probar respuestas con material verificable | Antes de integrar el servicio; fecha a definir |
| 8 | Por asignar entre Marco P. y Fede S.: diseñar y etiquetar casos límite sintéticos para probar métricas y mitigaciones | Si no hay muestra real suficiente o para probar validadores; fecha a definir |

**Límite de interpretación:** los datos sintéticos sirven para probar instrumentos,
validadores y escenarios; no permiten afirmar que los hábitos, riesgos o
resultados observados describan a estudiantes reales. Las fuentes aún no
inspeccionadas deben abrirse y revisarse antes de cambiar su estado a disponible.
