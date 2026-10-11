# Veredicto de viabilidad — Study Copilot

> **Equipo:** Padilla, Marco; Sanches, Federico
> **Caso:** Study Copilot
> **Versión:** 3 · **Fecha:** 11/10/2026

**Documento 4 de 4 del Hito 2**

**Datos sobre los que se decidió:** reales. Un **banco de pruebas** de **14
archivos** de **3 cátedras** de Ing. en Sistemas (UTN FR Delta) en `datos/`,
abierto e inspeccionado archivo por archivo con `eda-viabilidad.ipynb`.

Por decisión de arquitectura del 11/10/2026, el material de cada materia **lo
sube el usuario** al pedir el plan: el equipo no mantiene un corpus. El banco
sirve para ejercitar el sistema, no para alimentarlo.

---

## 1. Decisión

| Salida | Cuándo corresponde |
|---|---|
| Seguir | Cada propiedad cumple el nivel que el producto necesita, o lo que no se pudo medir tiene un riesgo acotado y con procedencia |
| **Ajustar el alcance** | Los datos sostienen una parte del problema. El proyecto sigue sobre esa parte |
| Pivotar | Los datos no sostienen el problema, y conviene cambiarlo antes de construir |

**Decisión: Ajustar el alcance.**

El banco de pruebas alcanza para construir y ejercitar el sistema. Lo que no
alcanza es para prometer la **priorización por peso real de los temas** ni
cualquier afirmación sobre resultado académico. El proyecto sigue sobre lo
primero.

> **Por qué no *Seguir*, aunque ahora 5 de 6 propiedades cumplan.** Ese 5 de 6
> no se ganó consiguiendo mejores datos: se ganó cambiando lo que el producto
> necesita. Los 14 archivos son los mismos que con la vara anterior daban 1 de
> 6. Tomar ese salto como licencia para «Seguir» sería exactamente la escalada
> del compromiso contra la que advierte el canvas. Quedan además dos faltantes
> que **ningún** cambio de arquitectura toca: la representatividad sigue
> fallando (1 sola carrera) y la calidad del contenido generado sigue sin
> medirse.

No es *Pivotar*: el cambio de arquitectura eliminó el obstáculo más grande —no
hace falta conseguir ni mantener un corpus de cátedras— y el material resulta
procesable.

## 2. Fundamentos

1. **El banco cubre los casos de entrada que el producto va a recibir.** **14**
   archivos, **3** materias, **3** tipos de documento, **2** formatos, **2**
   orígenes (cátedra y estudiante), **1** materia con temario y **2** sin
   (celdas 2 y 3). Y son procesables: **13 de 13** PDF con capa de texto, **0**
   ilegibles, **0** duplicados exactos (celda 4). Esto sostiene construir.
2. **La representatividad sigue fallando, y el cambio de arquitectura no la
   toca.** **1** carrera, **1** institución, **0** materias fuera del área del
   equipo (celda 6). No hay forma de saber si el sistema se comporta igual con
   vocabulario de otra disciplina, y el riesgo de calidad de servicio despareja
   de la sección 7 del canvas sigue sin poder medirse. Es el fundamento que más
   pesa para no decir «Seguir».
3. **Falta temario en 2 de 3 materias, y eso ahora informa el alcance en vez de
   bloquearlo.** Si el usuario no sube temario —y según el banco, dos de cada
   tres veces no lo va a tener— el producto no puede priorizar por peso real de
   los temas. Puede priorizar por nivel declarado, fecha y horas, que es menos
   de lo que el canvas prometía. Por eso el alcance se ajusta.

Un dato que cambió de signo y conviene no esconder: el **55%** del volumen de
texto son compilaciones de estudiantes (celda 7). Con la arquitectura anterior
era el peor hallazgo del EDA —material de fidelidad no verificada— y con la
nueva es **cobertura realista**, porque es lo que un estudiante tiene a mano y va
a subir. El número es el mismo; lo que cambió es qué significa.

Cada número remite a una celda de `eda-viabilidad.ipynb`, que corre de punta a
punta sobre `datos/`.

## 3. Exposición al riesgo

| Propiedad estimada | Riesgo (cifra) | Procedencia de la cifra | Qué haría falta para medirla |
|---|---|---|---|
| **Corrección conceptual del contenido generado** | **No estimado.** Riesgo central de la sección 7 del canvas: el producto generará contenido a partir de material que en el banco es **55%** de fidelidad no verificada | El 55% está medido (celda 7); lo que no se midió es cuánto error conceptual produce el modelo a partir de eso | Rúbrica con 2 revisores independientes sobre ≥50 piezas generadas, con acuerdo ≥80% |
| **Comportamiento fuera de Ing. en Sistemas** | **No estimado.** **1** carrera y **1** institución en el banco | El número está medido (celda 6); la extrapolación a otras áreas no tiene base | Agregar al banco material de ≥1 carrera fuera del área del equipo |
| **Qué sube realmente el usuario** | **No estimado.** El banco lo armó el equipo **eligiendo** qué incluir, así que no dice nada sobre la tasa de archivos ilegibles, de otra materia, o vacíos que llegarán en uso | Sin procedencia: la fuente 2 del mapa sigue sin obtenerse | Una prueba de uso donde los archivos los elija el usuario y no el equipo |
| **Completitud del feedback posterior** | **No estimado.** La métrica de negocio de la sección 6 del canvas depende por completo de esta columna | Sin procedencia: la fuente 6 sigue sin obtenerse | Una prueba de uso con seguimiento post-examen |
| **Completitud del formulario** | Riesgo bajo: **0%** de campos vacíos esperado | Garantía de diseño (sección 3 del canvas), no observación | Instrumentar el formulario y contar campos vacíos sobre planes reales |
| **Permisos de redistribución** | **14 de 14** archivos sin licencia declarada. Riesgo legal **no cuantificado** | Medido: inspección de los 14 archivos | Consultar a las cátedras y a la facultad por condiciones de uso |
| **Datos personales expuestos** | **5 de 14** archivos con autoría en metadatos, **2** con nombre real | Medido (celdas 7 y 12) | Ya está medido. Lo que falta no es medirlo sino **anonimizarlo** |

