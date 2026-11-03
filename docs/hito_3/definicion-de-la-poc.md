# Definición de la PoC — Study Copilot

**Documento del Hito 3 · Padilla, Marco; Sanches, Federico · se entrega con el tag `hito-3`**

Cuatro partes: propuesta, spec, diseño y plan. Este documento es el contrato:
lo que no está acá no se construye, y en la semana 9 la PoC se valida contra
los criterios de 2.3. Insumos: [`canvas.md`](../../canvas.md) (Hito 1) y
[`4-veredicto.md`](../hito_2/4-veredicto.md) (Hito 2); las celdas citadas son
de [`eda-viabilidad.ipynb`](../../eda-viabilidad.ipynb), que corre sobre
`datos/`.

## Historial de versiones

| Versión | Fecha | Qué cambió |
|---|---|---|
| 0, Clase 5 | 2026-10-13 | Overview y Objetivo, sin tag |
| 0.1 | 2026-10-27 | Fuera de alcance y riesgos; canvas pasa a v4 |
| 0.2 | 2026-11-02 | Decisión del modelo (3.1.1) con la prueba de `experimentos/`; riesgo 1 con cifras |

---

## 1. Propuesta

### 1.1 Overview

El estudiante completa un formulario (materia, temas, fecha de examen, nivel
autoevaluado por tema, horas disponibles por día y objetivo), sube los PDF de
su cursada (temario si lo tiene, parciales, guías de práctica) y ve un plan de
estudio día por día que respeta las horas declaradas, cubre todos los temas y
explica por qué priorizó cada uno, junto con la fecha del material que usó o
el aviso de que no se pudo determinar. Para un tema del plan puede pedir
preguntas de autoevaluación apoyadas en sus archivos, que se muestran como
borrador a revisar, nunca como contenido verificado. Es para el estudiante que
prepara un examen con varias materias compitiendo por las mismas horas. La
PoC no sale a usuarios: se ejercita sobre el banco de pruebas de `datos/`.
Datos reales en todo lo medido (los 14 archivos del banco); formularios
sintéticos, declarados, porque no existe ninguno real (0 en el banco, celda 2).

El veredicto del Hito 2 fue **ajustar el alcance**. El banco es procesable:
13 de 13 PDF con capa de texto y 0 duplicados exactos (celda 4). Pero sólo 1
de 3 materias tiene temario (celda 3), así que la priorización se apoya en
nivel, fecha, horas y objetivo, y no en el peso real de cada tema; 6 de 14
archivos no tienen fecha determinable (celda 5), por eso la fecha se muestra
o se avisa que falta; y el banco cubre 1 sola carrera (celda 6), así que la
PoC se demuestra sobre Ing. en Sistemas. El 55% del texto son compilaciones
de estudiantes (celda 7): es lo que el usuario va a subir, y por eso lo
generado a partir de ese material no se presenta como correcto sin revisión.

Entra: formulario validado; ingesta de PDF con capa de texto y rechazo de lo
que no se puede leer; plan con explicación por tema; preguntas de
autoevaluación con revisión humana; el camino de error (no sube nada, sube un
archivo ilegible o malformado, sube material de otra materia).

### 1.2 Objetivo

1. **Supuesto y riesgo.** De **factibilidad**: que un LLM por API, a partir
   del formulario y del texto de los PDF que sube el usuario, genera un plan
   que respeta las horas, cubre todos los temas, prioriza de forma
   consistente con nivel, fecha y objetivo, y explica cada prioridad; y que
   la ingesta distingue lo procesable de lo que no. De **valor**: que ese
   plan estructurado y explicado es mejor que lo que el estudiante obtiene
   hoy pidiéndole un plan a un chatbot genérico, el competidor más fuerte de
   la Sección 4 del canvas. El riesgo sale de la refutación de la Sección 3
   del canvas: que una sola llamada genérica dé un plan casi igual de bueno,
   y entonces el producto no agrega nada sobre el statu quo. Usabilidad y
   viabilidad no se prueban: la PoC no sale a usuarios, y las métricas de
   negocio de la Sección 6 están suspendidas por el veredicto hasta tener
   línea de base. La corrección conceptual de las preguntas generadas se
   mide sobre una muestra, pero no es el supuesto que la PoC pone a prueba:
   queda como riesgo en 1.4.
2. **Qué lo valida.** Los criterios de 2.3 cumplidos en la semana 9, y el
   proxy técnico de la Sección 6 del canvas sobre al menos 30 planes de las
   3 materias del banco: en al menos el 90%, el plan respeta las horas
   declaradas y cubre todos los temas ingresados, verificado por código y no
   a ojo. Y el workflow supera al *baseline* (una llamada única con el
   formulario y el material) en ese mismo conjunto.
