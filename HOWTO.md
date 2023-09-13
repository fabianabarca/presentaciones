# Cómo comenzar con el proyecto

## Instalación de dependencias

- Instalar [Python](https://www.python.org/downloads/)
- (Opcional) Crear un [ambiente virtual](https://docs.python.org/3/library/venv.html) para aislar las dependencias del proyecto:

  - Primero se instala virtualenv:

    ```bash
    pip install virtualenv
    ```

  - En el directorio _/presentaciones/presentaciones_ se crea el entorno virtual:
    ```bash
    py -m venv .venv
    ```
  - Se activa el entorno virtual:
    ```bash
    .\.venv\Scripts\activate
    ```

- En el directorio _/presentaciones/presentaciones_ instalar dependencias:

  - **Django:** Framework que facilita la creación de aplicaciones web siguiendo el patrón MVT.

    ```bash
    pip install Django
    ```

  - **Decouple:** Biblioteca que permite separar los parámetros de configuración del código usando archivos ini, .env o variables de entorno.
    ```bash
    pip install python-decouple
    ```

## Base de datos

En el directorio _/presentaciones/presentaciones_

- Para crear los archivos de migración que representan los cambios que se han hecho en los modelos se ejecuta el comando:
  ```bash
  python manage.py makemigrations
  ```
- Para aplicar los cambios en la base de datos se ejecuta el comando:
  ```bash
  python manage.py migrate
  ```
- Se repiten esos pasos cada vez que se hacen cambios en los modelos.

- Para administrar la base de datos, crear un super usuario con el comando:
  ```bash
  python manage.py createsuperuser
  ```

## Ejecución de la aplicación

- Para correr la aplicación se ejecuta el comando:
  ```bash
  python manage.py runserver
  ```
- La aplicación corre en: http://127.0.0.1:8000/

- Para administrar la base de datos, se inicia sesión con el super usuario creado en la siguiente dirección: http://127.0.0.1:8000/admin/
