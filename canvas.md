# AI Opportunity Canvas

> **Equipo:** …
> **Integrantes:** Padilla, Marco; Sanches, Federico
> **Caso:** Study Copilot
> **Versión:** 2 · **Fecha:** 29/09/2026

## Cómo se usa

Este canvas se completa **en equipo** durante la Clase, y se pushea al repo del
equipo como `canvas.md`. Es un documento vivo, se revisa cada vez que cambia alguna definición. El history se usa en la evaluación.

## Estado de validación actual

- **Confirmado (preliminar):** existe señal de problema de priorización y de
  uso de herramientas parciales (organización + recursos sueltos).
- **En validación:** magnitud del problema, adopción real en el segmento
  objetivo, y umbrales de éxito de la PoC.
- **Pendiente docente:** criterios finales de corte para métricas y alcance
  esperado de detalle en proxies técnicas y riesgos éticos.
- **Alternativa metodológica:** cuando no haya trabajo de campo en esta etapa,
  se usarán datos sintéticos sólo para diseñar instrumentos y probar
  sensibilidad, **no** para validar hipótesis en población real.

Algunas convenciones:

1. Nada de tecnología en la sección 1.
2. Todo lo que se escribe está sujeto a verificación. Y las verificaciones deben ser explícitas. Si no se sabe, hay que ser honesto.
3. Todas las secciones deben incluir `Evidencia` que confirme lo que escribieron, pero siempre con mentalidad de intentar refutarlo.

> "our research findings are not truths — they are merely confirming or
> disconfirming evidence that either supports or refutes our point of view.", Teresa Torres

Sesgos: el **sesgo de confirmación**
—buscamos la evidencia que nos da la razón— y la **escalada del compromiso**
—cuanto más invertimos en una idea, más nos casamos con ella—.

---

## 1. Problema y contexto

### A quién le pasa

Estudiante universitario (ej.: ingeniería, ciencias exactas) que cursa varias materias en simultáneo y se prepara para parciales o finales con poco tiempo y mucho material.

Situación concreta: en la semana previa a un examen, tiene la teoría y práctica dispersa (apuntes, PDFs, guías), varias materias compitiendo por las mismas horas, y ventanas de estudio cortas e irregulares entre cursada, trabajo y otras obligaciones.


### Qué le pasa

El progreso que intenta lograr es llegar preparado al examen aprovechando el tiempo que tiene, no "estudiar" en abstracto. Lo que le sale mal:

- No logra decidir qué estudiar primero ni *cuánto* dedicarle a cada tema dada la fecha del examen, su nivel en cada tema y las horas disponibles. La priorización depende de muchos factores difíciles de evaluar rápido.
- Quiere rendir bien frente a pares y docentes, y no quedar como alguien que "no llegó" por mala organización más que por no saber.
- Ansiedad e incertidumbre ("no sé si estoy usando bien el tiempo"), sensación de estar siempre atrasado y culpa cuando abandona un tema.


### Cuánto le cuesta

El costo no es sólo "estudiar muchas horas", sino usar mal horas escasas en la etapa más sensible (días previos a parciales/finales). El impacto aparece en tres planos:

- **Tiempo:** horas perdidas en decidir qué estudiar, reordenar prioridades y rehacer cronogramas.
- **Carga mental/emocional:** ansiedad, incertidumbre y fatiga de decisión por no saber si se está priorizando bien.
- **Resultado académico:** riesgo de subestudiar temas de alto peso y sobreestudiar temas de bajo impacto, llegando al examen con cobertura desbalanceada.

En síntesis, el costo principal es de asignación ineficiente del tiempo disponible, no de falta total de horas.

Como oportunidad de mejora, esta hipótesis se puede convertir en evidencia dentro del trimestre con un mínimo viable de validación:

- **Encuesta corta** (10-20 estudiantes): medir tiempo de planificación, percepción de ansiedad y autopercepción de priorización.
- **Entrevistas breves** (6-8 estudiantes): entender decisiones reales ("qué eligen estudiar primero y por qué") y detectar patrones.

