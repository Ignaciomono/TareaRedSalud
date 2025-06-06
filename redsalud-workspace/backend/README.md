# Backend RedSalud

Backend en Django para la gestión de datos médicos.

## Instalación

1. Crea un entorno virtual (puedes llamarlo `venv`, `.venv`, `enviroment`, etc.):
   ```sh
   python -m venv enviroment
   enviroment\Scripts\activate
   ```
2. Instala dependencias:
   ```sh
   pip install -r requirements.txt
   ```
3. Crea un archivo `.env` en la carpeta `backend/` con el siguiente contenido (ajusta tus datos):
   ```
   DB_NAME=Redsalud
   DB_USER=postgres
   DB_PASSWORD=tu_contraseña
   DB_HOST=localhost
   DB_PORT=5432
   SECRET_KEY=django-insecure-1234567890abcdefghijklmnopqrstuv
   ```
4. Aplica migraciones:
   ```sh
   python manage.py migrate
   ```
5. Ejecuta el servidor:
   ```sh
   python manage.py runserver
   ```

## Endpoints principales

- `GET /datos_medicos/` — Lista todos los datos médicos
- `POST /datos_medicos/` — Crea un nuevo dato médico
- `GET /datos_medicos/<id>/` — Obtiene un dato médico específico
- `PUT /datos_medicos/<id>/` — Actualiza un dato médico
- `DELETE /datos_medicos/<id>/` — Elimina un dato médico

## CORS

Asegúrate de tener configurado `django-cors-headers` para permitir solicitudes desde el frontend (`http://localhost:8080`).

## Base de datos

Por defecto usa PostgreSQL.  
**Configura tus credenciales en el archivo `.env`** y no en `settings.py`.  
El proyecto usa la librería `python-dotenv` para cargar estas variables de entorno automáticamente.

## Seguridad

- **No subas el archivo `.env` al repositorio** (ya está en `.gitignore`).
- Mantén tus contraseñas y claves secretas solo en `.env`.