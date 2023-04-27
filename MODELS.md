# Estructura del sitio y base de datos

## Aplicaciones

- `courses`: información sobre el o los cursos en la plataforma.
- `decks`: las presentaciones (*slide decks*).
- `website`: páginas misceláneas (inicio, acerca, contacto, etc.).
- `users`: manejo de usuarios, incluyendo estadísticas.

## Modelos de la base de datos

#### Nota sobre el almacenamiento de las presentaciones en Reveal.js

El sistema no tiene ni tendrá en el mediano plazo un editor con interfaz gráfica para las presentaciones en Reveal.js, por tanto la edición es directamente sobre documentos HTML. Por lo tanto, la mejor forma, por ahora, de guardar la presentación es como un `FileField` de Django.

En `courses/models.py`:

- `class Course`: cada curso donde hay presentaciones
    - `course_id` (CharField): llave primaria del curso (ejemplo: 'IE0405')
    - `name` (CharField): nombre del curso
    - `description` (TextField): descripción breve del curso

En `decks/models.py`:

- `class Deck`: cada presentación
    - `deck_id` (CharField): llave primaria de la presentación
    - `course_id` (ForeignKey): llave foránea para un curso del sistema
    - `sequence` (CharField): secuencia o número de la presentación dentro del curso. Es un valor alfanumérico que será útil entre otras cosas para ordenar la lista de presentaciones en la página del curso
    - `slides` (FileField): documento HTML con las diapositivas de la presentación
    - `visits` (PositiveIntegerField): número de visitas que ha tenido la presentación, de forma sincrónica o asincrónica.

En `website/models.py`:

- `class Notice`: notificaciones o avisos para el sistema o para un curso
    - `short_description` (CharField): titular de la noticia
    - `long_description` (TextField): contenido de la noticia
    - `course_id` (ForeignKey): llave foránea para un curso del sistema

En `users/models.py`:

- `class User`: información de cada persona usuaria
    - `user_id` (CharField): idenitificación (ejemplo: 'B12345')
    - `email` (EmailField): correo electrónico
    - `first_name` (CharField): nombres
    - `last_name` (CharField): apellidos