Qué se pretende medir con ese mínimo viable:

- **Tiempo de planificación** antes de estudiar (línea de base).
- **Nivel de incertidumbre** percibido antes del examen.
- **Señales de mala priorización** (temas clave relegados, repaso insuficiente, cambios de plan de último momento).

**ALTERNATIVA DATOS SINTETICOS:** si no se llega a trabajo de campo en esta etapa, se puede usar una simulación con datos sintéticos sólo para diseñar métricas y probar escenarios (conservador/medio/crítico), dejando explícito que no reemplaza evidencia empírica ni valida el problema en población real.

### Evidencia

#### De confirmación

- Experiencia propia del equipo y de compañeros cercanos: señal exploratoria útil para formular la hipótesis, pero insuficiente como evidencia concluyente por sí sola.
- Existencia y uso frecuente de herramientas de organización del estudio (Notion, calendarios, técnica Pomodoro, planners) como señal de que el problema se intenta resolver con alternativas parciales.
- Circulación de resúmenes y bancos de ejercicios compartidos (grupos de WhatsApp/Drive por materia) como indicio de búsqueda activa de apoyo para llegar a examen.
- Plan de validación empírica dentro del trimestre: encuesta corta (10-20 estudiantes) + entrevistas breves (6-8 estudiantes) para medir dificultad de priorización, tiempo de planificación e incertidumbre percibida.

#### De refutación

- Si al preguntar, los estudiantes dicen que ya se organizan bien solos (con su propio criterio o una simple lista) y no cambiarían, el dolor es menor del que suponemos.
- Que el cuello de botella real sea entender el contenido, no organizarlo.
- Que la ansiedad ante el examen no se reduzca con un plan (podría incluso aumentar la presión de "cumplir el cronograma").
- Que la evidencia de campo no confirme la hipótesis central de priorización (por ejemplo, que el problema dominante sea disciplina, comprensión o falta de horas, y no organización).

---

## 2. Stakeholders

### Roles

| Papel | Quién es | Qué necesita ver para decir que sí |
|---|---|---|
| Usuario | Estudiante que cursa varias materias y prepara exámenes | Que el plan generado sea realista y le ahorre tiempo de decisión; que el material adicional (resúmenes, ejercicios) sea correcto y útil |
| Influenciador | Compañeros de cursada, grupos de estudio | Que otros de su grupo lo usen y les sirva; recomendación boca a boca |
| Recomendador | Docentes / ayudantes que sugieren herramientas de estudio | Que no fomente hacer trampa ni reemplace el aprendizaje; que el contenido no tenga errores conceptuales |
| Comprador | El propio estudiante (si es freemium/pago individual) | Que el valor justifique el precio frente a alternativas gratuitas |
| Decisor | El propio estudiante | Igual que usuario y comprador (roles unificados en B2C) |
| Saboteador | Docente que ve riesgo de dependencia/copia; o el propio hábito de estudio ya instalado |  |


### Evidencia

#### De confirmación

- El usuario tiene el problema y hoy hace algo al respecto: arma cronogramas a mano, usa Notion/calendario, pide resúmenes a compañeros.
- Existe "presupuesto" en el mercado que reemplazamos: estudiantes ya pagan por apuntes, clases particulares y apps de estudio (evidencia de que el comprador existe y tiene con qué gastar).

#### De refutación

- Que el estudiante no pague nada por organizar el estudio y no piense hacerlo: todo su gasto va a contenido (particulares), no a planificación.
- Que el docente actúe como saboteador activo y desaconseje/prohíba la herramienta, frenando la adopción por la vía del recomendador.
- Que la decisión sea 100% individual e impulsiva y no haya un segundo actor que sostenga el uso en el tiempo (alta rotación).

---

## 3. Hipótesis de solución

### Descripción del producto

Plataforma web donde el estudiante completa un formulario con **materia, temas,
fecha de examen, nivel autoevaluado por tema, tiempo disponible por día y
objetivo** (aprobar / sacar más de 8 / preparar final). Con eso el sistema
genera un **plan de estudio personalizado** (qué estudiar, cuándo y cuánto
tiempo), con una **explicación** de por qué priorizó cada tema. Opcionalmente, el
usuario pide **material adicional**: resumen, ejercicios tipo parcial y preguntas
de autoevaluación.

