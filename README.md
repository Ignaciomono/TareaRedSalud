# RedSalud Workspace

Este proyecto es una aplicación full-stack para la gestión de datos médicos, boxes y usuarios, compuesta por un backend en Django y un frontend en Vue.js.

---

## Estructura del Proyecto

```
redsalud-workspace/
│
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── README.md
│   ├── .env
│   ├── app/
│   └── redsalud/
│
└── frontend/
    ├── package.json
    ├── README.md
    ├── public/
    └── src/
```

---

## Backend

- **Framework:** Django 4.2 + Django REST Framework
- **Base de datos:** PostgreSQL (configurable por `.env`)
- **Variables de entorno:** Usando `python-dotenv`
- **CORS:** Habilitado para desarrollo local
- **Modelos principales:** 
  - `DatosMedicos` (especialistas y sus horarios)
  - `Usuario` (login y permisos)
  - `Box` (gestión de boxes y reservas)
- **Endpoints REST:**
  - **Datos Médicos**
    - `GET /datos_medicos/` — Lista todos los datos médicos
    - `POST /datos_medicos/` — Crea un nuevo dato médico
    - `GET /datos_medicos/<id>/` — Obtiene un dato médico específico
    - `PUT /datos_medicos/<id>/` — Actualiza un dato médico
    - `DELETE /datos_medicos/<id>/` — Elimina un dato médico
  - **Usuarios**
    - `GET /usuarios/` — Lista todos los usuarios
    - `POST /usuarios/` — Crea un nuevo usuario
    - `GET /usuarios/<id>/` — Obtiene un usuario específico
    - `PUT /usuarios/<id>/` — Actualiza un usuario
    - `DELETE /usuarios/<id>/` — Elimina un usuario
  - **Login**
    - `POST /login/` — Login de usuario (requiere RUT y contraseña)
  - **Boxes**
    - `GET /boxes/` — Lista todos los boxes
    - `POST /boxes/` — Crea un nuevo box
    - `GET /boxes/<id>/` — Obtiene un box específico
    - `PUT /boxes/<id>/` — Actualiza un box
    - `DELETE /boxes/<id>/` — Elimina un box
- **Comandos de gestión de reservas:**
  - `python manage.py poblar_reservas` — Llena automáticamente las reservas de boxes según los horarios de los médicos (soporta múltiples horarios por celda).
  - `python manage.py vaciar_reservas` — Vacía todas las reservas de todos los boxes.
- **Seguridad:** No subas `.env` ni credenciales al repositorio.

---

## Frontend

- **Framework:** Vue.js 3 + Vue Router 4
- **Consumo de API REST:** Conexión a Django backend (`http://localhost:8000/`)
- **Vistas principales:**
  - **Home:** Login de usuario (autenticación por RUT y contraseña)
  - **Datos Médicos:** Tabla con todos los datos médicos registrados
  - **Coordinador:** Panel principal para el coordinador, búsqueda y listado de especialistas
  - **Vista Especialista:** Detalle de uno o varios especialistas, con todos sus datos y horarios
  - **Vista Boxes:** Gestión de boxes, muestra la asignación de especialistas y procedimientos a cada box
  - **Agregar Boxes:** Formulario para asignar especialistas a boxes
  - **Olvide Contraseña:** Información de contacto para recuperar acceso
- **Rutas configuradas en** `src/router.js`:
  - `/` — Home (login)
  - `/datos-medicos` — Lista de datos médicos
  - `/olvide-contraseña` — Recuperar contraseña
  - `/coordinador` — Panel de especialistas
  - `/boxes` — Gestión de boxes
  - `/agregar-boxes` — Asignar especialistas a boxes
  - `/vista-especialista` — Detalle de especialista(s)
- **Configuración de backend:** Puedes cambiar la URL del backend usando un archivo `.env` o `.env.local` en la carpeta `frontend/` con la variable `VUE_APP_API_URL`.
- **Notas:** No subas archivos `.env` del frontend al repositorio.

---

## Primeros Pasos

### Backend

1. Crea y activa un entorno virtual:
   ```sh
   python -m venv enviroment
   enviroment\Scripts\activate
   ```
2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
3. Crea un archivo `.env` en la carpeta `backend/` con tus datos de conexión.
4. Aplica migraciones y ejecuta el servidor:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend

```sh
cd frontend
npm install
npm run serve
```

Abre [http://localhost:8080](http://localhost:8080) en tu navegador.

---

## Notas importantes

- **No subas el archivo `.env` ni archivos de entorno del frontend al repositorio** (ya están en `.gitignore`).
- Si necesitas cambiar la URL del backend en el frontend, usa un archivo `.env` o `.env.local` en la carpeta `frontend/` y accede a la variable con `process.env.VUE_APP_API_URL`.
- Si tienes problemas de CORS, revisa la configuración en el backend.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Abre un issue o pull request.