<template>
  <div>
    <h1>Datos Médicos</h1>
    <router-link to="/datos-medicos/crear"><button>Crear Nuevo</button></router-link>
    <router-link to="/datos-medicos"><button>Volver a la lista</button></router-link>
    <router-link to="/"><button>Inicio</button></router-link>
    <table border="1">
      <thead>
        <tr>
          <th v-for="(value, key) in datos[0]" :key="key">{{ key }}</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="dato in datos" :key="dato.id">
          <td v-for="(value, key) in dato" :key="key">{{ value }}</td>
          <td>
            <router-link :to="`/datos-medicos/${dato.id}`"><button>Ver</button></router-link>
            <router-link :to="`/datos-medicos/${dato.id}/editar`"><button>Editar</button></router-link>
            <router-link :to="`/datos-medicos/${dato.id}/eliminar`"><button>Eliminar</button></router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'DatosMedicos',
  data() {
    return {
      datos: []
    }
  },
  mounted() {
    fetch('http://localhost:8000/datos_medicos/')
      .then(response => response.json())
      .then(data => {
        this.datos = data;
      });
  }
}
</script>