# EDA de viabilidad — Study Copilot

> **Equipo:** Padilla, Marco; Sanches, Federico
> **Caso:** Study Copilot
> **Versión:** 3 · **Fecha:** 11/10/2026
> **Muestra** (ruta en el repo): `datos/` — 14 archivos de 3 cátedras de Ing. en Sistemas (UTN FR Delta)
> **Notebook** (ruta en el repo): `eda-viabilidad.ipynb` — corre de punta a punta sobre `datos/`

---

## 1. Requerimientos: el nivel que el producto necesita

Fijado antes de abrir cualquier muestra, a partir de lo que el producto tiene
que hacer (canvas, sección 3), para quién (sección 2) y cuánto cuesta
equivocarse (secciones 6 y 7). La accesibilidad no entra: se midió en el mapa de
fuentes. No se exige más de lo que el producto necesita.

El producto resuelve dos casos, y el nivel se fija por caso:

- **Caso A — generar un plan de estudio** a partir del formulario.
- **Caso B — generar material complementario** (resumen, ejercicios, preguntas)
  para un tema del plan, apoyado en los archivos que el usuario sube.

La tabla conserva las dos columnas de nivel. La primera es la que se fijó antes
de abrir la muestra. La segunda es la que rige después de la decisión de
arquitectura del 11/10/2026, y aplica al **banco de pruebas**, que es lo que
`datos/` realmente es. Cuando las dos coinciden, la segunda dice «igual».

| Propiedad | Nivel original (corpus propio) | Nivel vigente (banco de pruebas) | De dónde sale el nivel vigente |
|---|---|---|---|
| **Volumen** | **Validación del problema:** 10-20 encuestas y 6-8 entrevistas. **Caso A:** ≥30 planes sobre ≥3 materias. **Caso B:** ≥50 piezas revisadas. **Feedback:** ≥20 respuestas | **Validación del problema, Caso A, Caso B y feedback: igual.** Para el banco se agrega: al menos **1 materia con temario y 1 sin temario**, ≥2 materias y los 3 tipos de documento | Un banco de pruebas no necesita volumen, necesita **cobertura de casos**. Como el temario ahora lo sube el usuario, el caso «no subió temario» es tan probable como el otro y hay que poder ejercitarlo |
| **Completitud** | **100%** en los seis campos del formulario. **≥50%** de respuesta en el feedback | **Formulario y feedback: igual.** Para el banco: que estén representadas las combinaciones que el producto va a recibir (con y sin temario, con y sin fecha legible) | Lo que el producto necesita completo es el formulario, que controla. Sobre lo que el usuario sube no puede exigir nada: tiene que **tolerar** la falta, no requerir la presencia |
| **Corrección** | Fecha válida y futura: **100%**. Horas en rango: **100%**. Nivel en {bajo, medio, alto}: **100%**. Duplicados exactos: **0** | **Igual** para el formulario. Para el banco: **100%** de los archivos procesables (con capa de texto o declarados como no procesables), y al menos **1 archivo con defecto** para probar el manejo de error | El producto tiene que poder leer lo que recibe. Un archivo malformado en el banco no es un defecto del banco: es el caso de prueba que falta cuando todo viene limpio |
| **Vigencia** | Temarios **≤1 año**. Parciales **≤3 años**. Feedback **≤7 días** | **Feedback: igual (≤7 días).** Para el material: **no hay nivel exigible**. Para el banco se exige lo contrario: **variedad temporal**, incluyendo al menos un archivo sin fecha determinable | **Cambió de dueño.** El usuario sube el material de su cursada, y el producto no puede exigirle actualidad. Lo que sí puede es **mostrar la fecha del material** que usó, y para probar eso el banco necesita casos viejos y casos sin fecha |
| **Representatividad** | **2** carreras, **3** materias, **1** fuera del área del equipo, niveles bajo/medio/alto ≥15%, participantes externos ≥50% | **Para el banco:** variedad de **formatos y orígenes** (≥2 formatos, ≥2 orígenes distintos: cátedra y estudiante) y ≥1 carrera fuera del área del equipo. Lo demás aplica a los participantes del estudio, no al banco | Un banco de pruebas no representa una población, representa **la variedad de entradas**. La exigencia de carreras se mantiene pero bajada a 1 externa: sin eso no sabemos si el sistema se rompe con vocabulario de otra disciplina |
| **Confiabilidad** | Nivel por tema: percepción declarada. Rúbrica: **2 revisores**, acuerdo **≥80%** | **Rúbrica: igual.** Para el banco se invierte la exigencia: tiene que **incluir** material de fidelidad dudosa, porque es lo que el usuario va a subir | Si el banco fuera todo material oficial impecable, las pruebas no dirían nada sobre el caso real. El material compilado por estudiantes deja de ser contaminación y pasa a ser **cobertura** |

