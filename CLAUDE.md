# Reglas de trabajo del repo

Valen para cualquier modificación de este repo, la haga quien la haga.

## Una modificación no puede romper la coherencia de los documentos

Un cambio no está terminado hasta verificar que no deja contradicciones:

1. **En el propio documento.** Encabezado, versión, resúmenes y cualquier otra
   sección que dependa de lo cambiado.
2. **En el resto del repo.** Buscar el término, la cifra o la decisión que cambió, y
   revisar cada lugar donde aparece. Los cruces más frecuentes:
   - `canvas.md`, contra el veredicto del Hito 2 y `docs/hito_3/definicion-de-la-poc.md`.
   - `README.md`: "Estado actual", "Pendientes conocidos" y la estructura del repo.
   - Las cifras de los documentos, contra el notebook o `experimentos/resultados/`.
3. **Corregir lo que se rompió.** Si la corrección requiere una decisión del equipo,
   no resolverla por cuenta propia: avisar qué quedó inconsistente.
4. **Decir qué se revisó y qué se encontró**, también cuando no se encontró nada.

## Lo superado se marca, no se borra

Si una decisión o una cifra deja de valer (por ejemplo, un umbral), se conserva
marcada como suspendida, con el motivo y una referencia al documento que la
reemplaza. El historial de lo que el equipo pensó también se evalúa.

Las marcas de trabajo, como un pendiente que ya se resolvió, sí se pueden quitar,
dejando constancia en la bitácora o el historial del documento.

## En un hito cerrado se corrigen errores, no decisiones

Los documentos de `docs/hito_1/` y `docs/hito_2/` registran lo que se sabía al
entregarlos.

- **Errores de hecho** (una referencia rota, un campo vacío, una cifra que no se
  reproduce): se corrigen en el documento y se sube su versión. Van como commits del
  hito en curso, sin tags nuevos, con un comentario que diga qué se corrige y por qué.
  Se registran en `docs/decisiones-de-proceso.md`.
- **Lo que quedó superado después** (por ejemplo, que el proveedor todavía no estaba
  elegido): no se reescribe. Se deja constancia en un documento vivo (`canvas.md`,
  `README.md`, la definición de la PoC).

`docs/hito_3/definicion-de-la-poc.md` sigue abierto hasta el tag `hito-3`.
