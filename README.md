# Presentaciones web interactivas

Presentaciones web del curso Modelos Probabilísticos de Señales y Sistemas. Parte del proyecto de docencia PD-IE-472-2022 "Estrategias docentes para sesiones virtuales interactivas con el desarrollo de un nuevo sistema web: una experiencia en el curso Modelos Probabilísticos de Señales y Sistemas" de la Escuela de Ingeniería Eléctrica de la Universidad de Costa Rica.

### Plataformas

**Django**: plataforma *backend* en Python ([djangoproject.com](https://www.djangoproject.com/))

<img src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" width="100px">

**Reveal.js**: plataforma *frontend* para presentaciones de diapositivas ([revealjs.com](https://revealjs.com/))

<img src="https://hakim-static.s3.amazonaws.com/reveal-js/logo/v1/reveal-black-text-sticker.png" width="100px">

**PyScript**: herramienta de integración de Python en HTML para ejecución de código ([pyscript.net](https://pyscript.net/))

<img src="https://pyscript.net/assets/images/pyscript-sticker-black.svg" width="100px">

### Herramientas

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1280px-NumPy_logo_2020.svg.png" width="100px">

<img src="https://www.fullstackpython.com/img/logos/scipy.png" width="100px">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/2560px-Pandas_logo.svg.png" width="100px">

<img src="https://matplotlib.org/stable/_images/sphx_glr_logos2_003.png" width="100px">

## Estructura de páginas dentro del sitio

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW0luaWNpb10gLS0-IEIoUHJveWVjdG8pXG4gICAgQSAtLT4gQyhEZW1vKSBcbiAgICBBIC0tPiBEe1JlZ2lzdHJvfVxuICAgIEQgLS0-fFByb2Zlc29yZXN8IEUoUGFuZWwgYWRtaW4pXG4gICAgRCAtLT58RXN0dWRpYW50ZXN8IEYoQ3Vyc28pXG4gICAgRiAtLT4gRyhDbGFzZSBYKVxuICAiLCJtZXJtYWlkIjp7InRoZW1lIjoibmV1dHJhbCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/edit#eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW0luaWNpb10gLS0-IEIoUHJveWVjdG8pXG4gICAgQSAtLT4gQyhEZW1vKSBcbiAgICBBIC0tPiBEe1JlZ2lzdHJvfVxuICAgIEQgLS0-fFByb2Zlc29yZXN8IEUoUGFuZWwgYWRtaW4pXG4gICAgRCAtLT58RXN0dWRpYW50ZXN8IEYoQ3Vyc28pXG4gICAgRiAtLT4gRyhDbGFzZSBYKVxuICAiLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwibmV1dHJhbFwiXG59IiwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)

### :house: &nbsp;&nbsp; Inicio 

*app "inicio"*

Página `index.html` de bienvenida con:

- Información general
- Inicio de sesión / registro de usuarios
- Lista de presentaciones de clase disponibles

### :hammer_and_wrench: &nbsp;&nbsp; Proyecto

*app "inicio"*

Página(s) `proyecto.html` con el planteamiento y el reporte del proyecto de docencia, incluyendo:

- Objetivos
- Antecedentes
- Justificación
- Convenciones como las que están aquí mismo, etc.

### :rocket: &nbsp;&nbsp; Demostración

*app "inicio"*

Presentación `demo.html` abierta al público mostrando todas las características del sistema:

- Multimedia
- Interactividad, etc.

### :gear: &nbsp;&nbsp; Panel de administración

*app "admin"*

Página `profesores.html` con estadísticas y configuración de las presentaciones disponibles en el curso para los estudiantes.

### :books: &nbsp;&nbsp; Curso

*app "clases"*

Página `IE0405.html` (o similar) con la información general del curso y la lista de clases disponibles.

### :chart_with_upwards_trend: &nbsp;&nbsp; Clase X

*app "clases"*

Páginas `claseX.html` con la presentación de cada sesión.

- Documento HTML con la presentación en Reveal.js
- Modelo: respuestas de los usuarios en cada clase
- Modelo: estadísticas de cada clase (asistencia, duración, respuestas, etc.)

## Convenciones sobre los formatos multimedia

### :art: &nbsp;&nbsp; Gráficas

Deben ser vectoriales (con excepciones).

#### *Gráficas estáticas*
- SVG (por defecto para gráficos)
- PNG, JPEG, etc. (para imágenes importadas, especialmente fotografías)
- CSS (cuando se pueda hacer nativamente)

##### Flujo de trabajo
- Python (Matplotlib) >>> SVG
- LaTeX (TikZ) >>> PDF >>> SVG
- Inkscape >>> SVG

#### *Gráficas animadas*
- GIF (por defecto para gráficos)
- Animaciones CSS (especialmente para elementos de la presentación)
- SVG + CSS (cuando sea posible)
- JavaScript (D3.js, anime.js, etc.)

#### *Gráficas interactivas*
- Bokeh (exportadas desde Python)
- Matplotlib (exportadas desde Python)
- JavaScript (nativas)

### :abacus: &nbsp;&nbsp; Ecuaciones

#### *Ecuaciones estáticas*
- LaTeX (directamente en Reveal.js con el plugin de MathJax)

#### *Ecuaciones animadas*
- (Opción más fuerte ahora) Creación en Manim y exportar en algún formato para que sea controlado por el usuario (por ejemplo GIF)
- (Opcional) Crear una una solución duradera con transiciones controladas por usuario y de fácil edición en LaTeX

### :computer: &nbsp;&nbsp; Código

#### *Código estático*
- Directamente en Reveal.js
- Gist de GitHub o algún otro visualizador de código en `<iframe>` o similar

#### *Código "animado" o editado en tiempo real*
- (Opcional) Implementación de una solución con WebRTC o similar
- Búsqueda de un visualizador

#### *Código ejecutable*
- (Opcional) Crear un REPL para el sitio
- Repl.it, Codepen u otra opción similar para Python

## Estilo visual

Las presentaciones, gráficas y demás material se van a ajustar al manual de identidad visual de la UCR. Para ello es necesario crear:

- Hoja de estilo de Matplotlib (`.mplstyle`)
- Hoja de estilo CSS (Reveal.js)

## Sobre la dinámica de la clase:

Algunas consideraciones iniciales sobre la dinámica que facilita el sistema de presentaciones.

- Muchas preguntas de verificación de lectura
- Las diapositivas no son réplicas del material de clase (explicados en las clases asincrónicas)
- Las diapositivas solo tienen información seleccionada de las presentaciones y videos disponibles de forma asincrónica

## Repositorio de características deseables:

Ideas no estructuradas:

- [ ] Laser pointer o similar
- [ ] WebRTC
- [ ] Poner instrucciones de Reveal.js: overview, zoom, etc.
- [ ] Asunto de tiempo de carga (ojo a esto)
- [ ] Matplotlib hace animaciones
- [ ] Gráficas: estáticas, animadas, interactivas
- [ ] Asunto de edición de código en tiempo real
- [ ] Hacer REPL propio
- [ ] Revisar asunto de sincronización
- [ ] Hacer registro de las respuestas de los usuarios en la base de datos
- [ ] Poner un aviso para evitar que se cierre la pestaña del navegador (para no salirse de la sesión)
- [ ] Estudiantes del curso pueden (deben) crear animaciones
- [ ] Crear plan de asignaciones