> Las filas de **vigencia**, **representatividad** y **confiabilidad** son las
> que más se movieron, y conviene mirarlas con desconfianza: son exactamente las
> tres que la muestra no cumplía. El argumento de por qué el cambio es legítimo
> está en la advertencia metodológica de arriba; si el lector no lo compra, la
> columna del nivel original queda para que pueda evaluar con la vara vieja.

## 2. Resultados de la verificación

Cada número sale de una celda de `eda-viabilidad.ipynb`. Los números **no
cambiaron** respecto de la versión anterior: lo que cambió es la vara contra la
que se leen. La última columna da las dos lecturas para que se vea cuáles
volteó el cambio de arquitectura y cuáles no.

| Propiedad | Medido o estimado | Resultado (número o gráfico) | Celda | Si es estimado, procedencia y qué haría falta | Cumple (nivel original → vigente) |
|---|---|---|---|---|---|
| **Volumen** | **Medido** | **14** archivos, **95** páginas, **158.120** caracteres, **3** materias, **1** carrera. Por tipo: **7** exámenes, **6** prácticas, **1** temario. Materias con temario: **1**; sin temario: **2**. Planes generados: **0**. Encuestas: **0**. Feedback: **0** | Celda 2 | El tramo no medido (planes, encuesta, feedback) no se estima: no hay procedencia. Hace falta la PoC y una prueba de uso | **No → Sí, como banco.** Cubre los 3 tipos, 3 materias, y tiene el caso con temario y el caso sin temario. **Sigue siendo No** para el producto: 0 planes y 0 encuestas |
| **Completitud** | **Medido** | **1 de 3** materias con temario. Con fecha en metadatos: **6 de 14**. Con autor: **5 de 14**. Texto vacío: **0 de 14** | Celda 3 | — | **No → Sí.** Lo que antes era la carencia principal —faltan 2 temarios— ahora es cobertura: el producto tiene que funcionar sin temario, y el banco permite probarlo |
| **Corrección** | **Medido** | Duplicados exactos: **0**. PDFs sin capa de texto: **0 de 13**. PDFs malformados: **1 de 13** (`investigacion_operativa/examenes/examen_02.pdf`). Formatos: **13** PDF y **1** TXT | Celda 4 | La corrección **conceptual** de lo generado sigue **No estimada**: el proveedor está acotado a ChatGPT o Claude, pero no se probó ninguno contra este material | **Sí → Sí.** No cambió. El PDF malformado, que antes era un defecto, ahora es el caso de prueba de manejo de error |
| **Vigencia** | **Medido** | Rango **2015-2020**. Más reciente: **6 años**. Temario: **11 años**. Sin fecha determinable: **6 de 14** | Celda 5 | — | **No → Sí, como banco.** Deja de ser incumplimiento porque el usuario sube su material. El banco tiene la variedad temporal que hacía falta, incluidos **6** archivos sin fecha, que es el caso difícil |
| **Representatividad** | **Medido**, con gráfico | Carreras: **1**. Materias: **3**. Fuera del área del equipo: **0**. Instituciones: **1**. Formatos: **2**. Orígenes distintos: **2** (cátedra y estudiante). Distribución: **5, 6 y 3** archivos por materia | Celda 6 | La distribución de niveles autoevaluados pertenece al formulario, que no se obtuvo | **No → No.** Cumple en formatos y orígenes, **falla en el requisito de ≥1 carrera externa**. Es el único incumplimiento que sobrevive al cambio de arquitectura |
| **Confiabilidad** | **Medido** | **4 de 14** archivos declaran en su propio texto ser compilaciones de estudiantes: **55%** del volumen de texto (87.361 de 158.120). Revisores: **0**. Nombres de persona en metadatos: **5 de 14** | Celda 7 | — | **No → Sí.** La fila que más cambia de signo: si el usuario sube lo que tiene a mano, el material compilado por compañeros **es** el caso real. Un banco sólo con material oficial probaría menos |

