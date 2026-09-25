# Proyecto: Study Copilot

Study Copilot es una plataforma que utiliza modelos de lenguaje (LLMs) para generar planes de estudio personalizados a partir de la situación académica de cada estudiante. El usuario ingresa información sobre materias, temas, fechas de examen, disponibilidad horaria y objetivos, y el sistema genera un plan de estudio adaptado. Además, puede solicitar materiales complementarios como resúmenes, ejercicios tipo parcial, preguntas de autoevaluación y mapas conceptuales.

## El verdadero problema

Los estudiantes suelen tener:

* Mucho material.
* Poco tiempo.
* Muchas materias simultáneas.
* Dificultad para organizar prioridades.

Cuando llega un examen, la pregunta siempre es:

> "Tengo 5 días para rendir, ¿qué estudio?"

o

> "Tengo 2 horas libres hoy, ¿cómo las aprovecho?"

La respuesta suele depender de muchos factores difíciles de evaluar rápidamente.


## Solución

El usuario completa un formulario con:

### Materia

Ejemplo:

* Álgebra

### Temas

* Matrices
* Determinantes
* Autovalores

### Fecha del examen

15/11/2026

### Nivel actual

* Matrices: Alto
* Determinantes: Medio
* Autovalores: Bajo

### Tiempo disponible

* Lunes: 2 horas
* Martes: 3 horas
* Miércoles: 1 hora

### Objetivo

* Aprobar
* Sacar más de 8
* Preparar final


## Salida del sistema

El LLM genera automáticamente:

### Plan sugerido

Lunes
- Matrices: 30 min
- Autovalores: 90 min

Martes
- Autovalores: 120 min
- Determinantes: 60 min

Miércoles
- Repaso general: 60 min


Además explica: Se priorizaron Autovalores porque el usuario se
autoevaluó con un nivel bajo y es un tema
fundamental para el examen.


## Funcionalidad diferencial

Además de generar el plan, el usuario puede seleccionar qué contenido adicional desea.

* Resumen
* Ejercicios tipo parcial
* Preguntas de autoevaluación