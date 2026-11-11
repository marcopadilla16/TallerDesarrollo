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
Desde el Hito 3 incluye además el código de la **PoC** (`poc/`), que se construye
sobre lo fijado en la [definición de la PoC](docs/hito_3/definicion-de-la-poc.md).

## Estado actual

| Entrega | Contenido | Referencia |
|---|---|---|
| #1 | Propuesta y AI Opportunity Canvas (v2) | Tag `v1.0` |
| #2 | Mapa de fuentes | Commit `2e69bc9` (sin tag) |
| #3 | Hito 2: muestra, EDA de viabilidad, datasheet y veredicto (**decisión: ajustar el alcance**). Canvas actualizado a v3 | Tag `v2.0` |
| #4 | Hito 3: definición de la PoC, **en curso**. Incluye los cierres del Hito 1 en el canvas (v5) y las correcciones de los documentos del Hito 2, sin tags nuevos ([registro](docs/decisiones-de-proceso.md)). El código de la PoC (`poc/`) corrió de punta a punta contra la API real el 10/11/2026, antes de sumar los ejercicios y las preguntas tipo parcial, con los 3 formularios sintéticos y el material entero del banco: 3 de 3 planes válidos, pero Redes necesitó un reintento y sigue sin respetar la prioridad por nivel (ver pendientes). Es una corrida de n=3, no la evaluación de la semana 9 | Sin tag todavía |

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
| 1 | [propuesta.md](docs/propuesta.md) | Qué es Study Copilot y qué problema ataca |
| 2 | [canvas.md](docs/hito_1/canvas.md) | Hipótesis de problema, solución, datos, métricas y riesgos. Incluye historial de versiones al final |
| 3 | [Mapa de fuentes](docs/hito_2/1-mapa-de-fuentes.md) | Qué datos necesita el proyecto y qué pasó al intentar conseguirlos |
| 4 | [EDA de viabilidad](docs/hito_2/2-eda-de-viabilidad.md) | Nivel exigido vs. nivel medido por propiedad, y búsqueda de *leakage* |
| 5 | [eda-viabilidad.ipynb](docs/hito_2/eda-viabilidad.ipynb) | Los números del EDA: una celda por propiedad y por tipo de *leakage* |
| 6 | [Datasheet](docs/hito_2/3-datasheet.md) | Qué se sabe y qué no de la muestra (formato *Datasheets for Datasets*) |
| 7 | [Veredicto](docs/hito_2/4-veredicto.md) | La decisión, sus fundamentos, la exposición al riesgo y el nuevo alcance |
| 8 | [Definición de la PoC](docs/hito_3/definicion-de-la-poc.md) | Qué se construye, cómo se valida y con qué modelo. En curso |

Cada número citado en el EDA y en el veredicto remite a una celda concreta del
notebook. El enunciado de la cátedra para el Hito 2 está en
[docs/hito_2/ENUNCIADO.md](docs/hito_2/ENUNCIADO.md).

## Estructura del repositorio

```
.
├── README.md
├── CLAUDE.md                 # Reglas de trabajo: coherencia entre documentos
├── .claude/commands/         # Comandos del proyecto para Claude Code (ver /help-project)
├── .github/prompts/          # Los mismos comandos para Copilot en VS Code
├── requirements.txt
├── .env.example              # Variables para poc/ y experimentos/ (copiar a .env)
├── datos/                    # Muestra: 14 archivos, 3 materias de Ing. en Sistemas
│   └── ing_sistemas/<materia>/{examenes,practicas,temario}/
├── experimentos/             # Prueba del modelo (baseline vs. workflow) y resultados
├── poc/                      # Código de la PoC (Streamlit + OpenAI)
│   ├── app.py                # Interfaz: formulario, archivos por tema, resultado
│   ├── pipeline.py           # Los seis pasos del workflow, en orden
│   ├── formulario.py         # Paso 1: validación del formulario
│   ├── ingesta.py            # Paso 2: PDF/TXT, rechazos, casi-duplicados
│   ├── prompts.py            # Reglas y mensajes para el modelo
│   ├── generador.py          # Pasos 3 a 5: llamada, validación, un reintento
│   ├── validacion.py         # Horas, cobertura, prioridad, contenido pedido
│   ├── registro.py           # Paso 6: un JSON por pedido en registro/
│   └── config.py             # Modelo, niveles, tipos de contenido, umbrales
├── .streamlit/config.toml    # Colores de la interfaz
├── tests/                    # Tests automáticos, con la API simulada
└── docs/
    ├── propuesta.md          # Idea inicial del proyecto
    ├── decisiones-de-proceso.md  # Exploraciones de proceso, insumo del informe final
    ├── hito_1/
    │   ├── ai-opportunity-canvas.pdf  # Plantilla de la cátedra
    │   └── canvas.md         # AI Opportunity Canvas (documento vivo)
    ├── hito_2/
    │   ├── ENUNCIADO.md      # Consigna de la cátedra
    │   ├── 1-mapa-de-fuentes.md
    │   ├── 2-eda-de-viabilidad.md
    │   ├── 3-datasheet.md
    │   ├── 4-veredicto.md
    │   └── eda-viabilidad.ipynb  # Notebook del EDA
    └── hito_3/
        ├── README.md         # Consigna de la cátedra
        └── definicion-de-la-poc.md
```

