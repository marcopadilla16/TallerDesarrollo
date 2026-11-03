---
description: Muestra una tabla con los comandos del proyecto, qué hace cada uno y cómo se usa
when_to_use: Para ver qué comandos tiene el proyecto y cuándo conviene cada uno
allowed-tools: Read, Glob
---

Mostrá los comandos de este proyecto. Respondé en español rioplatense.

1. Listá los archivos de `.claude/commands/*.md` y leé de cada uno su encabezado:
   `description`, `when_to_use` y `argument-hint`. El nombre del comando es el nombre
   del archivo. Incluí todos los que encuentres, también este: la tabla siempre sale
   de los archivos, no de memoria.
2. Mostrá una sola tabla, ordenada alfabéticamente, con estas columnas:

   | Comando | Qué hace | Cuándo conviene | Cómo se usa |

   En "Cómo se usa" poné la invocación con sus argumentos (por ejemplo,
   `/catch-up since 4fa9a47`). Si un comando no tiene alguno de esos campos, dejá
   "—" en esa celda en lugar de deducirlo.
3. Debajo de la tabla, agregá sólo esta línea: "Para sumar un comando, agregá un
   archivo en `.claude/commands/`: aparece acá solo."

No modifiques archivos.
