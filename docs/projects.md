# Planificación de proyectos programados

En el sistema web de presentaciones habrá cinco sesiones virtuales dedicadas a la explicación de la solución de cinco proyectos programados, uno por cada tema del curso, para ejemplificar tanto la materia del curso como el uso de herramientas computacionales para el análisis de datos.

#### Premisas

- Los proyectos siguen un "arco temático" alrededor de la creación de un *data pipeline*, o esquema de canalización para el análisis de datos.
- Los proyectos tienen énfasis en la programación de una solución basada en la teoría del curso.
- Los proyectos incluyen una documentación donde es explicado lo realizado.
- Los proyectos aquí presentados son un ejemplo para la evaluación de proyectos del curso.
- Objetivos globales:
  - Toma de decisiones basadas en datos
  - Diseño de sistemas de ingeniería
  - Diseño de experimentos (simulaciones de Monte Carlo)
- Estas sesiones virtuales son, aparte de los PyX, un acompañamiento al aprendizaje de la programación y serán de uso general en todos los semestres (los enunciados de los proyectos de cada semestre serán distintos).

#### Contenido de cada proyecto

Cada proyecto incluye:

1. Teoría del curso
1. Herramientas de programación
1. Etapas del proceso de análisis de datos
1. Presentación documental

Cada cada una de estas áreas es ampliada a continuación para determinar todos los contenidos que deben ser cubiertos en los proyectos.

## :books: Teoría del curso

La división es de un proyecto por cada tema del curso.

### :white_check_mark: Distribución en los proyectos 

- Proyecto 1: Introducción a la probabilidad
- Proyecto 2: Variables aleatorias
- Proyecto 3: Variables aleatorias múltiples
- Proyecto 4: Procesos aleatorios
- Proyecto 5: Cadenas de Markov

## :computer: Herramientas de programación

### Módulos de Python para análisis de datos

- NumPy
- Matplotlib
- SciPy
- Pandas
- Requests
- Seaborn
- Otros

### PyX: tutoriales de Python para análisis de datos

