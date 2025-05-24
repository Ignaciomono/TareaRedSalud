# Frontend RedSalud

Frontend en Vue 3 para la gestión de datos médicos.

## Instalación

```sh
cd frontend
npm install
```

## Uso

```sh
npm run serve
```

Abre [http://localhost:8080](http://localhost:8080).

## Vistas principales

- **Home:** Página de inicio con acceso a la lista de datos médicos.
- **Lista:** Muestra todos los datos médicos y permite ver, editar, eliminar o crear nuevos.
- **Crear:** Formulario para agregar un nuevo dato médico.
- **Detalle:** Información de un dato médico específico.
- **Editar:** Modifica un dato médico existente.
- **Eliminar:** Elimina un dato médico.

## Configuración de rutas

Las rutas están en `src/router.js` usando Vue Router 4.

## Conexión con el backend

El frontend consume la API REST de Django en `http://localhost:8000/datos_medicos/`.

## Notas

Si tienes problemas de CORS, revisa la configuración en el backend.