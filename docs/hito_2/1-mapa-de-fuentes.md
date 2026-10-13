# Mapa de fuentes — Study Copilot

> **Equipo:** …
> **Integrantes:** Padilla, Marco; Sanches, Federico
> **Caso:** Study Copilot
> **Versión:** 4 · **Fecha:** 11/10/2026

## 1. Las fuentes

| # | Fuente | Familia | ¿Está disponible hoy? (quién la abrió) | ¿Qué tan complejo es obtenerla? (tiempo, esfuerzo, dinero) | ¿Es sensible, tiene dueño? (términos de uso, licencia) | Volumen estimado |
|---|---|---|---|---|---|---|
| 1 | Respuestas a la encuesta y entrevistas exploratorias sobre hábitos, tiempo de planificación, incertidumbre y priorización | Los ingresa el usuario (participantes) | No hay respuestas recolectadas ni muestra inspeccionada; relevamiento propuesto en el Canvas | Bajo/medio: preparar instrumento, convocar participantes y analizar respuestas; sin costo monetario conocido | Puede incluir opiniones y experiencias personales. Requiere informar propósito y participación voluntaria; definir resguardo antes de recolectar | Encuesta: 10-20 estudiantes; entrevistas: 6-8, según el mínimo viable del Canvas |
| 2 | Formulario de uso: materia, temas, fecha, nivel por tema, disponibilidad y objetivo | Los ingresa el usuario | No existe una muestra del producto; se generaría cuando estudiantes usen la PoC | Medio: diseñar formulario y recolectar datos durante una prueba | Datos académicos personales; el estudiante los provee. Definir consentimiento, acceso, retención y eliminación | Una respuesta por plan generado; volumen desconocido hasta probar |
| 3 | Plan generado y registro de uso (ediciones, regeneraciones, sesiones realizadas) | Los genera el sistema | No existe todavía una muestra de uso; depende de implementar e instrumentar la PoC | Medio: instrumentar la PoC y acordar qué eventos guardar | Puede revelar temas que le cuestan al estudiante y hábitos de estudio. El equipo debe limitar los datos y restringir el acceso | Un registro por plan y eventos asociados; volumen desconocido |
| 4 | Temario de la materia | Lo ingresa el usuario (en producción). De terceros, sólo en el banco de pruebas | Sí, como banco de pruebas. | En producción: ninguno para el equipo, lo aporta el usuario. Para el banco de pruebas fue bajo | En producción el usuario sube material del que puede no tener derechos. | 1 archivo en el banco; en producción, 1 por materia que el usuario cargue |
| 5 | Parciales, finales y guías de práctica de la materia | Lo ingresa el usuario (en producción). De terceros, sólo en el banco de pruebas | Sí, como banco de pruebas; 7 exámenes y 6 guías de 3 materias, 90 páginas, 147.843 caracteres | En producción: ninguno para el equipo. Para el banco fue medio: se bajaron de repositorios estudiantiles sin contactar cátedras | Sin licencia declarada en los 13. 2 archivos exponen nombre real de persona en metadatos. 4 son compilaciones de estudiantes, no material oficial | 13 archivos en el banco; en producción, lo que suba cada usuario |
| 6 | Feedback posterior: utilidad del plan, adherencia y, si se decide medirlo, resultado del examen | Los ingresa el usuario (participantes) | No recolectado; sólo existiría luego de una prueba de uso y seguimiento | Medio/alto: requiere contactar participantes después de usar el plan y obtener respuestas voluntarias | Sensible: adherencia, percepción de dificultades y notas/resultados académicos. No solicitar notas si no son necesarias; definir consentimiento y resguardo | Una respuesta por participante/plan; seguimiento y tasa de respuesta desconocidos |
| 7 | Conocimiento y respuestas del modelo LLM usado para planes y materiales | De terceros | Proveedor acotado a dos candidatos: ChatGPT (OpenAI) o Claude (Anthropic). Falta elegir cuál, fijar la versión del modelo y probar respuestas contra el material de `datos/`; no se inspeccionó ninguna salida todavía | Medio: ambos ofrecen API de pago por uso. Falta estimar costo por plan generado y probar cobertura por materia | Verificar qué hace cada proveedor con los prompts, si se usan para entrenamiento y si se puede desactivar. No cargar datos identificables de estudiantes | Desconocido; dependerá del número de pruebas/planes y límites del servicio |
| 8 | Casos sintéticos de entradas, planes y fallas para probar instrumentos, métricas y mitigaciones | Sintéticos | No creados todavía; los produciría el equipo, sin muestra empírica inspeccionada | Bajo/medio: definir escenarios, etiquetarlos y revisar que cubran casos límite | No deben incluir datos reales ni presentarse como evidencia sobre estudiantes; autoría del equipo | A definir según los casos límite y validadores que se quieran probar |