**Resumen: con la vara vigente, 5 de 6** propiedades cumplen como banco de
pruebas, contra **1 de 6** con la vara original. Conviene decirlo con todas las
letras: **ese salto no viene de haber conseguido mejores datos, viene de haber
cambiado lo que el producto necesita**. Los 14 archivos son los mismos.

Lo que **no** se movió con el cambio, y por eso es lo que vale:

- **Representatividad sigue fallando.** 1 sola carrera. No sabemos qué pasa con
  vocabulario de Derecho, Medicina o Letras, y el riesgo de calidad de servicio
  despareja de la sección 7 del canvas sigue sin poder medirse.
- **La calidad del contenido generado sigue sin medirse.** Ningún modelo se
  probó contra este material.
- **La muestra sigue sin anonimizar** y **sin permisos**. Que sea banco de
  pruebas no cambia que haya 2 nombres reales de docentes en los metadatos.

## 3. Exposición al *leakage*

Las cinco búsquedas se ejecutaron sobre la muestra. Con el cambio de
arquitectura, buena parte de esta sección **pierde filo**: si el banco no se usa
para entrenar ni para evaluar un modelo —el LLM viene preentrenado y el material
lo aporta el usuario en uso— entonces no hay partición que contaminar. Se deja
completa igual, porque los riesgos reaparecen en cuanto se arme el dataset de
uso.

| Búsqueda | Qué se busca | Resultado (número) | Celda |
|---|---|---|---|
| **La definición** | Columnas que se completan después del momento en que el producto tendría que predecir | **No encontramos.** Archivos que sean registro de uso: **0 de 14**. Método: inspección archivo por archivo (celda 1). **El riesgo no desaparece, se pospone:** el feedback de resultado será una columna posterior a la predicción en el dataset de uso | Celda 8 |
| **El tiempo** | Si hay fecha y la etiqueta depende del momento | **6 de 14** sin fecha determinable; rango **2015-2020**. Sin etiqueta no hay dependencia temporal que medir. Como banco, esos 6 archivos son el caso de prueba de «material sin fecha», que el producto va a recibir seguido | Celda 9 |
| **Los duplicados** | Exactos y casi exactos | Exactos: **0**. Casi-duplicados: **1 par** — los dos compendios de Redes, Jaccard **0,33**, dos revisiones del mismo material (08/2017 y 02/2020). Como banco es útil: prueba que el sistema no cuente dos veces el mismo contenido si el usuario sube ambos | Celda 10 |
| **Los grupos** | Varias filas de una misma persona, cliente u objeto | **3 grupos** por materia (**5**, **6**, **3** archivos). **Ya no condiciona una partición**, porque no se entrena nada con esto. Sí condiciona el dataset de uso, donde la unidad será el **estudiante** y la partición tendrá que respetarla | Celda 11 |
| **La generación** | Cómo se produjo cada dato; se le pregunta a quien lo conoce | **5** productores de PDF distintos, **1 de 14** sin metadato de productor. **A nadie se le preguntó:** los archivos se bajaron de repositorios estudiantiles sin contactar cátedras. Para un banco de pruebas alcanza; para afirmar que son las versiones oficiales, no | Celda 12 |

**Lo que queda en pie para el Módulo 4:** cuando exista el dataset de uso, la
partición va **por estudiante y por tiempo**, y el feedback de resultado nunca
puede entrar como feature. Eso no lo probó esta muestra —no podía— pero es la
restricción que hay que respetar.