Casos de uso principales:

1. Generar plan de estudio a partir del formulario.
2. Regenerar/ajustar el plan si cambian tiempos o niveles.
3. Solicitar contenido complementario para un tema del plan.

Criterios de aceptación (hipótesis): el plan cubre todos los temas ingresados,
respeta las horas disponibles declaradas, prioriza de forma coherente con
nivel + fecha + objetivo, y la explicación es entendible.

Supuestos: el usuario ingresa datos honestos (nivel, tiempo); la calidad
generada por el LLM es suficiente para ser útil sin revisión experta.

### Acción

El estudiante decide distinto cómo asignar sus horas de estudio antes de un examen. En lugar de improvisar o dedicar tiempo a planificar, arranca con un cronograma priorizado y con material listo para cada bloque.

### Predicción

Lo que haría falta saber para tomar mejor esa decisión: **qué asignación de
tiempo por tema maximiza el resultado esperado en el examen**, dado el nivel
actual, la dificultad/peso de cada tema y las horas disponibles. En la versión
LLM, la "predicción" es una recomendación generativa de priorización + la
generación de contenido pertinente (resúmenes/ejercicios ajustados al tema y
nivel).

### Juicio

Cómo se valoran resultados y errores, y quién lo pone:

- Qué pesa más: ¿cubrir todo superficialmente o dominar lo esencial? Lo define
  el **objetivo** que elige el usuario (aprobar vs. sacar >8 vs. final).
- Costo de los errores: un plan que **sobreestima** el tiempo disponible frustra;
  uno que **prioriza mal** un tema difícil puede hacer perder el examen; un
  ejercicio o resumen **incorrecto** enseña mal (peor que no darlo).
- El juicio lo fija el equipo al diseñar la priorización y los límites (ej.: no
  dejar ningún tema en cero, reservar tiempo de repaso). Si nadie lo escribe, lo
  decide por descarte el prompt/modelo.

### Evidencia

#### De confirmación

- La decisión existe y hoy se toma peor: el estudiante ya decide cada semana qué
  estudiar, a ojo.
- La "predicción" es posible: existen tutores humanos y guías de estudio que ya
  recomiendan priorización; los LLMs generan planes y material de estudio de
  forma demostrada en productos existentes.

#### De refutación

- Que el estudiante tome la misma decisión con o sin el
  plan (siga su intuición igual). Entonces el sistema no cambia nada.
- Que la calidad del contenido generado no alcance sin revisión experta, y el
  usuario deba corregirlo tanto que no ahorre tiempo.
- Que una regla simple (repartir horas proporcional a "peso × (1 − nivel)")
  dé un plan casi tan bueno como el LLM: entonces gran parte no necesita modelo.

---

## 4. Alternativas y statu quo

### Qué hace hoy el usuario

- Arma un cronograma a mano (papel, notas del celular, calendario, Notion).
- Prioriza por intuición o por lo que "entra en el parcial".
- Busca resúmenes y ejercicios en grupos de WhatsApp/Drive, en internet, o los
  hace desde cero.
- En muchos casos no planifica: estudia lo primero que abre o lo que otros
  le dicen que "toma el profesor".

Costo del statu quo: tiempo de planificación, temas que quedan afuera, material
disperso y de calidad variable, ansiedad.

### Qué otras soluciones existen o podrían aparecer

- **Apps de organización** (Notion, Todoist, Google Calendar, Pomodoro): ordenan
  el tiempo pero no deciden qué priorizar ni generan contenido.
- **Herramientas de estudio con IA** (ChatGPT/Claude directo, Quizlet, apps de
  flashcards, generadores de resúmenes): el estudiante ya puede pedirle un plan a
  un chatbot genérico — este es el competidor más fuerte y podría mejorar solo.
- **Clases particulares / grupos de estudio:** resuelven priorización y
  comprensión, con costo de plata y coordinación.
