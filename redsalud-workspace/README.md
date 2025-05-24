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

### Frontend

- **Vue.js 3**
- **Vue Router 4**
- Consumo de la API REST del backend.
- Vistas: Home, Lista, Crear, Ver, Editar, Eliminar datos médicos.

## Primeros Pasos

### Backend

```sh
cd backend
python -m venv venv
venv\Scripts\activate  # En Windows
pip install -r requirements.txt
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

## Contribuciones

¡Las contribuciones son bienvenidas! Abre un issue o pull request.