# Presentaciones

Presentaciones sincrónicas del curso Modelos Probabilísticos de Señales y Sistemas.

* *Front-end*: **Reveal.js**
* *Back-end*: **Django**

## Estructura de páginas dentro del sitio

**index.html** (app "inicio")

* Página de bienvenida / información general
* Inicio de sesión / registro de usuarios
* Lista de presentaciones de clase disponibles
* Modelo: usuarios

**claseX.html** (app "clases")

* Documento HTML con la presentación en Reveal.js
* Modelo: respuestas de los usuarios en cada clase
* Modelo: estadísticas de cada clase (asistencia, duración, respuestas, etc.)

## Convenciones sobre los formatos de multimedia

### Gráficas

Deben ser vectoriales (con excepciones)

#### Gráficas estáticas
- SVG (por defecto para gráficos)
- PNG, JPEG, etc. (para imágenes importadas, especialmente fotografías)
- CSS (cuando se pueda hacer nativamente)

##### Flujo de trabajo
- Python (Matplotlib) >>> SVG
- LaTeX (TikZ) >>> PDF >>> SVG
- Inkscape >>> SVG

#### Gráficas animadas
- GIF (por defecto para gráficos)
- Animaciones CSS (especialmente para elementos de la presentación)
- SVG + CSS (cuando sea posible)
- JavaScript (D3.js, anime.js, etc.)

#### Gráficas interactivas
- Bokeh (exportadas desde Python)
- Matplotlib (exportadas desde Python)
- JavaScript (nativas)

### Ecuaciones

#### Ecuaciones estáticas
- LaTeX (directamente en Reveal.js con el plugin de MathJax)

#### Ecuaciones animadas
- (Opción más fuerte ahora) Creación en Manim y exportar en algún formato para que sea controlado por el usuario (por ejemplo GIF)
- (Opcional) Crear una una solución duradera con transiciones controladas por usuario y de fácil edición en LaTeX
