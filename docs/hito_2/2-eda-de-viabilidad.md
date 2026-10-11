# EDA de viabilidad

**Documento 2 de 4 del [Hito 2](README.md) · en equipo · cada número remite a una celda del notebook**

## Objetivo

Reunir la evidencia mínima para decidir si el proyecto sigue con los datos que el equipo consiguió. Se verifica cada propiedad de la calidad de los datos sobre la muestra y se compara con el nivel que el producto necesita; lo que no se puede medir se estima con procedencia; y se busca en la muestra la información que invalidaría la evaluación del modelo.

## Qué tiene que demostrar

Que cada propiedad tiene un número o un gráfico atrás, calculado por código que corre sobre la muestra del repo, y que ese número se lee contra un nivel fijado antes de mirar los datos. Lo medido y lo estimado están separados, y cada estimación dice de dónde sale.

## Alcance

Es la exploración que decide, no la que diseña. Distribuciones, correlaciones y features son la exploración profunda del Módulo 4, sobre el dataset completo y ya partido. Acá se mira solo lo que hace falta para el veredicto, y se mira antes de partir los datos, porque nada de lo que se mide entra al modelo.

---

**Equipo:**

**Muestra** (ruta en el repo):

**Notebook** (ruta en el repo):

---

## 1. Requerimientos: el nivel que el producto necesita

Se fija antes de abrir la muestra, y sale de lo que el producto tiene que hacer, para quién y cuánto cuesta equivocarse (secciones 3 y 6 del canvas). Un nivel escrito después de ver los números describe la muestra en lugar de exigirle algo. La accesibilidad no entra, porque se midió en el mapa de fuentes. No exigir más de lo que el producto necesita.

| Propiedad | Nivel que el producto necesita | De dónde sale ese nivel |
|---|---|---|
| Volumen (por caso que el producto resuelve) | | |
| Completitud (por columna) | | |
| Corrección (errores, formato, duplicados) | | |
| Vigencia (período que tiene que cubrir) | | |
| Representatividad (grupos que tienen que estar, y en qué proporción) | | |
| Confiabilidad (quién generó y verificó el dato; error de etiquetado tolerable) | | |

## 2. Resultados de la verificación

Una fila por propiedad, con el número o el gráfico que produjo el notebook y la celda que lo produjo. El volumen se cuenta por caso; la completitud, por columna y por segmento, con el porqué de lo que falta; la corrección, con duplicados, valores fuera de formato e imposibles, y una muestra chica cotejada contra el origen si se puede; la vigencia, con el período que cubre la muestra; la representatividad, comparando la composición de la muestra con la de los usuarios del producto, en un gráfico si hay más de dos grupos; la confiabilidad, con la coincidencia entre dos personas que etiquetan la misma muestra chica por separado, si hay etiquetas.

Lo que la muestra no permite medir se estima, con la cifra, su procedencia y qué haría falta para medirlo. Una estimación sin procedencia es una opinión con número.

| Propiedad | Medido o estimado | Resultado (número o gráfico) | Celda del notebook | Si es estimado, procedencia y qué haría falta para medirlo | Cumple el nivel |
|---|---|---|---|---|---|
| Volumen | | | | | |
| Completitud | | | | | |
| Corrección | | | | | |
| Vigencia | | | | | |
| Representatividad | | | | | |
| Confiabilidad | | | | | |

## 3. Exposición al *leakage*

*Leakage* es toda información que entra a las features al entrenar y no va a estar al predecir. Un modelo que la aprende pasa la evaluación y falla en uso. Se busca en la muestra antes de partir, con cinco búsquedas, y lo que se encuentra se escribe con números. Si una búsqueda no encuentra nada, el resultado es **No encontramos**, con el método; «no hay» afirma más de lo que la búsqueda prueba.

| Búsqueda | Qué se busca | Resultado (número) | Celda del notebook |
|---|---|---|---|
| La definición | Columnas que se completan después del momento en que el producto tendría que predecir | | |
| El tiempo | Si hay fecha y la etiqueta depende del momento | | |
| Los duplicados | Exactos y casi exactos | | |
| Los grupos | Varias filas de una misma persona, cliente u objeto | | |
| La generación | Cómo se produjo cada dato; se le pregunta a quien lo conoce | | |

---

*Las definiciones y los métodos de medición, en [Calidad de los datos](../../02-datos-viabilidad/conceptos/calidad-de-los-datos.md), [EDA de viabilidad](../../02-datos-viabilidad/conceptos/eda-de-viabilidad.md) y [Leakage](../../02-datos-viabilidad/conceptos/leakage.md).*
