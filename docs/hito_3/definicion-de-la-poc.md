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
| 0.3 | 2026-11-03 | Decisiones de diseño 3.1.2 a 3.1.5; salen del alcance la fecha del material, detectar material de otra materia, la anonimización y la escalabilidad |

---

## 1. Propuesta

### 1.1 Overview

El estudiante completa un formulario (materia, temas, fecha de examen, nivel
autoevaluado por tema, horas disponibles por día y objetivo), sube los PDF de
su cursada (temario si lo tiene, parciales, guías de práctica) y ve un plan de
estudio día por día que respeta las horas declaradas, cubre todos los temas y
explica por qué priorizó cada uno. Para un tema del plan puede pedir
preguntas de autoevaluación apoyadas en sus archivos, que se muestran como
borrador a revisar, nunca como contenido verificado. Es para el estudiante que
prepara un examen con varias materias compitiendo por las mismas horas. La
PoC no sale a usuarios: se ejercita sobre el banco de pruebas de `datos/`.
Datos reales en todo lo medido (los 14 archivos del banco); formularios
sintéticos, declarados, porque no existe ninguno real (0 en el banco, celda 2).

El veredicto del Hito 2 fue **ajustar el alcance**. El banco es procesable:
13 de 13 PDF con capa de texto y 0 duplicados exactos (celda 4). Pero sólo 1
de 3 materias tiene temario (celda 3), así que la priorización se apoya en
nivel, fecha, horas y objetivo, y no en el peso real de cada tema; y el banco
cubre 1 sola carrera (celda 6), así que la PoC se demuestra sobre Ing. en
Sistemas. El 55% del texto son compilaciones
de estudiantes (celda 7): es lo que el usuario va a subir, y por eso lo
generado a partir de ese material no se presenta como correcto sin revisión.

Entra: formulario validado; ingesta de PDF con capa de texto y rechazo de lo
que no se puede leer; plan con explicación por tema; preguntas de
autoevaluación con revisión humana; el camino de error (no sube nada, sube un
archivo ilegible o malformado).

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
- **Mostrar la fecha del material.** El veredicto la ponía como condición,
  pero un material viejo puede seguir vigente si el temario no cambió, y
  6 de 14 archivos no la tienen (celda 5). Ver 3.1.2.
- **Detectar material de otra materia.** El veredicto lo ponía en el camino
  de error; se deja afuera para acotar la PoC. El plan no se ve afectado,
  porque los temas salen del formulario; las preguntas sí pueden apoyarse en
  ese material. Ver 3.1.3.
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
- **Escalabilidad y límites de latencia y costo por plan.** Sin usuarios no
  hay carga que sostener, y lo medido en 3.1.1 no sirve de línea de base para
  el sistema final. Latencia y costo se registran por pedido, sin umbral.
  Ver 3.1.5.
- **Anonimizar el material antes de enviarlo a OpenAI.** La PoC no sale a
  usuarios y sólo procesa el banco de `datos/`; el texto se manda tal cual.
  Los metadatos con autor (5 de 14, celda 7) no se envían, porque la ingesta
  extrae sólo el texto, pero el cuerpo de un archivo nombra a un docente
  (datasheet). Pasa a ser condición para la prueba de uso que habilita el GO.

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
tokens que el baseline; que el material del usuario salga hacia OpenAI, sin
anonimizar en la PoC (1.3); y la independencia de un
proveedor. Con 9 planes por corrida, los resultados variaron hasta 2 planes
entre dos corridas del mismo modelo: la prueba alcanza para elegir el
diseño, no para los umbrales, que se miden en la semana 9 sobre al menos 30
planes.

#### 3.1.2 Los datos

