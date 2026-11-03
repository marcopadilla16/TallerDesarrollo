---
description: "Lee un documento en frío y responde las 3 preguntas de la revisión cruzada, sin reescribir nada. Usar antes de la revisión cruzada con otro equipo, o antes de cerrar una versión de un documento."
argument-hint: "[ruta del documento]"
agent: "agent"
tools: [read, search]
---

Hacé una lectura en frío del documento que se indicó al invocar este comando.

Si no se indicó ninguno, usá `docs/hito_3/definicion-de-la-poc.md`. Respondé en
español rioplatense. No modifiques archivos.

**En frío quiere decir** que juzgás sólo lo que está escrito. Ignorá lo que sepas del
proyecto por esta u otras conversaciones y no leas otros documentos para entender
este: si algo no se entiende sin ayuda, es un hallazgo. Sí podés abrir un archivo que
el documento cite, para comprobar que existe y dice lo que el documento afirma. Para
que la lectura sea realmente en frío, conviene correrlo en un chat nuevo.

## Las tres preguntas de la revisión cruzada

Son las del enunciado del Hito 3 (`docs/hito_3/README.md`):

1. **¿Qué se puede leer de dos maneras?** Texto del que dos personas podrían sacar
   conclusiones distintas: términos sin definir, umbrales que hay que interpretar,
   criterios que un tercero no podría chequear con sí o no.
2. **¿Qué puede impedir que la PoC funcione?** Supuestos sin evidencia, dependencias
   sin plan B, cosas que el documento da por hechas.
3. **¿Qué sacarían primero si perdieran una semana?** Elegí una sola cosa y justificala
   con lo que el propio documento dice que es central y lo que no.

## Cómo responder

- Una tabla por cada una de las preguntas 1 y 2: sección o línea, cita textual breve,
  y por qué es un problema.
- Para la pregunta 3: lo que sacarías y el motivo, en dos o tres oraciones.
- Al final, los 3 hallazgos más graves, con la pregunta que el equipo tiene que
  responder para resolver cada uno.
- Las secciones todavía vacías o marcadas "Pendiente" no se evalúan: listalas en una
  línea. Lo que importa es lo escrito.
