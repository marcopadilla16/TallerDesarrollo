# Veredicto de viabilidad

**Documento 4 de 4 del [Hito 2](README.md) · en equipo · una página · se entrega con el tag `hito-2`**

## Objetivo

Decidir si el proyecto sigue con los datos que el equipo consiguió, sigue con un alcance menor, o cambia de problema. La decisión la toma el equipo y la lee el docente como quien evalúa una inversión, con la evidencia del [EDA de viabilidad](2-eda-de-viabilidad.md) a la vista y sin tomar la palabra del equipo por el dato.

## Qué tiene que demostrar

Que la decisión se sigue de la evidencia. Cada afirmación remite a un número del EDA, lo estimado está separado de lo medido, y la salida elegida es la que esos números sostienen. Un «seguir» que no cita números se lee como una apuesta; un «pivotar» fundado se lee como el resultado que el módulo buscaba.

## Alcance

El veredicto decide sobre los datos, no sobre el modelo. Qué enfoque técnico conviene es el Módulo 3; cómo se construye el pipeline, el Módulo 4. Lo único que se adelanta es el primer paso del pipeline, porque condiciona todo lo demás.

---

**Equipo:**

**Datos sobre los que se decidió** (reales, sintéticos o los dos):

---

## 1. Decisión

Una de tres salidas, y nada más en esta sección.

| Salida | Cuándo corresponde |
|---|---|
| Seguir | Cada propiedad cumple el nivel que el producto necesita, o lo que no se pudo medir tiene un riesgo acotado y con procedencia |
| Ajustar el alcance | Los datos sostienen una parte del problema. El proyecto sigue sobre esa parte |
| Pivotar | Los datos no sostienen el problema, y conviene cambiarlo antes de construir |

Decisión:

## 2. Fundamentos

Tres líneas, cada una con un número de las partes 2 o 3 del EDA. Qué propiedades cumplen el nivel, cuáles no, y cuál pesó más en la decisión. El lector tiene que poder ir del fundamento a la celda del notebook que lo produce.

Fundamentos:

## 3. Exposición al riesgo

Lo que no se pudo medir y se estimó. Por cada propiedad estimada, la cifra del riesgo, su procedencia y qué haría falta para convertirla en una medición. Esta sección es la que distingue un veredicto fundado de uno optimista, y es la que se relee cuando algo falla en el Módulo 4.

| Propiedad estimada | Riesgo (cifra) | Procedencia de la cifra | Qué haría falta para medirla |
|---|---|---|---|
| | | | |

## 4. Consecuencias de la decisión

**Si la decisión es seguir o ajustar**, el plan del pipeline básico en tres líneas. Es el compromiso mínimo para arrancar el Módulo 4, no su diseño.

| | Plan |
|---|---|
| Obtención y conjunto de evaluación | Cómo se obtiene el dato completo y cómo se separa y se congela el conjunto de evaluación, antes de tocar las features |
| Limpieza y transformaciones | Qué necesita el dato crudo para llegar al modelo o al agente |
| Estructura final | Qué forma tiene el dataset que usa el producto |

**Si la decisión es ajustar**, además, el alcance nuevo y qué quedó afuera.

Alcance nuevo:

**Si la decisión es pivotar**, el problema nuevo y su hipótesis de datos, en las secciones 1 y 5 del [canvas](../ai-opportunity-canvas.md). La muestra, el notebook y el datasheet se entregan igual, sobre la muestra que el equipo tenía, porque son la evidencia del pivote.

Problema nuevo (referencia al canvas):

---

*Para el detalle de cada salida y la regla del conjunto de evaluación: [EDA de viabilidad](../../02-datos-viabilidad/conceptos/eda-de-viabilidad.md) y [Leakage](../../02-datos-viabilidad/conceptos/leakage.md).*