**Contexto.** El sistema no mantiene un corpus: el material llega en cada
pedido. Entran dos cosas: el formulario (materia, temas con su nivel, fecha
de examen, horas por día y objetivo) y los archivos que sube el usuario. El
plan del pipeline del veredicto (sección 4 de
[`4-veredicto.md`](../hito_2/4-veredicto.md)) fijaba: una ingesta que extrae
el texto y rechaza lo que no puede leer; detección del par de casi-duplicados
si el usuario sube dos versiones del mismo material; extracción de la fecha
del documento para mostrarla; `datos/` como banco de pruebas, nunca como
conjunto de evaluación; formulario y registro de eventos instrumentados desde
la primera prueba, con la evaluación separada por estudiante y por fecha de
examen; y por pedido, el formulario, los archivos con su texto y su fecha, y
el plan, con el feedback en tabla aparte. Lo que el veredicto no fijaba es
cuánto de ese texto llega al modelo. La prueba de 3.1.1 usó un tope de 30.000
caracteres con el temario primero: Gestión de Datos (19.832) e Investigación
Operativa (29.058) entraron enteras, pero en Redes `examen_01.pdf` se recortó
a 30.000 de 54.002 caracteres y otros dos archivos quedaron afuera; la materia
suma unos 109.000 caracteres (celda 2).

**Alternativas evaluadas.**

1. **Truncar con prioridad**, como en la prueba: temario, después parciales,
   después prácticas, hasta un tope. Barato y predecible, pero en Redes el
   plan se arma sin ver la mayor parte de lo que el usuario subió, y lo que
   se descarta lo decide el orden de carpetas, no el usuario. Descartada.
2. **Mandar sólo los fragmentos que mencionan los temas del formulario.**
   Reduce tokens, pero depende de que el nombre del tema en el formulario
   coincida con el vocabulario del archivo, y el 55% del texto son
   compilaciones de estudiantes con su propia terminología (celda 7). Agrega
   una pieza más que habría que evaluar. Queda como plan B del riesgo 3
   (1.4), no como diseño.
3. **Búsqueda semántica (embeddings).** Descartada: infraestructura que no
   entra en tres semanas, para un material que, por materia, cabe en la
   ventana de contexto del modelo.
4. **Mandar todo el material, entero, en la llamada.** Sigue en pie.

**Decisión.** La 4. Del plan del veredicto **se mantiene**: la ingesta por
pedido de PDF (con `pypdf`) y TXT, con rechazo explícito y mensaje para lo
que no tiene texto, no se puede abrir o tiene otro formato; `datos/` como
banco de pruebas de la ingesta; la instrumentación, que en la PoC es un
registro local por pedido (formulario, archivos con sus avisos, plan,
intentos, tokens y tiempo); y la partición de la evaluación, que con
formularios sintéticos se hace por formulario y por fecha de examen: ningún
formulario que se use para ajustar los prompts entra en los ≥30 planes de la
semana 9. **Cambia**: el material va entero, sin tope ni recorte; no se
extrae ni se muestra la fecha del documento, porque un material viejo puede
seguir vigente si el temario no cambió; los casi-duplicados se detectan pero sólo generan un aviso
al usuario, no se descarta nada; y la tabla de feedback no existe en la PoC,
porque no sale a usuarios. El texto se manda sin anonimizar (1.3).

**Consecuencias.** Los números de 3.1.1 se midieron con el tope de 30.000
caracteres, así que la prueba se vuelve a correr sin tope antes de construir,
empezando por Redes, que ya era el caso borde. Se resigna costo: a unos 4
caracteres por token, un plan de Redes manda del orden de 27.000 tokens de
material, y el reintento los vuelve a mandar. Se asume que el material de una
materia cabe en la ventana del modelo; si un pedido no cabe o el costo no se
sostiene, se pasa al plan B del riesgo 3 (límite por pedido y fragmentos por
tema). Si se detecta un casi-duplicado, el modelo recibe las dos versiones y
se pagan tokens redundantes. Sin fecha, el producto no avisa cuando un
material puede estar desactualizado: se asume que quien lo sube sabe si sigue
el programa vigente, y los temas del plan salen del formulario, no de los
archivos. Y mandar todo entero aumenta lo que sale hacia OpenAI, incluido
cualquier nombre que aparezca en el cuerpo del texto (en el banco, un
docente); en la PoC se acepta porque no hay material de usuarios, pero antes
de la prueba de uso hay que anonimizar.

