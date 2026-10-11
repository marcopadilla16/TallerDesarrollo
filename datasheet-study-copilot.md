# Datasheet abreviada — Study Copilot

> **Equipo:** Padilla, Marco; Sanches, Federico
> **Caso:** Study Copilot
> **Versión:** 2 · **Fecha:** 11/10/2026
> **Muestra:** `datos/` — 14 archivos de 3 cátedras de Ing. en Sistemas (UTN FR Delta)

**Documento 3 de 4 del Hito 2**

## Cómo se lee

Sigue el cuestionario de *Datasheets for Datasets* (Gebru y otros, 2021),
reducido a quince preguntas. Las respuestas que dependen de una medición remiten
a `eda-de-viabilidad-study-copilot.md` y a las celdas de `eda-viabilidad.ipynb`;
no la repiten con otras palabras.

**Advertencia de alcance.** Por decisión de arquitectura del 11/10/2026, el
material de cada materia **lo sube el propio usuario** al pedir el plan. Por eso
esta muestra **no es insumo del producto sino banco de pruebas**: archivos
parecidos a los que un estudiante va a subir, para ejercitar el sistema antes de
tener usuarios. **No contiene el formulario del usuario**, que el canvas
identifica como el dato del que más depende el proyecto, ni ningún registro de
uso.

---

## 1. Motivación

**1. ¿Para qué se creó el dataset?**

Respuesta: no se creó para nada relacionado con este proyecto. Son documentos de
cátedra —un temario, exámenes y guías de práctica— producidos entre 2015 y 2020
para dictar y evaluar tres materias de Ingeniería en Sistemas.

El equipo los reunió en octubre de 2026 con un propósito distinto del original:
usarlos como **banco de pruebas**. El producto no mantiene un corpus —el usuario
sube su propio material— así que estos 14 archivos existen para responder una
sola pregunta: *¿el sistema puede procesar lo que un estudiante tiene a mano?*

**2. ¿Quién lo creó, y por encargo de quién?**

Respuesta: hay dos orígenes distintos y conviene no mezclarlos.

- **Las cátedras de UTN FR Delta**, para 10 de los 14 archivos. Los metadatos
  conservan autoría en 5 de ellos (`Administrador` en 3, y dos nombres propios
  de personas).
- **Estudiantes**, para los 4 restantes, que son compilaciones de preguntas
  armadas de forma colaborativa. Esos 4 concentran el **55% del volumen de
  texto** de la muestra (celda 7).

Nadie encargó la recopilación: la armó el equipo bajándola de repositorios
estudiantiles.

## 2. Composición

**3. ¿Qué representa cada instancia, y cuántas hay?**

Respuesta: **14 instancias**, una por documento. Cada una es un archivo con su
texto y sus metadatos, clasificado por carrera, materia y tipo. Por tipo: **7
exámenes**, **6 guías de práctica**, **1 temario**. En total **95 páginas** y
**158.120 caracteres** de texto extraído (celda 2).

**4. ¿Es todo lo que existe o una muestra?**

Respuesta: es una muestra, y chica. Las tres cátedras produjeron muchos más
exámenes y guías de los que están acá, y existen cientos de materias más. No es
el universo de nada: es lo que el equipo pudo juntar.

**5. Si es una muestra, ¿de qué, y es representativa?**

Respuesta: es una muestra del material que circula en **repositorios
estudiantiles** de una sola facultad, no del material de cátedra existente. No
es representativa de su fuente: la distribución entre materias es despareja
(**5**, **6** y **3** archivos) y sólo **1 de las 3** materias tiene temario,
cuando las tres lo tienen en la realidad.

Pero como banco de pruebas la pregunta relevante es otra: **¿se parece a lo que
el usuario va a subir?** Y ahí sí. Un estudiante sube lo que juntó durante la
cursada —mezcla de material oficial y resuúmenes de compañeros, algunos sin
fecha, de años distintos— que es exactamente lo que hay acá.

Lo que **no** cubre: **1** sola carrera y **1** sola institución. No hay forma de
saber si el sistema se comporta igual con vocabulario de otra disciplina.

**6. ¿Falta información?**

Respuesta: sí, y el cambio de arquitectura le cambió el sentido. **2 de 3
materias no tienen temario** (celda 3). Cuando el equipo iba a mantener el
corpus, eso era una carencia que dejaba dos materias sin poder priorizarse.
Ahora que el temario lo sube el usuario —y muchos no lo van a tener a mano— es
**el caso de prueba de «sin temario»**, que el producto tiene que saber manejar.

Lo que sí falta sin atenuante: **6 de 14** archivos sin fecha en metadatos,
**9 de 14** sin autor, ninguno con licencia declarada, y ninguno con la
ponderación de evaluación.

**7. ¿Hay errores, ruido o duplicados?**

Respuesta: menos de lo esperado en formato, y mucho en procedencia.

- Duplicados exactos: **0**. Casi-duplicados: **1 par** (los dos compendios de
  Redes, con 0,33 de solapamiento de vocabulario), que son dos revisiones del
  mismo material bajo nombres distintos (celda 10).
- Archivos ilegibles: **0**. Los **13** PDF tienen capa de texto y no requieren
  OCR (celda 4).
