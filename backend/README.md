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

### Datos Médicos
- `GET /datos_medicos/` — Lista todos los datos médicos
- `POST /datos_medicos/` — Crea un nuevo dato médico
- `GET /datos_medicos/<id>/` — Obtiene un dato médico específico
- `PUT /datos_medicos/<id>/` — Actualiza un dato médico
- `DELETE /datos_medicos/<id>/` — Elimina un dato médico

### Usuarios
- `GET /usuarios/` — Lista todos los usuarios
- `POST /usuarios/` — Crea un nuevo usuario
- `GET /usuarios/<id>/` — Obtiene un usuario específico
- `PUT /usuarios/<id>/` — Actualiza un usuario
- `DELETE /usuarios/<id>/` — Elimina un usuario

### Login
- `POST /login/` — Login de usuario (requiere `rut` y `contraseña`)

### Boxes
- `GET /boxes/` — Lista todos los boxes
- `POST /boxes/` — Crea un nuevo box
- `GET /boxes/<id>/` — Obtiene un box específico
- `PUT /boxes/<id>/` — Actualiza un box
- `DELETE /boxes/<id>/` — Elimina un box

---

## Funcionalidades de gestión de reservas

Se han agregado dos comandos de administración para poblar y vaciar reservas de boxes según los datos médicos:

### Poblar reservas automáticamente

Llena el campo `reservas` de cada box con los horarios de atención de los médicos.

```sh
python manage.py poblar_reservas
```
- Extrae los horarios desde los campos de cada médico.
- Soporta múltiples horarios en una misma celda.
- Si el box no existe, lo reporta en consola.

### Vaciar todas las reservas

Limpia el campo `reservas` de todos los boxes.

```sh
python manage.py vaciar_reservas
```

---

## CORS

Asegúrate de tener configurado `django-cors-headers` para permitir solicitudes desde el frontend (`http://localhost:8080`).

## Base de datos

Por defecto usa PostgreSQL.  
**Configura tus credenciales en el archivo `.env`** y no en `settings.py`.  
El proyecto usa la librería `python-dotenv` para cargar estas variables de entorno automáticamente.

## Seguridad

- **No subas el archivo `.env` al repositorio** (ya está en `.gitignore`).
- Mantén tus contraseñas y claves secretas solo en `.env`.