- **Bancos de exámenes de la cátedra** (parciales viejos): fuertes para saber qué
  entra.

### Por qué lo nuestro sería suficientemente mejor como para que alguien se mueva

- Junta en un solo flujo lo que hoy está partido: **priorización + cronograma +
  material a medida**, atado a fecha, nivel y horas reales (un chatbot genérico
  requiere que el usuario sepa pedirlo y no integra el calendario ni el nivel por
  tema de forma estructurada).
- Estructura la entrada (formulario) para producir un plan **accionable y
  explicado**, no una respuesta genérica.

### Evidencia

#### De confirmación

- Hipótesis verificable: una proporción relevante de estudiantes usa al menos
  una herramienta de organización (Notion, calendario, Pomodoro, planners) y al
  menos un chatbot/LLM para tareas de estudio.
- Validación mínima dentro del trimestre: encuesta corta (20-30 estudiantes) y
  registro de frecuencia de uso (diario/semanal/ocasional), casos de uso
  (planificar, resumir, practicar) y combinación de herramientas.
- Criterio preliminar de lectura: si una mayoría de la muestra usa "organización
  + chatbot", hay señal de hábito instalado; si aparece baja adopción o uso sin
  valor percibido, la hipótesis pierde fuerza.
- Existencia de bancos de parciales y resúmenes compartidos por materia.

#### De refutación

- Que el statu quo "ChatGPT + calendario" ya sea suficientemente bueno y el
  estudiante no vea razón para cambiar.
- Que la mejora percibida no justifique aprender una herramienta nueva.
- Que la evidencia de campo no confirme adopción real de herramientas de
  organización y chatbots en el segmento objetivo.

**ALTERNATIVA DATOS SINTETICOS:** si no se llega a trabajo de campo en esta etapa, se puede usar una simulación con datos sintéticos para probar el instrumento y el análisis, dejando explícito que no valida adopción real.

---

## 5. Hipótesis de datos

### Dataset

Una fila por dato.

En "¿Lo vimos?" va:

- **Sí**: cuando el equipo accedió y revisó una muestra real de ese dato/fuente.
- **No**: cuando sabemos que existe o está publicado, pero todavía no lo
  inspeccionamos directamente.

Ejemplo: un temario en la web de cátedra puede ser "Público = Sí", pero
"¿Lo vimos? = No" si aún no lo abrimos/revisamos.

| Dato | Origen | ¿Público? | ¿Lo vimos? | ¿Sensibles? | Sesgo conocido | Comentarios |
|---|---|---|---|---|---|---|
| Formulario del usuario (materia, temas, fecha, nivel, horas, objetivo) | Ingresado por el propio usuario | No | No | Sí (datos académicos personales) | Autoevaluación de nivel subjetiva y sesgada | Dato del que más depende el producto; se genera en uso, hay que registrarlo desde el día 1 |
| Conocimiento base para generar plan/contenido | Modelo LLM preentrenado (proveedor) | No (pesos), sí el servicio | No | No | Sesgos del corpus de entrenamiento del LLM; puede alucinar | No entrenamos el modelo; consumimos API. Riesgo: cobertura despareja por materia/idioma |
| Programas y temarios de cátedras | Sitios de facultades / cátedras | Parcial | No | No | Desactualización | Útil para validar que los temas y su peso sean reales |
| Parciales/finales anteriores | Cátedras, repositorios estudiantiles | Parcial | No | Puede tener nombres | Sesgo de "lo que tomó históricamente ≠ lo que tomará" | Serviría para calibrar priorización y simulacros |
| Feedback de resultado (¿el plan sirvió? ¿aprobó?) | Registrado por el usuario post-uso | No | No | Sí (nota/resultado académico) | Sesgo de respuesta (contesta quien está conforme) | Sin esto no hay "respuesta correcta" para mejorar ni para medir éxito |


### Evidencia

#### De confirmación

- Los datos de entrada existen porque los provee el propio usuario (barato de
  obtener, pero sólo en uso).