#### 3.1.3 Workflow o agente

**Contexto.** El usuario completa el formulario, sube sus archivos y espera
ver un plan día por día con una explicación por tema y preguntas de
autoevaluación. Lo que hay que resolver no tiene ramas abiertas: los pasos
(validar el formulario, leer los archivos, generar, verificar, mostrar) se
conocen antes de empezar y son los mismos en cada pedido. La parte difícil es
aritmética (horas por día, cobertura de temas), y la prueba de 3.1.1 mostró
que el modelo solo no la resuelve: 0 de 18 planes válidos con una llamada
única, 17 de 18 cuando el código verifica y pide un reintento.

**Alternativas evaluadas.**

1. **Una llamada.** Formulario y material al modelo, JSON a la pantalla. Es el
   *baseline* de 3.1.1: 0 de 18 planes válidos, porque reformula los temas y
   no hay forma de verificar la cobertura. Descartada; queda como vara del
   criterio de ventaja.
2. **Workflow con pasos fijados por el equipo.** El código ordena los pasos y
   el modelo interviene en uno solo. Es lo que se midió en 3.1.1 como
   alternativa elegida. Sigue en pie.
3. **Workflow con una llamada por pieza:** una para el plan y otra para las
   preguntas de cada tema, a pedido. Cada salida es más corta y el reintento
   del plan no rehace las preguntas, pero suma llamadas y latencia por cada
   tema que se consulta. Descartada: una sola llamada deja una sola salida
   para validar y registrar.
4. **Agente.** El modelo, con herramientas (leer un archivo, validar el plan,
   recalcular minutos), decide qué hacer y cuándo terminar. Sirve cuando el
   camino no se conoce de antemano, que no es el caso. El costo, la latencia
   y la cantidad de llamadas varían por pedido, y es más difícil de evaluar
   contra criterios fijos. Además no está medido. Descartada.

**Decisión.** La 2, con estos pasos:

1. **Validación del formulario** (código): campos completos, niveles válidos,
   horas no negativas, días anteriores a la fecha del examen.
2. **Ingesta** (código), según 3.1.2: texto de cada PDF o TXT, rechazo con
   mensaje de lo que no se puede leer, aviso de casi-duplicados. Si no queda
   ningún archivo legible, se avisa y el plan se arma sólo con el formulario,
   sin preguntas.
3. **Generación** (LLM, una llamada): formulario y material entero; devuelve
   un JSON con el plan día por día, una explicación por tema y las preguntas
   de autoevaluación de cada tema.
4. **Validación del JSON** (código): formato, horas por día, cobertura, temas
   inventados, una explicación por tema, prioridad bajo ≥ medio ≥ alto, y
   preguntas para cada tema.
5. **Reintento** (LLM, a lo sumo uno), con los errores concretos del paso 4.
   Si sigue sin pasar, el plan se muestra marcado con los errores, no se
   oculta.
6. **Registro y pantalla** (código): el pedido se guarda según 3.1.2 y el
   JSON se muestra formateado: el plan por día, la explicación por tema y,
   al pedirlas para un tema, sus preguntas como borrador a revisar.

