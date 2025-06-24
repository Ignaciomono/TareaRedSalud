# RedSalud Workspace

Este proyecto es una aplicación full-stack para la gestión de datos médicos, boxes y usuarios, compuesta por un backend en Django y un frontend en Vue.js.

---

## ¿Qué es este proyecto?

RedSalud Workspace es una plataforma para la gestión de especialistas médicos, sus horarios, boxes de atención y reservas. Permite a los coordinadores y especialistas visualizar, asignar y reservar horarios en boxes, así como gestionar usuarios y autenticación.

---

## ¿Cómo se creó y qué tecnologías se usaron?

- **Backend:**  
  - **Framework:** Django 4.2 + Django REST Framework  
  - **Base de datos:** PostgreSQL  
  - **Variables de entorno:** Usando `python-dotenv`  
  - **CORS:** Habilitado para desarrollo local con `django-cors-headers`  
  - **Serialización:** Serializadores automáticos para exponer modelos como API REST  
  - **Gestión de reservas:** Comandos de administración para poblar y vaciar reservas  
  - **Seguridad:** Uso de archivo `.env` para credenciales y claves secretas

- **Frontend:**  
  - **Framework:** Vue.js 3 + Vue Router 4  
  - **Consumo de API REST:** Conexión a Django backend (`http://localhost:8000/`)  
  - **Estilos:** CSS personalizado  
  - **Gestión de estado y rutas:** Vue Router  
  - **Variables de entorno:** `.env` para la URL del backend

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
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   └── ...
│   └── redsalud/
│
└── frontend/
    ├── package.json
    ├── README.md
    ├── public/
    └── src/
        ├── App.vue
        ├── main.js
        ├── router.js
        └── components/
            ├── Home.vue
            ├── DatosMedicos.vue
            ├── Coordinador.vue
            ├── VistaBoxes.vue
            ├── ConfirmarReserva.vue
            ├── Horario.vue
            ├── OlvideContraseña.vue
            └── ...
```

---

## Backend

- **Modelos principales:** 
  - `DatosMedicos`: Especialistas y sus horarios
  - `Usuario`: Login y permisos
  - `Box`: Gestión de boxes y reservas

- **Serializadores:**  
  Definidos en `app/serializers.py`, permiten exponer los modelos como JSON para la API REST.

- **Vistas y lógica de negocio:**  
  Definidas en `app/views.py`, gestionan la autenticación, CRUD de datos médicos, usuarios, boxes y la lógica de reservas.

- **Comandos de gestión de reservas:**  
  - `python manage.py poblar_reservas`: Llena automáticamente las reservas de boxes según los horarios de los médicos.
  - `python manage.py vaciar_reservas`: Vacía todas las reservas de todos los boxes.

- **Seguridad:**  
  No subas `.env` ni credenciales al repositorio.

### Endpoints REST

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

- **Reservar**
  - `POST /reservar/` — Realiza una reserva de box para un especialista en un horario específico  
    - **Ejemplo de payload:**
      ```json
      {
        "codigo_box": "1234",
        "seleccion": [
          {"dia": "Lunes", "hora": "08:15"},
          {"dia": "Martes", "hora": "09:00"}
        ],
        "especialista_id": 5
      }
      ```

---

## Frontend

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

- **Consumo de API REST:**  
  El frontend utiliza `fetch` para consumir los endpoints del backend. Las URLs pueden configurarse mediante un archivo `.env` en la carpeta `frontend/` usando la variable `VUE_APP_API_URL`.

- **Ejemplo de petición desde el frontend:**
  ```js
  fetch('http://localhost:8000/reservar/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      codigo_box: '1234',
      seleccion: [{ dia: 'Lunes', hora: '08:15' }],
      especialista_id: 5
    })
  })
  .then(res => res.json())
  .then(data => { /* manejar respuesta */ });
  ```

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
3. Crea un archivo `.env` en la carpeta `backend/` con tus datos de conexión:
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

---

## Notas importantes

- **No subas el archivo `.env` ni archivos de entorno del frontend al repositorio** (ya están en `.gitignore`).
- Si necesitas cambiar la URL del backend en el frontend, usa un archivo `.env` o `.env.local` en la carpeta `frontend/` y accede a la variable con `process.env.VUE_APP_API_URL`.
- Si tienes problemas de CORS, revisa la configuración en el backend.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Abre un issue o pull request.