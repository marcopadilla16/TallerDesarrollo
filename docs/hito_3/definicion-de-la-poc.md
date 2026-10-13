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

*Pendiente (Clase 6).*

### 1.4 Riesgos

*Pendiente (Clase 6).*

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

*Pendiente.*

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