**Consecuencias.** El modelo no elige el camino, así que cada pedido cuesta
una o dos llamadas y su resultado se puede reproducir y verificar contra los
criterios de 2.3. Se resigna flexibilidad: cualquier caso que no esté en los
pasos (por ejemplo, ajustar el plan conversando) queda afuera, lo que ya está
en 1.3. Las preguntas viajan en la misma llamada que el plan: la salida es
más larga, el reintento por un error del plan las vuelve a generar, y la
prueba de 3.1.1 no las incluía, así que se suman a la nueva corrida que pide
3.1.2. La validación por código cubre que haya preguntas para cada tema, no
que sean correctas: eso lo mide la rúbrica del riesgo 2 (1.4). El material de
otra materia no se chequea en la PoC: si el usuario lo sube, llega al modelo
igual. El plan no cambia, porque los temas salen del formulario, pero las
preguntas pueden apoyarse en ese material.

#### 3.1.4 Construir o usar hecho

**Contexto.** Las piezas salen de los pasos de 3.1.3: la interfaz
(formulario, subida de archivos y pantalla del resultado), la ingesta, la
detección de casi-duplicados, la generación, la validación con reintento y el
registro por pedido. Restricciones: Python (el
EDA y la prueba de 3.1.1 ya lo usan), la PoC corre local para una persona por
vez (1.3), y la única API de LLM disponible es la de OpenAI.

**Alternativas evaluadas.**

1. **Interfaz.** *Flask o FastAPI con HTML propio*: control total, pero un
   backend y un frontend que construir y mantener, para una PoC local.
   *Línea de comandos*: lo más barato, pero no muestra el plan formateado ni
   permite pedir las preguntas de un tema. *Gradio*: resuelve lo mismo que
   Streamlit, pero está pensado para demos de un modelo con entradas y salida;
   el formulario tiene una cantidad variable de temas con su nivel y una
   disponibilidad por día. *Streamlit*: formulario, subida de archivos y
   pantalla en Python, sin frontend aparte. Sigue en pie.
2. **Salida del modelo.** *Structured Outputs* (`json_schema`): la API
   garantiza la forma del JSON, pero la validación por código hace falta igual
   para horas, cobertura y prioridad, y la prueba de 3.1.1 no se midió así.
   *JSON mode* (`json_object`): garantiza JSON válido, no su forma; es lo que
   se midió. Sigue en pie.
3. **Validación.** *Pydantic* para la forma y código propio para lo demás:
   suma una dependencia para chequear lo que `validar()` ya chequea. *Código
   propio*, a partir de `validar()` y `errores_prioridad()` de la prueba.
   Sigue en pie.
4. **Casi-duplicados.** *Una librería* (de similitud de texto o *MinHash*):
   pensada para colecciones grandes, cuando un pedido trae pocos archivos.
   *Jaccard propio* sobre vocabulario, el de la celda 10. Sigue en pie.
5. **Registro.** *SQLite*: permite consultas, que la evaluación de ≥30 planes
   no necesita. *Un archivo JSON por pedido* en una carpeta local, con la
   librería estándar. Sigue en pie.

**Decisión.**

| Pieza | Se usa hecho | Se construye |
|---|---|---|
| Interfaz | Streamlit | El formulario, la validación de campos y la vista del plan, las explicaciones y las preguntas |
| Ingesta | `pypdf` para PDF; lectura de TXT de la librería estándar | Las reglas de rechazo y sus mensajes |
| Casi-duplicados | — | Jaccard sobre vocabulario, umbral 0,30 (celda 10) |
| Generación | API de OpenAI con el SDK `openai`, `gpt-5.4-mini-2026-03-17` en JSON mode; `python-dotenv` para `OPENAI_API_KEY` y `OPENAI_MODEL` | Los prompts con las reglas |
| Validación y reintento | — | A partir de `validar()` y `errores_prioridad()`, más el chequeo de preguntas por tema |
| Registro | `json` de la librería estándar | Un archivo por pedido con lo que fija 3.1.2 |

Lo que se usa hecho es lo que no es el producto: interfaz, lectura de PDF y el
modelo. Lo que se construye es lo que el producto promete y los criterios de
2.3 verifican: las reglas del plan y su validación.

