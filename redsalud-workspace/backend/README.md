# Backend RedSalud

Backend en Django para la gestión de datos médicos.

## Instalación

1. Crea un entorno virtual:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
2. Instala dependencias:
   ```sh
   pip install -r requirements.txt
   ```
3. Aplica migraciones:
   ```sh
   python manage.py migrate
   ```
4. Ejecuta el servidor:
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

Por defecto usa PostgreSQL. Configura tus credenciales en `settings.py`.