## 2. Los riesgos

| # | Completitud (qué puede faltar y por qué) | Exactitud (errores, formato, duplicados) | Actualidad (período que cubre) | Representatividad (a quién deja afuera) | Confiabilidad de las etiquetas (quién etiquetó y con qué criterio) |
|---|---|---|---|---|---|
| 1 | Puede faltar la experiencia de quienes no respondan o abandonen la encuesta | Recuerdo impreciso del tiempo y respuestas influenciadas por cómo se formule la pregunta | Describe hábitos del período consultado; no necesariamente los de otras épocas del año | Muestra de conveniencia puede concentrarse en compañeros, carreras o niveles similares | El equipo clasifica respuestas; acordar categorías y conservar las respuestas originales anonimizadas |
| 2 | El estudiante puede omitir temas, restricciones o disponibilidad | Nivel autoevaluado es subjetivo; fechas y horas pueden ingresarse mal | Refleja la situación declarada al crear cada plan; puede cambiar luego | Usuarios de la PoC no representan necesariamente a todos los estudiantes | Nivel y objetivo los declara el propio estudiante; son percepciones, no mediciones objetivas |
| 3 | El registro puede no capturar estudio fuera de la PoC o sesiones completadas sin marcar | Eventos perdidos, duplicados o acciones mal interpretadas | Se genera durante el uso; la cobertura depende del período de prueba | Sólo representa a usuarios que acepten probar la PoC y tengan acceso a ella | «Sesión realizada» debe definirse; los eventos del sistema no prueban por sí solos que hubo estudio efectivo |
| 4 | En producción: puede faltar el temario por completo, porque depende de que el usuario lo tenga y lo suba. | No se detectaron errores de extracción: el archivo tiene capa de texto legible | No es riesgo del equipo sino del usuario: sube el material que tiene. En el banco, 11 años de antigüedad | El banco cubre 1 de 3 materias, 1 carrera y 1 institución | El producto no puede verificar que lo que sube el usuario sea la versión vigente |
| 5 | Hay material de las 3 materias, pero desbalanceado: 3, 6 y 5 archivos por materia | Mejor de lo previsto, 0 duplicados exactos, 0 archivos ilegibles, 13 de 13 PDFs con capa de texto (no hace falta OCR). 1 par de casi-duplicados y 1 PDF con estructura malformada | Rango 2015-2020 en el banco; 6 de 14 sin fecha determinable. En producción depende de lo que suba el usuario | Una sola carrera (Ing. en Sistemas) y una sola institución en el banco | Confirmado y cuantificado. 4 de 14 archivos declaran en su propio texto ser compilaciones de estudiantes, y concentran el 55% del volumen de texto. Como banco de pruebas eso es realista: es lo que un estudiante tiene a mano y va a subir |
| 6 | Puede faltar respuesta de quienes no siguieron el plan o tuvieron una mala experiencia | Autorreporte y recuerdo pueden ser inexactos; las notas pueden confundirse con otros resultados | Debe recogerse después de cada uso/examen; el retraso afecta el recuerdo | Puede responder más quien quedó satisfecho; quienes abandonan pueden quedar fuera | «Útil», «adherencia» y «resultado» necesitan definiciones; el resultado no demuestra causalidad del plan |
| 7 | El modelo puede desconocer temas de nicho o contenidos específicos de una cátedra | Puede generar errores o afirmaciones plausibles pero falsas | El conocimiento tiene fecha de corte, distinta en ChatGPT y en Claude, y ninguno de los dos conoce los temarios de antemano | Calidad variable por idioma, disciplina y representación en los datos de entrenamiento; ambos candidatos están entrenados mayoritariamente en inglés | Las respuestas no vienen etiquetadas como correctas; requieren revisión con material de la cátedra |
| 8 | Los casos podrían no cubrir fallas relevantes o combinar pocos factores | El equipo puede etiquetar como «esperable» un caso discutible | Representa supuestos actuales, no cambios reales en cursos o modelos | No modela diversidad real de estudiantes salvo que se diseñe expresamente | Las etiquetas las asigna el equipo; documentar reglas y separar casos de prueba de evidencia empírica |

