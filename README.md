# RedSalud Workspace

Este proyecto es una aplicación full-stack para la gestión de datos médicos, compuesta por un backend en Django y un frontend en Vue.js.

## Estructura del Proyecto

```
redsalud-workspace/
│
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── README.md
│   ├── app/
│   └── redsalud/
│
└── frontend/
    ├── package.json
    ├── README.md
    ├── public/
    └── src/
```

### Backend

- **Django 4.2**
- **Django REST Framework**
- **Base de datos PostgreSQL**
- Endpoints CRUD para el modelo `DatosMedicos`.
- Uso de variables de entorno con `python-dotenv`.

### Frontend

- **Vue.js 3**
- **Vue Router 4**
- Consumo de la API REST del backend.
- Vistas: Home, Lista, Crear, Ver, Editar, Eliminar datos médicos.

## Primeros Pasos

### Backend

1. Crea y activa un entorno virtual (puede llamarse `venv`, `.venv`, `enviroment`, etc.):
   ```sh
   python -m venv enviroment
   enviroment\Scripts\activate
   ```
2. Instala las dependencias:
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

## Notas importantes

- **No subas el archivo `.env` ni archivos de entorno del frontend al repositorio** (ya están en `.gitignore`).
- Si necesitas cambiar la URL del backend en el frontend, usa un archivo `.env` o `.env.local` en la carpeta `frontend/` y accede a la variable con `process.env.VUE_APP_API_URL`.

## Contribuciones

¡Las contribuciones son bienvenidas! Abre un issue o pull request.