Para el curso han sido desarrollados una serie de tutoriales de programación llamados [PyX](https://github.com/fabianabarca/python).

| Nombre | Tema | Librerías |
| ------ | ---- | ---- |
| `Py0`  | Introducción a Python |  |
| `Py1`  | Funciones y librerías estándar | Math, Random... |
| `Py2`  | Manipulación de datos  | Pandas |
| `Py3`  | Librerías de computación científica | NumPy, SciPy, Matplotlib |
| `Py4`  | Funciones estadísticas | Stats de SciPy |
| `Py5`  | Curvas de ajuste y modelos estadísticos para datos | Fitter |
| `Py6`  | Intercambio de datos con servicios web | Requests |
| `Py7`  | Graficación estadística  | Seaborn |

Pendientes:

| Nombre | Tema | Librerías |
| ------ | ---- | ---- |
| `Py8`  | Bases de datos SQL con Python | SQLite |
| `Py9`  | Principios de programación orientada a objetos |  |
| `Py10` | Documentación de código | Sphinx |

Adicional:

| Nombre | Tema | 
| ------ | ---- | 
| `Git0` | Introducción a Git: sistemas de control de versiones |

### Entornos de programación de Python

- Entornos interactivos
  - Jupyter
  - REPL.it
- Entornos integrados de desarrollo
  - VS Code
  - PyCharm
  - Sublime
  - Atom

### Otras herramientas

- Sistemas de versiones (Git y GitHub)
- Convenciones de formato (PEP 8)

### :white_check_mark: Distribución en los proyectos

- Proyecto 1: Py0, Py1, Py2
- Proyecto 2: Py3, Py4, Py5
- Proyecto 3: Py6, Py7, Py8
- Proyecto 4: Py9, Py10, Git0
- Proyecto 5: todos los anteriores

## :bar_chart: Etapas del proceso de análisis de datos

El análisis de datos masivos tiene una secuencia usual de pasos y tareas comunes para realizar su labor. Los itemes a continuación serán parte de los proyectos.

### Tareas básicas

- Importación de datos
  - de archivos locales
  - de fuentes externas
    - API
- Almacenamiento de datos
- Preprocesamiento de datos
- Manipulación de datos
  - como contenedor (lista, tupla, diccionario)
  - como `array` de NumPy
  - como `DataFrame` de Pandas
- Análisis exploratorio de datos
  - estadística descriptiva
  - gráficas

### Formatos de archivos de datos

- JSON
- CSV
- XLSX
- Otros: XML, YAML, TOML

### Gráficas

- Clasificación de tipos de gráficas
- Paquetes de graficación en Python: Matplotlib, Seaborn

### :white_check_mark: Distribución en los proyectos

- Proyecto 1
  - importación de datos de archivos locales
  - preprocesamiento de datos
  - visualización de datos
- Proyecto 2
  - procesamiento de datos
  - análisis estadístico exploratorio de datos
  - modelado de distribuciones de probabilidad
- Proyecto 3
  - importación de datos de servicios web
  - visualización avanzada de datos
  - manipulación de bases de datos
- Proyecto 4
  - almacenamiento en bases de datos
- Proyecto 5
  - diseño de simulaciones aleatorias

## :page_facing_up: Presentación documental

### Jupyter

Jupyter permite la edición de celdas de Markdown y de código fuente junto con los resultados de su ejecución y la posibilidad de exportar como HTML o PDF. 

### LaTeX

Una plantilla de LaTeX para hacer un reporte de alta calidad, utilizando las herramientas de importación de código y de gráficas para mostrar los resultados de las simulaciones.

### Documentación en GitHub

Un archivo `README.md` es una forma sencilla y efectiva de documentar un proyecto.

### Documentación en Python

La forma más completa de documentar un proyecto de software en Python es con herramientas como Sphinx y similares, que luego se pueden publicar en páginas como ReadTheDocs.

### :white_check_mark: Distribución en los proyectos

Posible distribución de presentación documental en los proyectos:

- Proyecto 1: Jupyter (Markdown)
- Proyecto 2: Jupyter (Markdown)
- Proyecto 3: LaTeX
- Proyecto 4: GitHub (Markdown)
- Proyecto 5: Sphinx

# Descripción de los proyectos

## Proyecto 1

> El proyecto consiste en el estudio (importación, inspección, graficación) de un conjunto de datos para obtener (por medio de funciones y cálculos numéricos) frecuencias relativas de eventos de interés y así resolver problemas de probabilidades conjuntas y condicionales.

### Teoría del curso

Presentaciones:

- Teoría de conjuntos y análisis combinatorio
- Introducción a la probabilidad
- Probabilidad conjunta y condicional y teorema de Bayes
- Eventos independientes y pruebas de Bernoulli

### Herramientas de programación

- Aprender los principios básicos de Python (Py0, Introducción a Python)
- Aprender cómo usar librerías y hacer funciones en Python (Py1, Funciones y librerías estándar)
- Aprendar a usar Pandas para manipulación de datos (Py2, Manipulación de datos)

### Etapas del proceso de análisis de datos

Manipulación de datos
Exploración de datos
Visualización de datos

- Importar datos de archivos locales en varios formatos
- Preprocesar datos
- Visualizar datos
  - Histogramas

### Presentación documental

- Presentar un informe en Jupyter

## Proyecto 2

> El proyecto consiste en el modelado matemático de un conjunto de datos aleatorios con una distribución de probabilidad, usando las herramientas de Python, y la estimación de parámetros de interés de estos datos, como la media y la varianza, entre otros. Con esto es posible también calcular probabilidades para resolver un problema específico.

### Teoría del curso

Presentaciones:

- Variables aleatorias
- Funciones de distribución condicionales
- Momentos de una variable aleatoria
- Funciones que dan momentos
- Transformaciones de una variable aleatoria

### Herramientas de programación

- Utilizar librerías de computación científica y graficación en Python (Py2, Librerías de computación científica)

### Etapas del proceso de análisis de datos

- Procesamiento de datos
- Análisis estadístico exploratorio de datos
- Modelado de distribuciones de probabilidad

### Presentación documental

- Presentar un informe en Jupyter

## Proyecto 3

> El proyecto consiste en el análisis de un conjunto de datos masivos con varias variables relacionadas entre sí, para encontrar parámetros como la correlación y la covarianza.

### Teoría del curso

Presentaciones:

- Variables aleatorias múltiples
- Momentos de variables aleatorias múltiples
- Transformaciones de variables aleatorias múltiples
- Teorema del límite central y otros

### Herramientas de programación

### Etapas del proceso de análisis de datos

### Presentación documental

- Presentar un informe en LaTeX

## Proyecto 4

> El proyecto consiste en el análisis de una señal aleatoria variante en el tiempo.

### Teoría del curso

Presentaciones:

- Procesos estocásticos
- Ergodicidad y funciones de correlación
- Características espectrales de procesos estocásticos
- Respuesta de sistemas lineales a una señal aleatoria

### Herramientas de programación

- Desarrollar un proyecto colaborativo en GitHub

### Etapas del proceso de análisis de datos

- Análisis de datos dinámicos (variantes en el tiempo)

### Presentación documental

- Presentar un informe en GitHub

## Proyecto 5

> El proyecto consiste en la simulación de un sistema dinámico para comprobar los conceptos de la teoría de colas.

### Teoría del curso

Presentaciones:

- Proceso contador de Poisson
- Cadenas de Markov de tiempo continuo
- Markov de tiempo continuo y el vector de estado estable
- Cadenas de Markov de tiempo discreto
- Markov de tiempo discreto y el vector de estado estable

### Herramientas de programación

- Todas las herramientas de programación aprendidas hasta el momento

### Etapas del proceso de análisis de datos

- Desarrollo de simulaciones aleatorias (pruebas de Monte Carlo)

### Presentación documental

- Presentar un informe como documentación de software con Sphinx
