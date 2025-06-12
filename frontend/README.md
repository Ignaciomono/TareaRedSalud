# Frontend RedSalud

Frontend en Vue 3 para la gestión de datos médicos y boxes.

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

- **Home:** Página de inicio y login de usuario (con autenticación por RUT y contraseña).
- **Datos Médicos:** Tabla con todos los datos médicos registrados.
- **Coordinador:** Vista principal para el coordinador, muestra y permite buscar especialistas.
- **Vista Especialista:** Detalle de uno o varios especialistas, con todos sus datos y horarios.
- **Vista Boxes:** Gestión de boxes, muestra la asignación de especialistas y procedimientos a cada box.
- **Agregar Boxes:** Formulario para asignar especialistas a boxes.
- **Olvide Contraseña:** Información de contacto para recuperar acceso.

## Configuración de rutas

Las rutas están en `src/router.js` usando Vue Router 4:

- `/` — Home (login)
- `/datos-medicos` — Lista de datos médicos
- `/olvide-contraseña` — Recuperar contraseña
- `/coordinador` — Panel de especialistas
- `/boxes` — Gestión de boxes
- `/agregar-boxes` — Asignar especialistas a boxes
- `/vista-especialista` — Detalle de especialista(s)

## Conexión con el backend

El frontend consume la API REST de Django en `http://localhost:8000/`.

- Para datos médicos: `http://localhost:8000/datos_medicos/`
- Para login: `http://localhost:8000/login/`
- Para boxes: `http://localhost:8000/boxes/`
- Para usuarios: `http://localhost:8000/usuarios/`

### Cambiar la URL del backend

Si necesitas cambiar la URL del backend (por ejemplo, para producción), puedes crear un archivo `.env` o `.env.local` en la carpeta `frontend/` con:

```
VUE_APP_API_URL=http://localhost:8000/
```

Y en tu código Vue, usa `process.env.VUE_APP_API_URL` para acceder a la variable.

## Notas

- Si tienes problemas de CORS, revisa la configuración en el backend.
- **No subas archivos `.env` del frontend al repositorio** (ya están en `.gitignore`).

---
**Actualizado:** Ahora el frontend soporta gestión de boxes, asignación de especialistas, login y vistas detalladas de especialistas, coordinador y boxes.