3. **Qué decisión habilita.** GO: congelar el alcance en la semana 10 y
   pasar a una prueba de uso real, con el formulario y el registro de eventos
   instrumentados, que es lo único que mide las métricas de negocio. Cambiar
   el enfoque: si la validez estructural no llega al 90% con los planes B de
   1.4 agotados, el cronograma lo arma una regla determinista (horas
   proporcionales a 1 − nivel, ningún tema en cero, repaso al final) y el LLM
   queda sólo para explicar y generar preguntas. NO GO: validez estructural
   bajo el 50%, o ninguna ventaja sobre el *baseline*; en ese caso el
   producto no supera a "chatbot + calendario" y se vuelve a la Sección 4 del
   canvas.

### 1.3 Fuera de alcance

- **Priorizar por el peso real de cada tema.** Requiere temario, y en el
  banco sólo 1 de 3 materias lo tiene (celda 3). La priorización usa nivel,
  fecha, horas y objetivo.
- **Materias fuera de Ing. en Sistemas.** El banco cubre 1 carrera y 1
  institución (celda 6): no hay con qué probar el vocabulario de otra
  disciplina.
- **PDF escaneados, fotos y formatos que no sean PDF o TXT.** El banco no
  tiene ninguno sin capa de texto (13 de 13, celda 4), así que un OCR no se
  podría evaluar. Un archivo así se rechaza con un mensaje: es un caso borde,
  no una funcionalidad.
- **Resúmenes y ejercicios tipo parcial.** Del material complementario entran
  sólo las preguntas de autoevaluación. Medir la corrección conceptual pide
  una rúbrica con 2 revisores (EDA, confiabilidad); para un tipo de pieza
  entra en tres semanas, para tres no.
- **Regenerar o ajustar el plan conversando** (caso de uso 2 del canvas). Si
  cambian las horas o los niveles, la persona vuelve a cargar el formulario.
- **Toda afirmación sobre resultado académico, y las métricas de negocio del
  canvas** (adherencia, retención, tiempo de planificación). No hay línea de
  base y la PoC no sale a usuarios; quedan para la prueba de uso que habilita
  el GO.
- **Cuentas, persistencia entre sesiones, integración con calendarios y
  despliegue.** La PoC corre local y la usa una persona por vez.

### 1.4 Riesgos

**El LLM no respeta las restricciones numéricas del plan.** Sale del
supuesto de 1.2: que el plan sume las horas declaradas por día y no deje
temas afuera es aritmética, y un LLM puede devolver un plan plausible que no
cierra. Medido en 3.1.1: con el workflow, 17 de 18 planes son válidos, pero
la prioridad falla en 4 de 18 y el reintento no la corrigió. Señal:
validez estructural bajo el 90%. Plan B: el LLM devuelve la asignación como
JSON, el código verifica horas y cobertura y reintenta una vez con el error
concreto; si sigue sin cerrar, el cronograma lo arma la regla determinista
(horas proporcionales a 1 − nivel, ningún tema en cero, repaso al final) y el
LLM sólo explica. Es la salida "cambiar el enfoque" de 1.2.

**Las preguntas generadas tienen errores conceptuales.** Sale del veredicto:
es el riesgo central no estimado, y el 55% del texto del banco son
compilaciones de estudiantes de fidelidad no verificada (celda 7). Señal:
menos del 80% de las preguntas de la muestra aprobadas por la rúbrica. Plan B:
cada pregunta cita el fragmento del archivo del que sale, para que se pueda
contrastar; si aun así no alcanza, en lugar de generar preguntas se extraen
las de los parciales que subió el usuario (7 exámenes en el banco, celda 2),
que no tienen error de generación.

**Lo que sube el usuario no se puede usar.** Sale del veredicto: no sabemos
qué va a subir, porque el banco lo armó el equipo eligiendo qué incluir. En
el banco, 1 de 13 PDF está malformado (celda 4) y 6 de 14 archivos no tienen
fecha (celda 5); en uso puede llegar un escaneado, un archivo de otra materia
o más texto del que conviene mandar en una llamada (el banco suma 158.120
caracteres en 14 archivos, celda 2). Señal: algún archivo del banco que rompe
la ingesta en vez de producir un mensaje. Plan B: límite de tamaño por
archivo y por pedido, rechazo explícito de lo que no tiene texto, y al
modelo se le mandan sólo los fragmentos que mencionan los temas del
formulario, no el archivo entero.

---

## 2. Spec