**Consecuencias.** Se agrega `streamlit` a `requirements.txt`; el resto ya
está. Streamlit vuelve a ejecutar el script en cada interacción, así que el
resultado del pedido se guarda en el estado de la sesión: pedir las preguntas
de un tema no puede disparar otra llamada al modelo. Con JSON mode, un JSON
con la forma equivocada lo detecta la validación y consume el reintento; si
eso pasa seguido en la nueva corrida de 3.1.2, se pasa a Structured Outputs
sin cambiar el resto. El código propio es poco y en buena parte ya probado,
pero es lo que hay que mantener y testear: ingesta, Jaccard, prompts y
validación. Se resigna la independencia del proveedor: la llamada usa el SDK
de OpenAI directamente, sin una capa que permita cambiar de modelo de otra
empresa.

#### 3.1.5 Requerimientos no funcionales

**Contexto.** La PoC pone a prueba que el plan sea válido y que la ingesta
distinga lo procesable de lo que no (1.2). Corre local, para una persona por
vez, sobre el banco de `datos/` (1.3).

**Alternativas evaluadas.**

1. **Fijar las tres propiedades a nivel de producto:** límites de latencia y
   costo por plan, pedidos concurrentes, integración continua. Descartada:
   no hay línea de base para los límites, nadie más que el equipo usa la
   PoC, y el trabajo no entra en tres semanas sin quitárselo a lo que la
   PoC prueba.
2. **Sólo confiabilidad.** Descartada: sin tests ni evaluación reproducible,
   cada cambio de prompt deja sin saber si los ≥30 planes siguen pasando.
3. **Confiabilidad primero, mantenibilidad después, escalabilidad afuera.**
   Dentro de mantenibilidad, se descartan los prompts en archivos aparte y la
   integración continua: con dos personas y un solo repositorio, no cambian
   lo que se puede verificar. Sigue en pie.

**Decisión.** La 3.

| Propiedad | Prioridad | Nivel que fija la PoC | Cómo se verifica |
|---|---|---|---|
| Confiable | 1 | ≥90% de planes válidos sobre ≥30 (1.2) | El script de evaluación, por código |
| | | 0 de 14 archivos del banco rompen la ingesta: cada uno da texto o un mensaje | Test automático sobre `datos/` |
| | | Un error de la API (timeout, sin crédito, respuesta que no es JSON) se muestra con un mensaje y se registra; la aplicación no se cae | Test automático con la API simulada |
| Mantenible | 2 | Tests automáticos de la validación y de la ingesta | Se corren antes de cada tag |
| | | Modelo y parámetros por variable de entorno (`OPENAI_MODEL`, 3.1.1) | Cambiar el modelo no toca el código |
| | | Evaluación reproducible: un script corre los ≥30 planes y guarda los resultados, como `experimentos/resultados/` | Un comando, el mismo para los dos integrantes |
| Escalable | 3 | No se busca (1.3) | — |

Latencia y costo no tienen umbral: se registran en cada pedido (3.1.2).

**Consecuencias.** La confiabilidad que se fija es la del plan y la de la
ingesta, no la del servicio: si la API de OpenAI falla, el usuario ve un
mensaje y vuelve a pedir; no hay reintentos por errores de red ni modelo de
respaldo. Los tests necesitan formularios sintéticos fijos y una API
simulada, que hay que construir. Cada corrida del script de evaluación tiene
costo de API, así que no se corre en cada cambio sino antes de cada decisión
y en la semana 9. Sin integración continua, que los tests pasen depende de
que alguien los corra. Sin límite de latencia, un plan de Redes con el
material entero y las preguntas puede tardar más de lo aceptable; si pasa,
los datos del registro permiten fijar el límite después. Y si el resultado es
GO, la prueba de uso va a pedir despliegue, concurrencia y límites de costo
que la PoC no construye.

### 3.2 Arquitectura

*Pendiente (Clase 6).*

---

## 4. Plan

### 4.1 Plan de construcción

*Pendiente (Clase 6).*