## 3. El plan de obtención

| # | Quién del equipo la consigue | Para cuándo |
|---|---|---|
| 1 | Por asignar entre Marco P. y Fede S.: preparar y aplicar encuesta/entrevistas con participación voluntaria | A definir en clase según el calendario del trimestre |
| 2 | Por asignar entre Marco P. y Fede S.: definir campos mínimos del formulario y probarlo con la PoC | A definir en clase; antes de la primera prueba de uso |
| 3 | Por asignar entre Marco P. y Fede S.: especificar eventos mínimos y registro de sesiones | A definir en clase; antes de la primera prueba de uso |
| 4 |  Por asignar entre Marco P. y Fede S.: localizar y abrir al menos un temario vigente de una materia elegida. Ya no hay que reclamar temarios a las cátedras: los sube el usuario. | Antes de la primera prueba de uso |
| 5 | Por asignar entre Marco P. y Fede S.: localizar y revisar permisos de una muestra de exámenes de esa materia. | Permisos y anonimización: antes del próximo push |
| 6 | Por asignar entre Marco P. y Fede S.: preparar preguntas de seguimiento y decidir si realmente hace falta recolectar notas | Después de la prueba de uso; fecha a definir |
| 7 | Por asignar entre Marco P. y Fede S.: diseñar y etiquetar casos límite sintéticos para probar métricas y mitigaciones | Si no hay muestra real suficiente o para probar validadores; fecha a definir |

**Límite de interpretación:** los datos sintéticos sirven para probar instrumentos,
validadores y escenarios; no permiten afirmar que los hábitos, riesgos o
resultados observados describan a estudiantes reales. Las fuentes aún no
inspeccionadas deben abrirse y revisarse antes de cambiar su estado a disponible.

## 4. El resultado de la obtención

Ejecutado el plan, la diferencia entre lo que el mapa supuso y lo que realmente
se consiguió. Todos los números salen de `eda-viabilidad.ipynb`, que corre sobre
`datos/`.

| # | Qué se obtuvo (o por qué no) | ¿Es la muestra que se entrega? | Qué cambió respecto de lo que esperábamos |
|---|---|---|---|
| 1 | Nada. No se preparó ni aplicó el instrumento | No | Pendiente |
| 2 | Nada. Requiere una PoC que no existe | No | Pendiente |
| 3 | Nada. Requiere la PoC instrumentada | No | Pendiente |
| 4 | 1 temario (Gestión de Datos), 5 páginas | Sí, como banco de pruebas | Cambió el sentido de la fuente: ya no hay que conseguir temarios, los sube el usuario. Que 2 de 3 materias del banco no tengan temario deja de ser una carencia y pasa a ser un caso de prueba necesario: el producto tiene que funcionar sin temario, porque muchos usuarios no lo van a subir |
| 5 | 13 archivos: 7 exámenes y 6 guías de práctica, de 3 materias | Sí, como banco de pruebas | Mejor de lo esperado en corrección: 0 duplicados, 0 ilegibles, 13 de 13 con capa de texto, sin OCR. Y lo que parecía el peor hallazgo —4 archivos (55% del texto) son compilaciones de estudiantes— cambia de signo: si el usuario sube lo que tiene a mano, eso es exactamente lo que va a subir. Como banco de pruebas, es realista |
| 6 | Nada. Depende de las fuentes 2 y 3 | No | Pendiente |
| 7 | No se generaron. El equipo decidió no usar sintéticos en esta instancia | No | Pendiente |