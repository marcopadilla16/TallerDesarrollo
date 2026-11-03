---
description: Resumen del estado del proyecto Study Copilot contra los entregables de cada hito
allowed-tools: Bash(git status:*), Bash(git log:*), Bash(git tag:*), Bash(git fetch:*), Bash(git diff:*), Bash(ls:*), Read, Glob, Grep
---

Hacé un catch-up del proyecto Study Copilot para alguien que no recuerda en qué
estaba. Respondé en español rioplatense, como el resto del repo.

## 1. Relevá los entregables previstos

Los enunciados de la cátedra son la fuente de verdad de qué hay que entregar,
cuándo y con qué criterios:

- `docs/hito_*/README.md` y `docs/hito_*/ENUNCIADO.md` (el Hito 1 sólo tiene la
  plantilla del canvas en PDF).
- Si aparece un enunciado de un hito nuevo, incluilo.

De cada hito anotá: qué archivos se entregan, el tag que lleva, las fechas o
semanas que fija el enunciado, y los criterios de evaluación.

## 2. Relevá el estado real

- Git: `git fetch -q`, `git status -sb`, `git log --oneline -15
  --date=short --format="%h %ad %an %s"`, `git tag -l`. Distinguí lo
  commiteado, lo modificado sin commitear y lo que está en el remoto.
- Para cada entregable, abrí el archivo y verificá contra el enunciado:
  qué secciones están escritas y cuáles siguen vacías o dicen "Pendiente";
  qué criterio de evaluación cumple cada una y cuál no.
- Coherencia entre documentos: versión y bitácora de `canvas.md`, la sección
  "Estado actual" y "Pendientes conocidos" del `README.md` raíz, y si algún
  documento contradice a otro (por ejemplo, el canvas contra el veredicto o
  contra la definición de la PoC).
- Experimentos: si hay resultados en `experimentos/resultados/`, resumí la
  última corrida (modelo, fecha, tabla de resumen). Si no hay, decí que la
  prueba no se corrió.

## 3. Escribí el catch-up

Con estas tres secciones, en este orden:

**¿Qué hicimos?** Una tabla por hito: qué se entregó, tag o commit, y el
resultado clave (por ejemplo, la decisión del veredicto).

**¿En qué estamos?** El hito en curso: qué está hecho, qué falta contra el
enunciado, y lo que está modificado sin commitear. Incluí el calendario: qué
fecha fija el enunciado y si ya pasó.

**¿Cómo seguimos?** Los próximos pasos en orden, con lo que bloquea a cada
uno, y las preguntas que necesitás que el equipo responda.

## Reglas

- Cada afirmación sale de un archivo o de git; citá el archivo con un enlace
  relativo. No inventes fechas: si una fecha de entrega no está en el repo,
  decí que no se conoce y pedila. Las fechas que no salen del repo (por
  ejemplo, una prórroga) pueden estar en la memoria del proyecto: usalas
  diciendo de dónde salen.
- Separá lo verificado de lo inferido (por ejemplo, la semana del curso
  calculada a partir de las fechas de los commits).
- Sé breve: el catch-up se lee en dos minutos. Nada de repetir el contenido
  de los documentos; sólo su estado.
- No modifiques archivos ni hagas commits: este comando sólo informa.

$ARGUMENTS
