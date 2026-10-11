# Hito 2 — Dataset preparado y EDA de viabilidad

**En equipo · fin de semana 4 · se entrega en el repo del equipo con el tag `hito-2`**

## Objetivo

Poner a prueba la hipótesis de datos del canvas contra datos reales y decidir, con evidencia, si el proyecto sigue, ajusta su alcance o pivota. Es la primera vez que el equipo toca el dato, y la última oportunidad barata de cambiar de problema, porque desde la semana 6 el costo de pivotar incluye una spec y, desde la 7, código.

## Qué tiene que demostrar

Que el equipo sabe con qué datos cuenta, qué les falta y cuánto pesa lo que les falta, y que la decisión que toma se sigue de eso. El lector tiene que poder reconstruir cada número del veredicto hasta la celda del notebook que lo produjo.

## Qué se entrega

Cuatro documentos de esta carpeta, en el orden en que se producen, más la muestra y el notebook.

| # | Documento | Qué decide o informa | Cuándo |
|---|---|---|---|
| 1 | [Mapa de fuentes](1-mapa-de-fuentes.md) | De qué fuentes depende el proyecto, cuáles están al alcance y qué pasó al intentar conseguirlas | Clase 3; se actualiza antes de la Clase 4 |
| 2 | [EDA de viabilidad](2-eda-de-viabilidad.md) | El nivel que el producto necesita por propiedad, lo que la muestra dio y la exposición al *leakage* | Clase 4, sobre la muestra |
| 3 | [Datasheet abreviado](3-datasheet.md) | Lo que se sabe y lo que no se sabe de la muestra, para quien la use después | Clase 4, después del EDA |
| 4 | [Veredicto](4-veredicto.md) | La decisión, sus fundamentos, la exposición al riesgo y lo que sigue | Clase 4, al cierre |

**La muestra** va en el repo, o un extracto anonimizado si hay datos sensibles, con instrucciones de cómo se obtuvo o se regenera. Es la evidencia primaria; sin ella el resto es opinión.

**El notebook** produce los números del documento 2. Corre de punta a punta sobre la muestra del repo, sin pasos manuales. Una celda por propiedad y una por búsqueda de *leakage*. Lo que no está en el notebook no cuenta como medido.

## Criterios de evaluación

- La muestra es real y verificable.
- Cada propiedad verificada tiene un número o un gráfico atrás, y cada una que no se pudo verificar tiene su riesgo cuantificado, con procedencia.
- El datasheet contesta cada pregunta que aplica, o la marca como no sabida cuando ni la documentación de la fuente ni la muestra la contestan.
- El veredicto se sigue de la evidencia. Un pivote bien justificado vale más que un «seguir» sin números.

## Si no consiguieron la muestra

Es un resultado del hito, y de los que importan. Se entregan igual el mapa de fuentes con lo que se intentó y lo que falló, el nivel por propiedad (que no depende de la muestra) y el veredicto, que en ese caso es *ajustar* o *pivotar*, con la exposición al riesgo de todo lo que no se pudo verificar.