## Cómo reproducir el EDA

Requiere Python 3.10 o superior.

```bash
pip install -r requirements.txt
jupyter notebook docs/hito_2/eda-viabilidad.ipynb
```

El notebook busca la carpeta `datos/` subiendo desde donde se ejecuta, así que
corre desde la raíz o desde `docs/hito_2/`, de punta a punta y sin pasos manuales.
`pypdf` está fijado en `requirements.txt`: con otra versión cambia el texto extraído y
no se reproducen los caracteres citados en los documentos.

## Cómo correr la PoC

Desde la raíz del repositorio, con las dependencias instaladas:

```bash
cp .env.example .env        # y completar OPENAI_API_KEY (el .env no se commitea)
streamlit run poc/app.py
```

En la barra lateral se cargan la materia, la fecha, el objetivo, el contenido que
se quiere generar (preguntas de autoevaluación, ejercicios prácticos, preguntas
tipo parcial) y un material general opcional. En el cuerpo, cada tema lleva su
nivel y sus propios archivos. El contenido se genera aunque no se suba ningún
archivo: en ese caso el modelo usa su conocimiento general y la pantalla lo
marca.

Para probarla sin subir nada, la barra lateral ofrece el material de una materia
del banco de `datos/`. Cada pedido queda registrado en `registro/` (ignorado por git).

Los tests no llaman a la API real y no cuestan nada:

```bash
pytest
```

> **Aviso.** El texto de los archivos se envía a OpenAI sin anonimizar (fuera de
> alcance en la PoC, sección 1.3 de la definición). Usar sólo el banco de pruebas.

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
- [ ] Documentar de dónde se obtuvo la muestra: los enlaces a los repositorios estudiantiles, que el enunciado del Hito 2 pide para poder regenerarla.
- [ ] Consultar permisos de redistribución a las cátedras (14 de 14 sin licencia declarada).
- [ ] Definir el comportamiento del producto cuando el usuario no sube temario.
- [x] Elegir proveedor de LLM y fijar la versión del modelo: OpenAI, `gpt-5.4-mini-2026-03-17` ([definición de la PoC](docs/hito_3/definicion-de-la-poc.md), 3.1.1).
- [ ] Sumar al banco material de al menos una carrera fuera de Ing. en Sistemas.
- [ ] Volver a correr la prueba del modelo **sin el tope de 30.000 caracteres** (3.1.2), con las repeticiones de 3.1.1. Una primera corrida de la PoC (n=3, 10/11/2026) ya mostró que sin tope Redes manda unos 40.000 tokens por llamada y tardó 79 s con el reintento, contra ~13.900 tokens y 3,8 s de media en 3.1.1; el costo y la latencia de la definición no valen para el material entero.
- [ ] Decidir qué hacer con la prioridad en el caso de 6 temas en 5 horas: el reintento no la corrigió en la corrida real (riesgo 1 de la definición; plan B: regla determinista).
- [ ] Correr contra la API real el contenido nuevo (ejercicios prácticos y preguntas tipo parcial, con y sin archivos): los tests lo cubren con la API simulada, pero la corrida real del 10/11/2026 fue anterior y sólo pidió el plan. Con tres tipos de contenido la salida es más larga, así que se espera más costo y latencia.
- [ ] Rediscutir la rúbrica de corrección conceptual: la definición (v0.4) la pide ahora para tres tipos de contenido y para pedidos sin archivos, y entraba en tres semanas sólo para uno (1.3, suspendido).
- [ ] Script de evaluación (≥30 planes, workflow vs. *baseline*): requiere antes los criterios de aceptación de la sección 2.3, todavía pendientes.