### 2.1 Escenarios

*Pendiente (Clase 6).*

### 2.2 User experience

*Pendiente (Clase 6).*

### 2.3 Criterios de aceptación

*Pendiente (Clase 6).*

---

## 3. Diseño

### 3.1 Decisiones de diseño

#### 3.1.1 El modelo

**Contexto.** El modelo lee el formulario y el texto de los archivos que sube
el usuario, y genera el plan día por día con una explicación por tema; para
un tema del plan, genera preguntas de autoevaluación. No se entrena nada: es
un LLM por API. Datos de la prueba: 3 formularios sintéticos sobre las 3
materias del banco (con temario, sin temario, y 6 temas en 5 horas), con el
texto real de sus archivos. Restricciones: la única API disponible es la de
OpenAI, tres semanas, dos personas, pago por uso, y el material del usuario
sale de su máquina. La prueba (`experimentos/prueba_modelo.py`, resultados
en `experimentos/resultados/`, 2026-11-02) midió por código si el plan
respeta las horas de cada día, cubre todos los temas con su nombre, no
inventa temas y explica cada uno (validez), y si el promedio de minutos por
nivel cumple bajo ≥ medio ≥ alto (prioridad). Las preguntas de
autoevaluación no entraron en la prueba.

**Alternativas evaluadas.**

1. **Baseline: una llamada única** con el formulario y el material, como
   haría el estudiante con un chatbot; sólo se le pide formato JSON. Con
   `gpt-5.4-mini-2026-03-17`: 0 de 18 planes válidos. Respeta las horas en
   14 de 18, pero en ninguno conserva los nombres de los temas: los parte o
   los reformula ("SQL: consultas y subconsultas" pasa a "SQL: consultas
   básicas, SELECT/FROM/WHERE…"). Para una persona puede ser un buen plan;
   para el producto no se puede verificar que cubra cada tema, y la
   prioridad no se puede medir. Descartada; es la vara del criterio de
   ventaja.
2. **Workflow con el mismo modelo:** reglas explícitas en el prompt,
   validación del plan por código y un reintento con los errores concretos.
   Con `gpt-5.4-mini-2026-03-17`: 17 de 18 planes válidos (10 de 18 al
   primer intento), 17 de 18 respetan las horas, 18 de 18 conservan los
   temas, prioridad coherente en 14 de 18; 3,8 s y unos 13.900 tokens por
   plan de media, contra 4,6 s y 9.200 tokens del baseline. Sigue en pie.
3. **El mismo workflow con `gpt-4.1-mini-2025-04-14`**, un modelo anterior
   que no razona antes de responder. 9 de 9 planes válidos (7 al primer
   intento), pero prioridad coherente en 3 de 9, y 5,9 s por plan.
   Descartada: falla justo en priorizar, que es lo que el producto promete.
4. **Otro proveedor (Claude).** Descartado sin probar: no hay API
   disponible. La regla determinista que reparte los minutos queda como plan
   B (1.4), no como alternativa: no prueba la pieza de IA.

**Decisión.** La 2, con `gpt-5.4-mini-2026-03-17` fijado por versión y
configurable por `OPENAI_MODEL`. La inclinó la prueba: es la única que
produce planes verificables, casi nunca se pasa de las horas y prioriza
mejor que la alternativa 3.

**Consecuencias.** Se asume que reglas, validación y reintento alcanzan para
la prioridad, y la prueba no lo sostiene del todo: falla en 4 de 18 planes,
y en el único caso en que el reintento tuvo que corregirla, no la corrigió
(riesgo 1). Las dos fallas de la segunda corrida fueron en el formulario de
6 temas en 5 horas, que pasa a ser caso borde. Se resigna: un 50% más de
tokens que el baseline; que el material del usuario salga hacia OpenAI, lo
que obliga a anonimizar antes de enviar (3.1.5); y la independencia de un
proveedor. Con 9 planes por corrida, los resultados variaron hasta 2 planes
entre dos corridas del mismo modelo: la prueba alcanza para elegir el
diseño, no para los umbrales, que se miden en la semana 9 sobre al menos 30
planes.

#### 3.1.2 Los datos

*Pendiente (Clase 6).*

#### 3.1.3 Workflow o agente

*Pendiente (Clase 6).*

#### 3.1.4 Construir o usar hecho

*Pendiente (Clase 6).*

#### 3.1.5 Requerimientos no funcionales

*Pendiente (Clase 6).*

### 3.2 Arquitectura

*Pendiente (Clase 6).*

---

## 4. Plan

### 4.1 Plan de construcción

*Pendiente (Clase 6).*
