# Presentaciones web sincrónicas virtuales

Presentaciones sincrónicas del curso Modelos Probabilísticos de Señales y Sistemas. Parte del proyecto de docencia

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

## Convenciones sobre los formatos multimedia

### :art: Gráficas

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

### :abacus: Ecuaciones

#### *Ecuaciones estáticas*
- LaTeX (directamente en Reveal.js con el plugin de MathJax)

#### *Ecuaciones animadas*
- (Opción más fuerte ahora) Creación en Manim y exportar en algún formato para que sea controlado por el usuario (por ejemplo GIF)
- (Opcional) Crear una una solución duradera con transiciones controladas por usuario y de fácil edición en LaTeX

### :computer: Código

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
