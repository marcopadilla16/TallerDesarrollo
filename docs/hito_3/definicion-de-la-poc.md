# Definición de la PoC — Study Copilot

**Documento del Hito 3 · Padilla, Marco; Sanches, Federico · se entrega con el tag `hito-3`**

Cuatro partes: propuesta, spec, diseño y plan. Este documento es el contrato:
lo que no está acá no se construye, y en la semana 9 la PoC se valida contra
los criterios de 2.3. Insumos: [`canvas.md`](../hito_1/canvas.md) (Hito 1) y
[`4-veredicto.md`](../hito_2/4-veredicto.md) (Hito 2); las celdas citadas son
de [`eda-viabilidad.ipynb`](../hito_2/eda-viabilidad.ipynb), que corre sobre
`datos/`.

## Historial de versiones

| Versión | Fecha | Qué cambió |
|---|---|---|
| 0, Clase 5 | 2026-10-13 | Overview y Objetivo, sin tag |
| 0.1 | 2026-10-27 | Fuera de alcance y riesgos; canvas pasa a v4 |
| 0.2 | 2026-11-02 | Decisión del modelo (3.1.1) con la prueba de `experimentos/`; riesgo 1 con cifras |
| 0.3 | 2026-11-03 | Decisiones de diseño 3.1.2 a 3.1.5; salen del alcance la fecha del material, detectar material de otra materia, la anonimización y la escalabilidad |
| 0.4 | 2026-11-10 | Entra el contenido que elige el estudiante (preguntas de autoevaluación, ejercicios prácticos y preguntas tipo parcial), que se genera aunque no se suba ningún archivo; los archivos se cargan por tema, más un material general. Cambian 1.1, 1.2, 1.3, 1.4, 3.1.2, 3.1.3, 3.1.4 y 3.2. Los ejercicios tipo parcial salían del alcance en 1.3: queda marcado como suspendido |
| 0.4.1 | 2026-11-11 | Correcciones sin cambio de contenido: los enlaces al canvas y al notebook, que se habían movido a `docs/hito_1/` y `docs/hito_2/`; y la alternativa 3 de 3.1.3, que había quedado mezclada con la 2 y con restos de su versión anterior |
| 0.5 | 2026-11-11 | Spec completa. User experience (2.2): señal de confianza binaria, sin puntaje; corregir es cambiar el formulario y volver a pedir. Escenarios (2.1): happy path, 4 casos borde (el peor, muchos temas en pocas horas) y el plan inválido después del reintento como error del sistema. Criterios de aceptación (2.3), según la plantilla de la cátedra (`plantilla/`). Calidad: válidos ≥ 90% y prioridad coherente ≥ 80%; la corrección del contenido queda como señal del riesgo 2, no como criterio. Latencia: p90 ≤ 120 s, con lo que se suspende «sin umbral» en 1.3 y 3.1.5. Casos borde: 5 de 5 escenarios cubiertos, con el error del sistema. Ventaja: workflow − *baseline* ≥ 30 puntos en planes válidos. En 1.2, la decisión cubre los umbrales nuevos (la prioridad bajo el 80% cambia el enfoque; una ventaja menor a 30 puntos es NO GO) y se suspende «ninguna ventaja» |

---

## 1. Propuesta

### 1.1 Overview

