# Hito 3 - Definición de la PoC

**En equipo · fin de semana 6 · se entrega en el repo del equipo como `definicion-de-la-poc.md`, con el tag `hito-3`**

## Objetivo

Definir el alcance real de la PoC y sus criterios de aceptación.

- Lo que no se encuentra especificado no debe construirse.
- Lo que se encuentra especificado tiene que poder construirse en tres semanas.
- En la semana 9, la PoC se valida contra los criterios de aceptación definidos en este documento.


El documento es uno solo, [`definicion-de-la-poc.md`](definicion-de-la-poc.md), y la plantilla dice qué va en cada sección.

## Plan

- Semana 5, al cierre de la Clase 5: commit de `definicion-de-la-poc.md` con el Overview, el Objetivo y el registro de la decisión del modelo, sin tag.
- Semana 6, en la Clase 6: el resto del documento, y revisión cruzada. En pares, los equipos se leen el documento en frío y lo discuten con tres preguntas (qué se puede leer de dos maneras, qué puede impedir que la PoC funcione, qué sacarían primero si perdieran una semana). No se entrega nada de la revisión; lo que surja se corrige antes del tag.
- Fin de semana 6: commit y tag `hito-3`. Versión 1 del documento.
- Semana 10: versión 2 (final), con el alcance congelado.

**Pivote.** Si algún equipo decide pivotar, reentrega los hitos 1 y 2 junto con el 3, sin eliminar los tags anteriores, con los tags `hito-1.1`, `hito-2.1`, etc.

## Criterios de evaluación

Son los del hito; los criterios de aceptación de la parte 2 son los de la PoC. Un chequeo por parte del documento.

1. **Propuesta.** El Objetivo dice qué supuesto pone a prueba y de qué riesgo es, qué lo da por demostrado y qué decisión habilita; el Overview describe la PoC y sostiene su alcance con la cifra del EDA y los fundamentos del veredicto del Hito 2; el fuera de alcance tiene al menos un ítem con su motivo; hay 2 o 3 riesgos con su origen, su cifra o motivo y un plan B ejecutable.
2. **Spec.** El *happy path*, de 3 a 5 casos borde y el error del sistema están escritos como escenarios (dado, cuando, entonces); la user experience dice qué ve el usuario en el peor caso borde y cómo sigue; los criterios de aceptación tienen sus cuatro filas con todas las columnas (la de ventaja sobre el *baseline* solo si lo que se construye no es el *baseline*), y un tercero puede chequear cada una con sí o no, sin interpretar.
3. **Diseño.** Están los cinco registros de decisión (modelo, datos, workflow o agente, construir o usar hecho, requerimientos no funcionales), y cada uno evalúa al menos dos alternativas, dice por qué se descartó cada una, qué inclinó la decisión y qué se asume y qué se resigna; el del modelo tiene al *baseline* entre sus alternativas. La arquitectura nombra las cinco piezas y dice cuál se construye y cuál se usa hecha (y las herramientas, si hay un agente).
4. **Plan.** Cubre las semanas 7, 8 y 9 con responsable y demostración al cierre, con el *baseline* de punta a punta en la 8, y entra en tres semanas con este equipo.

**Peso.** Es el tercero de los cuatro hitos entre los que se distribuye el Proyecto Integrador, que vale el 40 % de la nota final.


