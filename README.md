# Study Copilot

Trabajo práctico de **Taller de Desarrollo** — Maestría en Inteligencia Artificial, 3.er trimestre.

**Equipo:** Padilla, Marco · Sanches, Federico

---

## De qué se trata

Plataforma que genera **planes de estudio personalizados** a partir de la
situación académica de cada estudiante. El usuario carga materia, temas, fecha
de examen, nivel autoevaluado por tema, tiempo disponible y objetivo, sube el
material de la cursada, y el sistema devuelve un cronograma priorizado con la
explicación de por qué priorizó cada tema. Opcionalmente genera resúmenes,
ejercicios tipo parcial y preguntas de autoevaluación.

El repositorio documenta el recorrido del proyecto **por hitos**: primero se
formulan las hipótesis (problema, solución, datos) y después se las contrasta
con datos reales para decidir si el proyecto sigue, ajusta su alcance o pivota.
Todavía no contiene código del producto.

## Estado actual

| Entrega | Contenido | Referencia |
|---|---|---|
| #1 | Propuesta y AI Opportunity Canvas (v2) | Tag `v1.0` |
| #2 | Mapa de fuentes | Commit `2e69bc9` (sin tag) |
| #3 | Hito 2: muestra, EDA de viabilidad, datasheet y veredicto (**decisión: ajustar el alcance**). Canvas actualizado a v3 | Esta entrega |

**En una línea:** el EDA mostró que el material disponible alcanza para construir
y probar el sistema, pero no para priorizar temas por su peso real (2 de 3
materias no tienen temario) ni para generalizar fuera de Ing. en Sistemas. Se
decidió además que el material lo sube el usuario, por lo que `datos/` funciona
como **banco de pruebas**, no como corpus del producto. Detalle en el
[veredicto](docs/hito_2/4-veredicto.md).

## Orden de lectura sugerido

Los documentos se leen en el orden en que se produjeron; cada uno se apoya en el
anterior.

| # | Documento | Qué responde |
|---|---|---|
| 1 | [propuesta.md](propuesta.md) | Qué es Study Copilot y qué problema ataca |
| 2 | [canvas.md](canvas.md) | Hipótesis de problema, solución, datos, métricas y riesgos. Incluye historial de versiones al final |
| 3 | [Mapa de fuentes](docs/hito_2/1-mapa-de-fuentes.md) | Qué datos necesita el proyecto y qué pasó al intentar conseguirlos |
| 4 | [EDA de viabilidad](docs/hito_2/2-eda-de-viabilidad.md) | Nivel exigido vs. nivel medido por propiedad, y búsqueda de *leakage* |
| 5 | [eda-viabilidad.ipynb](eda-viabilidad.ipynb) | Los números del EDA: una celda por propiedad y por tipo de *leakage* |
| 6 | [Datasheet](docs/hito_2/3-datasheet.md) | Qué se sabe y qué no de la muestra (formato *Datasheets for Datasets*) |
| 7 | [Veredicto](docs/hito_2/4-veredicto.md) | La decisión, sus fundamentos, la exposición al riesgo y el nuevo alcance |

Cada número citado en el EDA y en el veredicto remite a una celda concreta del
notebook. El enunciado de la cátedra para el Hito 2 está en
[docs/hito_2/ENUNCIADO.md](docs/hito_2/ENUNCIADO.md).

## Estructura del repositorio

```
.
├── README.md
├── propuesta.md              # Idea inicial del proyecto
├── canvas.md                 # AI Opportunity Canvas (documento vivo)
├── eda-viabilidad.ipynb      # Notebook del EDA (Hito 2)
├── requirements.txt
├── datos/                    # Muestra: 14 archivos, 3 materias de Ing. en Sistemas
│   └── ing_sistemas/<materia>/{examenes,practicas,temario}/
└── docs/
    ├── hito_1/
    │   └── ai-opportunity-canvas.pdf
    └── hito_2/
        ├── ENUNCIADO.md      # Consigna de la cátedra
        ├── 1-mapa-de-fuentes.md
        ├── 2-eda-de-viabilidad.md
        ├── 3-datasheet.md
        └── 4-veredicto.md
```

## Cómo reproducir el EDA

Requiere Python 3.10 o superior.

```bash
pip install -r requirements.txt
jupyter notebook eda-viabilidad.ipynb
```

El notebook debe ejecutarse **desde la raíz del repositorio** (lee la carpeta
`datos/` con una ruta relativa) y corre de punta a punta sin pasos manuales.

## Sobre los datos

La muestra en `datos/` reúne exámenes, prácticas y un temario de tres materias
de Ingeniería en Sistemas, obtenidos de repositorios
estudiantiles. Se usa exclusivamente con fines académicos, para ejercitar el
sistema con archivos parecidos a los que subiría un usuario real.

- No tienen licencia de redistribución declarada.
- Algunos archivos contienen autoría en sus metadatos.

Ambos puntos están identificados y medidos en el EDA y figuran como pendientes
abajo.

## Pendientes conocidos

Surgen del [mapa de fuentes](docs/hito_2/1-mapa-de-fuentes.md), el
[datasheet](docs/hito_2/3-datasheet.md) y el [veredicto](docs/hito_2/4-veredicto.md):

- [ ] Anonimizar la muestra (5 archivos con autoría en metadatos, 2 con nombre real).
- [ ] Consultar permisos de redistribución a las cátedras (14 de 14 sin licencia declarada).
- [ ] Definir el comportamiento del producto cuando el usuario no sube temario.
- [ ] Elegir proveedor de LLM (ChatGPT o Claude) y fijar la versión del modelo.
- [ ] Sumar al banco material de al menos una carrera fuera de Ing. en Sistemas.