- Temarios y parciales viejos son parcialmente accesibles públicamente.

#### De refutación

- El dato clave (feedback de si el plan funcionó y si
  aprobó) no existe hoy y sólo aparece después de meses de uso; sin él no se
  puede medir éxito real ni mejorar la priorización.
- Que la autoevaluación de nivel sea tan poco fiable que degrade todo el plan.
- Que los temarios reales estén desactualizados o no publicados y no se puedan
  usar para validar el peso de cada tema.

---

## 6. Métrica de éxito

### Métrica de negocio

* **% de sesiones planificadas que efectivamente se realizan** (adherencia al
plan)
* **% de usuarios que regeneran/usan el plan para un segundo examen**
(retención = señal de que sirvió)
* tiempo dedicado a **planificar** antes vs. después (debe bajar).

### Umbral preliminar (a validar)

Estos valores se usan como objetivo inicial de trabajo para el trimestre. No son
definitivos: se validan con docente, línea de base y resultados de la prueba
piloto.

**PENDIENTE DOCENTE:** validar estos rangos preliminares y el criterio de corte
de "no vale la pena" para evitar umbrales arbitrarios.

- Adherencia al plan: objetivo preliminar entre 50% y 70% de las sesiones planificadas.
- Reducción del tiempo de planificación: objetivo preliminar entre 30% y 50% respecto de la línea de base.
- Retención: objetivo preliminar entre 20% y 40% de usuarios que vuelven a usarlo para un segundo examen.

**ALTERNATIVA DATOS SINTETICOS:** si no se llega a medir estos umbrales con
trabajo de campo en esta etapa, se usan escenarios sintéticos
(conservador/intermedio/exigente) sólo para análisis de sensibilidad y ajuste
del criterio, no para validar impacto real.

### Cómo se mediría dentro del trimestre, aunque sea de forma aproximada

- Encuesta corta post-examen a usuarios de la PoC: ¿seguiste el plan? ¿cuánto
  tardaste en organizarte antes vs. con la app? ¿lo volverías a usar?

### Métrica técnica que usaríamos como proxy

- Calidad del contenido generado evaluada por rúbrica: porcentaje de
  resúmenes/ejercicios sin errores conceptuales críticos, con revisión manual
  sobre muestra. Unidad: % de piezas correctas sobre total revisado.
- Validez estructural del plan: porcentaje de planes que respetan las horas
  disponibles y cubren todos los temas ingresados. Unidad: % de planes válidos
  sobre total generado (verificable automáticamente).
- Coherencia de priorización: porcentaje de planes cuya asignación de tiempo es
  consistente con nivel declarado + cercanía de examen + objetivo del usuario,
  evaluado con checklist simple sobre muestra. Unidad: % de planes coherentes
  sobre total evaluado.

**ALTERNATIVA DATOS SINTETICOS:** si no se llega a una muestra real suficiente
en esta etapa, se puede usar un set de casos sintéticos etiquetados (planes
esperables vs. defectuosos) para probar la métrica y el validador, dejando
explícito que no sustituye validación en uso real.

**PENDIENTE DOCENTE:** confirmar si estas proxies técnicas y su nivel de detalle
cumplen con lo esperado por la consigna de la cátedra.

### Qué se registra de cada uso

Para cada plan generado: entrada del formulario, plan producido, si el usuario lo
regeneró/editó, y si cumplió las sesiones y qué resultado obtuvo en el
examen. Sin este registro el sistema no aprende de su propio funcionamiento.

### Evidencia

#### De confirmación

- El tiempo de planificación y la adherencia se pueden medir con encuesta +
  instrumentación desde el arranque, sin construir el sistema completo.

#### De refutación

- Que no exista línea de base confiable del tiempo actual de planificación
  (nadie lo mide hoy), y el umbral quede como número inventado.
- Que el "éxito" real (aprobar / mejor nota) dependa de tantos factores externos
  que no se pueda atribuir al producto dentro del trimestre.

---

## 7. Riesgos éticos y de sesgo (preliminar)