**Lectura de esta tabla:** el cambio de arquitectura **agregó** una fila de
riesgo en vez de sacarla. Al mover el material al usuario, aparece algo que
antes no existía: no sabemos qué va a subir. El banco no lo responde, porque lo
armó el equipo eligiendo qué incluir.

## 4. Consecuencias de la decisión

### Plan del pipeline básico

| | Plan |
|---|---|
| **Obtención y conjunto de evaluación** | El material **no se obtiene: llega en cada pedido**. El pipeline arranca con un paso de ingesta que acepta el archivo del usuario, extrae texto y rechaza lo que no puede leer. `datos/` queda como banco de pruebas de ese paso, nunca como conjunto de evaluación de un modelo. Los datos de uso nacen con la PoC: se instrumenta el formulario y el registro de eventos antes de la primera prueba, y el conjunto de evaluación se separa **por estudiante y por fecha de examen**, nunca por fila |
| **Limpieza y transformaciones** | Extracción de texto por archivo subido (en el banco, 13 de 13 PDF la tienen; hay que decidir qué pasa con un escaneado sin capa de texto), detección del par de casi-duplicados si el usuario sube dos versiones del mismo material, y **extracción de la fecha del documento** para poder mostrarla. En el banco, 6 de 14 no la tienen: ese camino hay que resolverlo |
| **Estructura final** | Por pedido: el formulario, la lista de archivos subidos con su texto y su fecha cuando se pueda determinar, y el plan generado. El feedback posterior va en tabla aparte, unida sólo después de congelar la evaluación, para que nunca entre como feature |

### Alcance nuevo

El proyecto sigue sobre **generar el plan y el material de estudio a partir de lo
que el usuario sube**, que es lo que el banco de pruebas sostiene.

- **Se mantiene:** generar el plan a partir del formulario con su explicación, y
  medir el % de planes que respetan las horas declaradas y cubren todos los
  temas ingresados.
- **Se mantiene, con dos condiciones:** el material complementario se genera
  apoyado en los archivos del usuario, **mostrando siempre la fecha del material
  usado** —y avisando cuando no se pudo determinar, que en el banco es 6 de 14—
  y **con revisión humana**.
- **Se agrega al alcance:** el camino de error. Qué hace el producto si el
  usuario no sube nada, sube un escaneado ilegible o sube material de otra
  materia. Antes no existía como problema; ahora es parte del producto.

**Qué queda afuera:**

- **Priorizar por peso real de los temas.** Requiere temario, y según el banco
  dos de cada tres veces el usuario no lo va a tener. La priorización se apoya
  en nivel declarado, fecha y horas, que es menos de lo que el canvas prometía.
  Hay que ajustar la sección 3 del canvas para no prometer de más.
- **Materias fuera de Ing. en Sistemas.** El banco cubre **1** carrera.
- Toda afirmación sobre **mejora del resultado académico**. Sin línea de base.
- Los **umbrales de la sección 6 del canvas** (adherencia 50-70%, reducción del
  tiempo de planificación 30-50%, retención 20-40%), suspendidos como criterio
  de éxito hasta que exista línea de base.

### Lo primero que tiene que pasar

1. **Anonimizar la muestra antes del próximo push.** 5 archivos exponen autoría
   en metadatos y 2 traen nombre real de persona. El Hito 2 admite entregar un
   extracto anonimizado; hoy lo que está en el repo no lo es.
2. **Revisar permisos de redistribución.** 14 de 14 archivos sin licencia
   declarada. Es la condición para que el banco pueda quedarse donde está.
3. **Definir qué hace el producto sin temario.** Según el banco es el caso
   mayoritario (2 de 3 materias), y hoy no está resuelto. Ya no se trata de
   conseguir los temarios faltantes: los sube el usuario, o no los sube.
4. **Elegir entre ChatGPT y Claude, y fijar la versión del modelo** (fuente 7).
   El proveedor ya está acotado a esos dos; falta decidir cuál, leer los
   términos de uso de ambos y probar salidas contra el banco. Es lo que destraba
   medir la calidad del contenido generado.
5. **Agregar al banco material de al menos 1 carrera fuera de Ing. en
   Sistemas.** Es el único incumplimiento que sobrevivió al cambio de
   arquitectura, y es barato de resolver.