- **1** PDF con estructura interna malformada, que se lee igual.
- Formatos mezclados: **13** PDF y **1** TXT.
- El ruido serio es de contenido: uno de los archivos declara de sí mismo que
  «muchas están incompletas», y otros dos piden al lector que los corrija. No es
  ruido medible con un validador: es material que avisa que no es confiable.

**8. ¿Depende de recursos externos, con licencias o costos?**

Respuesta: los archivos son autocontenidos, pero **ninguno de los 14 declara
licencia ni permiso de redistribución**. Son materiales de cátedra y
compilaciones estudiantiles que hoy están en el repo sin base documentada para
estar ahí. El producto además dependerá de un servicio de LLM externo —**ChatGPT
(OpenAI) o Claude (Anthropic)**, aún sin decidir entre los dos—, con sus propios
términos de uso y costo por API, todavía sin revisar (fuente 7 del mapa).

**9. Si hay personas, ¿se puede identificar a alguien, directa o indirectamente?**

Respuesta: **sí, directamente, y está verificado.** **5 de 14** archivos exponen
el campo de autor en los metadatos, y **2 de ellos contienen nombre y apellido
reales** de personas. Además, uno de los archivos menciona a un docente por su
nombre de pila en el cuerpo del texto. La muestra **no está anonimizada**.

El Hito 2 admite entregar «un extracto anonimizado si hay datos sensibles». Hay
que limpiar los metadatos y el texto antes del próximo push.

**10. ¿Hay datos sensibles?**

Respuesta: sí, aunque de menor gravedad que en el dataset previsto. Lo sensible
acá son los nombres de docentes y autores (pregunta 9). No hay datos de
estudiantes: los exámenes son enunciados en blanco, no copias resueltas, así que
no aparecen notas ni rendimiento de nadie. El riesgo sensible fuerte —nivel por
tema, dificultades, resultado del examen— pertenece al dataset que el producto
generaría, y ese todavía no existe.

## 3. Recolección

**11. ¿Cómo se consiguió cada dato, y en qué período?**

Respuesta: descargados por el equipo de repositorios estudiantiles el
**11/10/2026**, sin contactar a ninguna cátedra. El período que **cubre** el
material es **2015-2020** según metadatos y marcas de revisión en el texto
(celda 5); **6 de 14** archivos no tienen fecha determinable. El más reciente
tiene **6 años** y el temario tiene **11**.

**12. Si es una muestra, ¿con qué criterio se eligió?**

Respuesta: por conveniencia y disponibilidad. Se eligieron tres materias de la
carrera que cursa el equipo y se tomó lo que estaba publicado y accesible, sin
muestreo sistemático ni criterio de cobertura. Eso explica tanto el desbalance
entre materias como que las tres sean del área del propio equipo.

**13. Si hay personas, ¿sabían que se recolectaban sus datos, y lo consintieron?**

Respuesta: **no**, y es un problema abierto. Los docentes cuyos nombres figuran
en los metadatos no fueron informados ni consintieron que su material se
recopilara ni se usara para alimentar un producto. No hubo recolección de datos
de estudiantes, así que esa parte no aplica.

## 4. Usos

**14. ¿Hay algo en cómo se armó que afecte sus usos?**

Respuesta: sí, cuatro cosas, todas medidas.

1. **La procedencia está mezclada.** El **55%** del texto son compilaciones de
   estudiantes, no material oficial (celda 7). Como banco de pruebas eso es una
   virtud —es lo que el usuario va a subir— pero significa que las pruebas que
   se corran encima **no dicen nada sobre material oficial**.
2. **El material es viejo:** rango 2015-2020, el más nuevo de 6 años y el
   temario de 11. Sirve para probar que el sistema muestre la fecha del material
   que usó; no sirve para probar comportamiento con programas vigentes.
3. **Cubre 1 sola carrera.** Cualquier prueba sobre esto mide el comportamiento
   con vocabulario de Ingeniería en Sistemas, y nada más.
4. **No contiene la etiqueta del producto** (celda 8), porque no hay registros de
   uso. El riesgo de *leakage* no está resuelto, está pospuesto al dataset de
   uso, donde la partición deberá ir por estudiante y por tiempo.

**15. ¿Para qué tareas no debería usarse?**

Respuesta:

- **No debe usarse como conjunto de evaluación de un modelo.** Es un banco de
  pruebas funcional: sirve para ver si el sistema procesa archivos, no para
  medir calidad de forma generalizable. Con 3 materias de 1 carrera, cualquier
  métrica mediría la cátedra.
- **No debe tomarse como evidencia de que el problema existe.** Eso depende de
  las fuentes 1 y 2, que siguen sin obtenerse.
- **No debe usarse para calibrar los umbrales de la sección 6 del canvas.** No
  hay línea de base.
- **No debe redistribuirse** hasta revisar permisos y anonimizar los metadatos.
  Que sea banco de pruebas no cambia que haya 2 nombres reales de docentes.
- **No debe servirse a un usuario como contenido de estudio.** Es material de
  prueba del equipo, de hasta 11 años de antigüedad y de otras cátedras. El
  producto le muestra al usuario lo que el usuario sube, no esto.