Para mantener esta sección accionable, consolidamos cada riesgo con su impacto,
grupo afectado y mitigación mínima en esta etapa:

| Tipo de riesgo | Impacto posible | Afectados principales | Mitigación propuesta |
|---|---|---|---|
| **Asignación (allocative)** | Bajo en B2C individual (no reparte recursos escasos), pero con riesgo indirecto si una institución lo usara para priorizar apoyos | Estudiantes con mayor necesidad de acompañamiento | Definir explícitamente alcance B2C; prohibir uso institucional para ranking/priorización sin evaluación específica |
| **Calidad de servicio (quality of service)** | Rendimiento desigual por materia/idioma; peor servicio en materias de nicho | Estudiantes de carreras/temas poco representados | Mostrar límites de cobertura; incorporar revisión del usuario y flag de contenido dudoso |
| **Representación (representational)** | Etiquetado/desmotivación por autoevaluación y tono de feedback | Estudiantes con baja autoconfianza o menor capital académico | Cuidar lenguaje de explicaciones; evitar juicios identitarios; centrar feedback en acciones de estudio |
| **Interpersonal y privacidad** | Exposición de datos académicos sensibles; pérdida de autonomía por sobreconfianza en el plan | Usuarios que cargan nivel, dificultades y resultados | Minimización de datos, consentimiento informado, y opción de editar/ignorar recomendaciones |
| **Social (societal)** | Dependencia de la herramienta y difusión de contenido incorrecto con apariencia confiable | Comunidad estudiantil en uso extendido | Diseñar para enseñar priorización (no sólo "dar respuesta"), e incluir revisión humana como parte del flujo |

Sobre **quién decide el sistema**, decide principalmente sobre el propio
estudiante (qué estudiar y cuándo), y potencialmente influye en terceros si ese
output se comparte.

Datos con riesgo de **proxy indebido**: autoevaluación de nivel y objetivo elegido
podrían correlacionar con trayectoria/recursos; no deben usarse para segmentar,
rankear o calificar.

**Para qué NO debería usarse:** evaluar, calificar o comparar estudiantes, ni
reemplazar el proceso de comprensión del contenido.

Cuando el sistema se equivoca (prioridad mala, ejercicio incorrecto), el usuario
debe poder detectarlo y corregirlo (revisar, editar, ignorar el plan). Esa
supervisión humana no es opcional: es una condición de diseño.

**ALTERNATIVA DATOS SINTETICOS:** como oportunidad de mejora, si no se llega a
validar estos riesgos con campo en esta etapa, se pueden construir escenarios
sintéticos de falla (por ejemplo, materia de nicho + autoevaluación sesgada +
recomendación errónea) para probar mitigaciones, dejando explícito que no
reemplaza evidencia empírica.

Regulación: educación es un dominio sensible; antes de escalar conviene revisar
normativa de protección de datos personales aplicable a estudiantes (incluyendo
casos de menores de edad).

**PENDIENTE DOCENTE:** confirmar el alcance mínimo esperado para esta sección
de ética/sesgo (formato consolidado vs. desarrollo individual por sub-tipo de riesgo).

### Evidencia

#### De confirmación

- Casos publicados de alucinaciones de LLMs generando contenido incorrecto
  con apariencia confiable (riesgo de ejercicios/resúmenes erróneos).
- Sesgo documentado de LLMs por idioma/representación en el corpus.
- Marco de protección de datos personales aplicable a datos académicos.

#### De refutación

- Que el riesgo de **asignación** no aplique en el modelo B2C individual (se
  puede descartar con fundamento).
- Que el riesgo de dependencia sea acotado si el producto se diseña para
  **enseñar a priorizar** (mostrar el porqué) en vez de sólo dar la respuesta.

---

## Bitácora de revisiones

| Fecha | Versión | Cambio | Responsable |
|---|---|---|---|
| 2026-09-25 | 1 | Versión inicial del canvas | Fede S. |
| 2026-09-29 | 2 | Revisión de consistencia; resolución de dudas #1 a #7; marcado de pendientes con docente y alternativas con datos sintéticos | Marco P. |