El estudiante completa un formulario (materia, temas, fecha de examen, nivel
autoevaluado por tema, horas disponibles por día y objetivo), sube, si los
tiene, los PDF o TXT de su cursada (temario, parciales, guías de práctica), en
la tarjeta de cada tema o como material general, y ve un plan de estudio día
por día que respeta las horas declaradas, cubre todos los temas y explica por
qué priorizó cada uno. Además elige qué contenido quiere para sus temas:
preguntas de autoevaluación, ejercicios prácticos y preguntas tipo parcial. Se
genera aunque no suba ningún archivo: en ese caso el modelo usa su conocimiento
general de la materia y la pantalla lo marca. Todo se muestra como borrador a
revisar, nunca como contenido verificado. Es para el estudiante que
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
que no se puede leer, con archivos por tema o generales; plan con explicación
por tema; preguntas de autoevaluación, ejercicios prácticos y preguntas tipo
parcial con revisión humana, con o sin archivos; el camino de error (sube un
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
   línea de base. La corrección conceptual del contenido generado se
   mide sobre una muestra, pero no es el supuesto que la PoC pone a prueba:
   queda como riesgo en 1.4.
2. **Qué lo valida.** Los criterios de 2.3 cumplidos en la semana 9, y el
   proxy técnico de la Sección 6 del canvas sobre al menos 30 planes de las
   3 materias del banco: en al menos el 90%, el plan respeta las horas
   declaradas y cubre todos los temas ingresados, verificado por código y no
   a ojo. Y el workflow supera al *baseline* (una llamada única con el
   formulario y el material) en ese mismo conjunto, por al menos 30 puntos (2.3).
3. **Qué decisión habilita.** GO, con los criterios de 2.3 cumplidos:
   congelar el alcance en la semana 10 y pasar a una prueba de uso real, con
   el formulario y el registro de eventos instrumentados, que es lo único que
   mide las métricas de negocio. Cambiar el enfoque: si la validez
   estructural no llega al 90% o la prioridad coherente al 80%, con los
   planes B de 1.4 agotados, el cronograma lo arma una regla determinista
   (horas proporcionales a 1 − nivel, ningún tema en cero, repaso al final) y
   el LLM queda sólo para explicar y generar preguntas. NO GO: validez
   estructural bajo el 50%, o una ventaja sobre el *baseline* menor a 30
   puntos; en ese caso el producto no supera a "chatbot + calendario" y se
   vuelve a la Sección 4 del canvas. Un escenario de 2.1 sin cubrir no decide
   nada: se corrige y se vuelve a chequear antes del GO. Una latencia sobre el
   techo de 2.3 pasa al plan B del riesgo 3 (3.1.5).
   *Suspendido en la v0.5:* «NO GO: [...] o ninguna ventaja sobre el
   *baseline*». Con el umbral de 2.3, una ventaja de entre 0 y 30 puntos no
   cumplía el GO ni caía en el NO GO.

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
- **Resúmenes.** Del material complementario entran las preguntas de
  autoevaluación, los ejercicios prácticos y las preguntas tipo parcial (desde
  la v0.4); los resúmenes quedan afuera.
  *Suspendido en la v0.4:* «sólo las preguntas de autoevaluación; los
  ejercicios tipo parcial, afuera». El motivo era que medir la corrección
  conceptual pide una rúbrica con 2 revisores (EDA, confiabilidad) y para un
  tipo de pieza entra en tres semanas, para tres no. Lo reemplaza la decisión
  del equipo de incluir los tres tipos; el costo de esa rúbrica sobre tres
  tipos queda como parte del riesgo 2 de 1.4, sin resolver.
- **Regenerar o ajustar el plan conversando** (caso de uso 2 del canvas). Si
  cambian las horas o los niveles, la persona vuelve a cargar el formulario.
- **Toda afirmación sobre resultado académico, y las métricas de negocio del
  canvas** (adherencia, retención, tiempo de planificación). No hay línea de
  base y la PoC no sale a usuarios; quedan para la prueba de uso que habilita
  el GO.
- **Cuentas, persistencia entre sesiones, integración con calendarios y
  despliegue.** La PoC corre local y la usa una persona por vez.
- **Escalabilidad y límite de costo por plan.** Sin usuarios no hay carga que
  sostener, y lo medido en 3.1.1 no sirve de línea de base para el sistema
  final. El costo se registra por pedido, sin umbral. Ver 3.1.5.
  *Suspendido en la v0.5:* «límites de latencia [...] Latencia y costo se
  registran por pedido, sin umbral». La plantilla pide un criterio de latencia
  con percentil; queda fijado en 2.3 como techo de tolerancia para la demo
  (p90 ≤ 120 s), no como límite de producto.
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

**El contenido generado tiene errores conceptuales.** Sale del veredicto:
es el riesgo central no estimado, y el 55% del texto del banco son
compilaciones de estudiantes de fidelidad no verificada (celda 7). Desde la
v0.4 el riesgo crece por dos lados: hay tres tipos de pieza (preguntas de
autoevaluación, ejercicios prácticos y preguntas tipo parcial) y se generan
aunque no haya archivos, en cuyo caso el modelo no tiene un fragmento en el
que apoyarse. Señal: menos del 80% de las piezas de la muestra aprobadas por
la rúbrica, contadas por tipo. Plan B: cada pieza cita el fragmento del
archivo del que sale, para que se pueda contrastar, y la que se generó sin
archivos se marca como tal (la PoC ya lo hace); si aun así no alcanza, en
lugar de generar preguntas se extraen las de los parciales que subió el
usuario (7 exámenes en el banco, celda 2), que no tienen error de generación.
Ese último plan B no cubre los ejercicios ni los pedidos sin archivos.

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

#### Happy path

- **Dado** un estudiante que prepara Gestión de Datos (la materia del banco con
  temario), con 3 temas de niveles distintos, fecha de examen, horas por día y
  objetivo, y con PDF legibles cargados en cada tema
- **Cuando** pide el plan y las preguntas de autoevaluación
- **Entonces** el sistema valida el formulario y extrae el texto de cada archivo
- **Y** muestra un plan día por día que respeta las horas de cada día y cubre los
  3 temas con su nombre
- **Y** el tema de nivel más bajo recibe más minutos que el de nivel más alto
- **Y** cada tema tiene su explicación de por qué se priorizó así
- **Y** las preguntas de cada tema aparecen como borrador a revisar, con los
  archivos en los que se apoyan
- **Y** el pedido queda registrado

#### Casos borde

##### 2.1.1 Materia sin temario

- **Dado** un estudiante de Investigación Operativa, que no tiene temario (2 de 3
  materias del banco, celda 3), con parciales y guías de práctica cargados
- **Cuando** pide el plan
- **Entonces** el plan cubre todos los temas del formulario y respeta las horas
- **Y** cada explicación justifica la prioridad con el nivel, la fecha, las horas
  o el objetivo, sin atribuirle a un tema un peso en el examen
- **Le cuesta al usuario:** que un tema que pesa mucho en el examen, pero que
  declaró saber bien, reciba poco tiempo.

##### 2.1.2 Sin archivos

- **Dado** un formulario completo, sin ningún archivo cargado
- **Cuando** pide el plan y ejercicios prácticos
- **Entonces** el sistema genera el plan y los ejercicios con el conocimiento
  general del modelo
- **Y** la pantalla marca que el contenido se generó sin material
- **Y** el registro deja constancia de que no hubo archivos
- **Le cuesta al usuario:** estudiar con un ejercicio equivocado sin un fragmento
  contra el cual contrastarlo.

##### 2.1.3 Archivo ilegible o con un formato no admitido

- **Dado** un tema con un PDF legible y otro archivo escaneado, sin capa de
  texto, o con un formato que no es PDF ni TXT
- **Cuando** pide el plan
- **Entonces** el sistema rechaza ese archivo con un mensaje que lo nombra y dice
  por qué
- **Y** el pedido sigue con los archivos legibles
- **Y** el registro guarda el aviso
- **Le cuesta al usuario:** creer que el plan tuvo en cuenta un material que no
  se leyó.

##### 2.1.4 Muchos temas en pocas horas (peor caso borde)

- **Dado** un formulario de Redes con 6 temas de niveles distintos y 5 horas en
  total, repartidas en 3 días: el caso en el que falló la prioridad en 3.1.1
- **Cuando** pide el plan
- **Entonces** el plan respeta las horas y cubre los 6 temas
- **Y** el promedio de minutos por nivel cumple bajo ≥ medio ≥ alto
- **Y** si después del reintento no lo cumple, el plan se muestra marcado con el
  error de prioridad, no se oculta (3.1.3, paso 5)
- **Le cuesta al usuario:** dedicarle menos tiempo a lo que menos sabe, que es lo
  que el producto promete evitar. Es el que más le cuesta: lo retoma 2.2.

#### Error del sistema

- **Dado** un pedido cuyo plan no pasa la validación por código: un día se pasa
  de las horas declaradas o falta un tema del formulario
- **Cuando** el reintento, con los errores concretos, tampoco lo corrige
- **Entonces** el sistema muestra el plan marcado con esos errores, sin ocultarlo
  ni presentarlo como válido (3.1.3, paso 5)
- **Y** el registro guarda el pedido con los dos intentos y sus errores
- **Y** el usuario puede volver a pedir, o ajustar el formulario (menos temas o
  más horas) y pedir de nuevo

La caída de la API (timeout, sin crédito, respuesta que no es JSON) no es este
escenario: está fijada como requerimiento en 3.1.5, con su test.

### 2.2 User experience

1. **Interacción y control.** El usuario completa el formulario en una app
   local de Streamlit: materia, fecha, objetivo, horas por día, cada tema con
   su nivel y sus archivos, y qué contenido quiere. Controla todo lo que el
   modelo recibe: los temas del plan salen del formulario, no de los archivos,
   y el modelo no puede agregar ni quitar ninguno (la validación lo rechaza).
   No controla cómo reparte los minutos: no puede ajustar el plan conversando
   (1.3).
2. **Señal de confianza.** No hay un puntaje: el modelo no da uno confiable.
   La señal es explícita y binaria. Todo se muestra como borrador a revisar.
   Cada tema dice en qué archivos se apoyó, el contenido generado sin material
   lo dice, y un plan que no pasó la validación se muestra marcado con sus
   errores. Los archivos rechazados y los casi-duplicados se avisan con su
   nombre.
3. **Corrección o aviso.** En la PoC no se puede editar la salida ni avisar
   que está mal: no hay tabla de feedback, porque no sale a usuarios (3.1.2).
   Para corregir, el usuario cambia el formulario (niveles, horas, temas o
   archivos) y vuelve a pedir.
4. **Peor caso borde (2.1.4).** Con 6 temas en 5 horas, si la prioridad sigue
   mal después del reintento, el usuario ve el plan igual, con una marca que
   dice que un tema de nivel más bajo recibió menos minutos que otro de nivel
   más alto. Para seguir, puede sumar horas o sacar los temas que mejor sabe y
   volver a pedir, o usar el plan sabiendo dónde falla.

### 2.3 Criterios de aceptación

| Criterio | Métrica (qué cuenta como respuesta aceptable) | Umbral (uno por tipo de error, si un error cuesta más que el otro) | Conjunto de evaluación | Cómo se chequea |
|---|---|---|---|---|
| Calidad de la respuesta | Plan válido: respeta las horas de cada día, cubre todos los temas del formulario con su nombre, no inventa temas y explica cada uno. Aparte, prioridad coherente: el promedio de minutos por nivel cumple bajo ≥ medio ≥ alto | Plan inválido, que no se puede usar: válidos ≥ 90% (1.2). Prioridad incoherente, que se puede usar pero no cumple lo que el producto promete: coherentes ≥ 80% (en 3.1.1 dio 14 de 18, el 78%) | ≥ 30 planes de las 3 materias, con formularios sintéticos que no se usaron para ajustar los prompts (3.1.2) | El script de evaluación cuenta, por código, los planes que pasan cada validación y los compara con cada umbral |
| Latencia (con el percentil) | Tiempo desde que el usuario envía el formulario hasta que ve el resultado, con el reintento incluido; percentil 90 | p90 ≤ 120 s. Es un techo de tolerancia para una demo, no un límite de producto: la única medición con el material entero dio 79 s en Redes con un reintento | Los mismos ≥ 30 pedidos de la fila anterior | El script calcula el p90 de los tiempos del registro (3.1.2) y lo compara con el umbral |
| Cobertura de los casos borde | Un escenario está cubierto si el sistema hace todo lo que dicen su «Entonces» y cada «Y» en 2.1. Entran los 4 casos borde y el error del sistema. En 2.1.4, mostrar el plan marcado cuando la prioridad falla es parte del escenario | 5 de 5 escenarios cubiertos | Un formulario sintético por escenario, con archivos del banco. Para 2.1.3 se agregan dos archivos de prueba declarados (uno sin capa de texto y otro con un formato no admitido), porque el banco no tiene ninguno (celda 4) | Una lista de sí o no por escenario, con cada «Entonces» y cada «Y». Rechazos, marcas y registro, con tests automáticos; lo que muestra la pantalla, a mano en la demo de la semana 9 |
| Ventaja sobre el *baseline* | Diferencia, en puntos porcentuales, entre los planes válidos del workflow y los del *baseline* (una llamada única, 3.1.1), con la misma validación de la fila de calidad. Exige los nombres de los temas porque el producto tiene que poder verificar que cubre cada uno, aunque el plan del *baseline* le pueda servir a una persona (3.1.1). La prioridad no se compara: con los temas reformulados no se puede medir | Workflow − *baseline* ≥ 30 puntos: más que la variación entre dos corridas del mismo modelo en 3.1.1 (hasta 2 de 9 planes, unos 22 puntos) | Los mismos ≥ 30 formularios, corridos con las dos variantes | El script corre las dos variantes y compara los porcentajes de planes válidos con el umbral |

La corrección conceptual del contenido generado (preguntas y ejercicios) no es un
criterio de aceptación: no es el supuesto que la PoC pone a prueba (1.2). Se mide
con la rúbrica sobre una muestra, como señal del riesgo 2 (1.4).

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
nivel cumple bajo ≥ medio ≥ alto (prioridad). Ni las preguntas de
autoevaluación ni el resto del contenido (ejercicios, preguntas tipo parcial)
entraron en la prueba.

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
registro local por pedido (formulario, archivos con su tema y sus avisos, plan,
intentos, tokens y tiempo); y la partición de la evaluación, que con
formularios sintéticos se hace por formulario y por fecha de examen: ningún
formulario que se use para ajustar los prompts entra en los ≥30 planes de la
semana 9. **Cambia**: el material va entero, sin tope ni recorte; los archivos
se cargan por tema, más un material general opcional, y el modelo recibe cada
grupo con su encabezado; no se
extrae ni se muestra la fecha del documento, porque un material viejo puede
seguir vigente si el temario no cambió; los casi-duplicados se detectan pero sólo generan un aviso
al usuario, no se descarta nada; y la tabla de feedback no existe en la PoC,
porque no sale a usuarios. El texto se manda sin anonimizar (1.3). Sin
archivos legibles el pedido sigue: el contenido se genera con el conocimiento
del modelo y el registro deja constancia de que no hubo material.

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

**Contexto.** El usuario completa el formulario, sube sus archivos, si los
tiene, y espera ver un plan día por día con una explicación por tema y el
contenido de estudio que pidió (preguntas de autoevaluación, ejercicios
prácticos, preguntas tipo parcial). Lo que hay que resolver no tiene ramas abiertas: los pasos
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
3. **Workflow con una llamada por pieza:** una para el plan y otra para el
   contenido de cada tema, a pedido. Cada salida es más corta y el reintento
   del plan no rehace el contenido, pero suma llamadas y latencia por cada
   tema que se consulta. Descartada: una sola llamada deja una sola salida
   para validar y registrar. Con tres tipos de contenido la salida única
   crece, y es el primer candidato a revisar si la nueva corrida muestra que
   el costo o la latencia no se sostienen.
4. **Agente.** El modelo, con herramientas (leer un archivo, validar el plan,
   recalcular minutos), decide qué hacer y cuándo terminar. Sirve cuando el
   camino no se conoce de antemano, que no es el caso. El costo, la latencia
   y la cantidad de llamadas varían por pedido, y es más difícil de evaluar
   contra criterios fijos. Además no está medido. Descartada.

**Decisión.** La 2, con estos pasos:

1. **Validación del formulario** (código): campos completos, niveles válidos,
   horas no negativas, días anteriores a la fecha del examen, tipos de
   contenido conocidos.
2. **Ingesta** (código), según 3.1.2: texto de cada PDF o TXT, de un tema o
   generales, rechazo con mensaje de lo que no se puede leer, aviso de
   casi-duplicados. Si no queda ningún archivo legible, se avisa y se sigue: el
   plan y el contenido pedido se generan igual, con el conocimiento general del
   modelo, y la pantalla lo marca.
3. **Generación** (LLM, una llamada): formulario y material entero, separado
   en general y por tema; devuelve un JSON con el plan día por día, una
   explicación por tema y, para cada tema, el contenido que el estudiante pidió
   (preguntas de autoevaluación, ejercicios prácticos, preguntas tipo parcial).
4. **Validación del JSON** (código): formato, horas por día, cobertura, temas
   inventados, una explicación por tema, prioridad bajo ≥ medio ≥ alto, y al
   menos un ítem de cada tipo pedido para cada tema.
5. **Reintento** (LLM, a lo sumo uno), con los errores concretos del paso 4.
   Si sigue sin pasar, el plan se muestra marcado con los errores, no se
   oculta.
6. **Registro y pantalla** (código): el pedido se guarda según 3.1.2 y el
   JSON se muestra formateado: el plan por día, la explicación por tema y una
   pestaña por cada tipo de contenido pedido, como borrador a revisar, con la
   indicación de en qué archivos se apoyó cada tema.

**Consecuencias.** El modelo no elige el camino, así que cada pedido cuesta
una o dos llamadas y su resultado se puede reproducir y verificar contra los
criterios de 2.3. Se resigna flexibilidad: cualquier caso que no esté en los
pasos (por ejemplo, ajustar el plan conversando) queda afuera, lo que ya está
en 1.3. El contenido viaja en la misma llamada que el plan: con los tres tipos
pedidos la salida es bastante más larga, el reintento por un error del plan lo
vuelve a generar, y la prueba de 3.1.1 no lo incluía, así que se suma a la
nueva corrida que pide 3.1.2. La validación por código cubre que haya
contenido de cada tipo pedido para cada tema, no que sea correcto: eso lo mide
la rúbrica del riesgo 2 (1.4). Un tema sin archivos recibe contenido generado
con el conocimiento del modelo, que es justo donde más puede equivocarse. El
material de otra materia no se chequea en la PoC: si el usuario lo sube, llega
al modelo igual. El plan no cambia, porque los temas salen del formulario, pero
el contenido puede apoyarse en ese material.

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
| Interfaz | Streamlit | El formulario (con los archivos por tema, el material general y la elección del contenido), la validación de campos y la vista del plan, las explicaciones y cada tipo de contenido |
| Ingesta | `pypdf` para PDF; lectura de TXT de la librería estándar | Las reglas de rechazo y sus mensajes |
| Casi-duplicados | — | Jaccard sobre vocabulario, umbral 0,30 (celda 10) |
| Generación | API de OpenAI con el SDK `openai`, `gpt-5.4-mini-2026-03-17` en JSON mode; `python-dotenv` para `OPENAI_API_KEY` y `OPENAI_MODEL` | Los prompts con las reglas |
| Validación y reintento | — | A partir de `validar()` y `errores_prioridad()`, más el chequeo del contenido pedido por tema |
| Registro | `json` de la librería estándar | Un archivo por pedido con lo que fija 3.1.2 |

Lo que se usa hecho es lo que no es el producto: interfaz, lectura de PDF y el
modelo. Lo que se construye es lo que el producto promete y los criterios de
2.3 verifican: las reglas del plan y su validación.

**Consecuencias.** Se agrega `streamlit` a `requirements.txt`; el resto ya
está. Streamlit vuelve a ejecutar el script en cada interacción, así que el
resultado del pedido se guarda en el estado de la sesión: cambiar de pestaña
o abrir el contenido de otro tema no puede disparar otra llamada al modelo. Con JSON mode, un JSON
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

El costo no tiene umbral: se registra en cada pedido (3.1.2). La latencia tiene
el techo de tolerancia de 2.3 (p90 ≤ 120 s). *Suspendido en la v0.5:* «Latencia y
costo no tienen umbral», por el criterio de latencia que pide la plantilla (2.3).

**Consecuencias.** La confiabilidad que se fija es la del plan y la de la
ingesta, no la del servicio: si la API de OpenAI falla, el usuario ve un
mensaje y vuelve a pedir; no hay reintentos por errores de red ni modelo de
respaldo. Los tests necesitan formularios sintéticos fijos y una API
simulada, que hay que construir. Cada corrida del script de evaluación tiene
costo de API, así que no se corre en cada cambio sino antes de cada decisión
y en la semana 9. Sin integración continua, que los tests pasen depende de
que alguien los corra. Y si el resultado es
GO, la prueba de uso va a pedir despliegue, concurrencia y límites de costo
que la PoC no construye.

*Suspendido en la v0.5:* «Sin límite de latencia, un plan de Redes con el
material entero y las preguntas puede tardar más de lo aceptable; si pasa, los
datos del registro permiten fijar el límite después». Lo reemplaza el techo de
2.3: si un pedido lo supera de forma sistemática, se pasa al plan B del riesgo 3
(límite por pedido y fragmentos por tema).

### 3.2 Arquitectura

```mermaid
flowchart LR
    U([Estudiante]) -->|formulario y archivos| I
    subgraph App local en Streamlit
        I["Interfaz<br/>Streamlit"]
        IN["Ingesta<br/>pypdf, TXT"]
        P["Procesamiento<br/>validación del formulario,<br/>casi-duplicados, registro JSON"]
        M["Modelo<br/>workflow: prompt, validación,<br/>1 reintento"]
    end
    API[("API de OpenAI<br/>gpt-5.4-mini-2026-03-17")]
    I --> IN --> P --> M
    M <-->|JSON mode| API
    M -->|JSON del plan| I
    M --> R[("registro/<br/>un JSON por pedido")]
    E["Evaluación<br/>script ≥30 planes + tests"] -.->|formularios sintéticos<br/>y datos/| IN
    E -.->|lee| R
```

| Pieza | Qué es en este proyecto | Se construye o se usa hecha | Con qué (API, modelo preentrenado, librería) |
|---|---|---|---|
| **Ingesta** | Recibe el formulario y los archivos que sube el usuario en cada pedido, extrae el texto de cada PDF o TXT y rechaza con un mensaje lo que no se puede leer o tiene otro formato | Se usa hecha la lectura; se construyen las reglas de rechazo y los mensajes | `pypdf`; lectura de TXT de la librería estándar; subida de archivos de Streamlit |
| **Procesamiento** | Valida el formulario, detecta casi-duplicados, arma el material entero que va al modelo y guarda el registro del pedido | Se construye | Código propio (Jaccard sobre vocabulario, umbral 0,30, celda 10); `json` de la librería estándar para el registro |
| **Modelo o agente** | El workflow de 3.1.3: una llamada que devuelve el plan, las explicaciones y el contenido pedido (preguntas, ejercicios, preguntas tipo parcial) en JSON, la validación por código y a lo sumo un reintento con los errores | Se usa hecho el modelo; se construyen los prompts, la validación y el reintento | API de OpenAI con el SDK `openai`, `gpt-5.4-mini-2026-03-17` en JSON mode; `python-dotenv` para `OPENAI_API_KEY` y `OPENAI_MODEL` |
| **Interfaz** | Una app local donde un tercero completa el formulario, sube sus archivos por tema o como material general, elige qué contenido quiere y ve el plan por día, la explicación de cada tema, cada tipo de contenido como borrador y los mensajes de error | Se usa hecho el framework; se construyen las pantallas | Streamlit |
| **Evaluación** | Un script que corre el workflow y el *baseline* sobre el conjunto congelado y mide validez, prioridad y ventaja contra los criterios de 2.3; tests automáticos de ingesta, validación y errores de la API; la rúbrica del contenido generado, a mano | Se construye | Código propio a partir de [`prueba_modelo.py`](../../experimentos/prueba_modelo.py), con la misma API y el mismo modelo; `pytest` para los tests |

---

## 4. Plan

### 4.1 Plan de construcción

*Pendiente (Clase 6).*
