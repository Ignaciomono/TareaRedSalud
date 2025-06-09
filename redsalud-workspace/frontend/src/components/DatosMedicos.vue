<template>
  <div class="datos-medicos-scroll">
    <h1>Datos Médicos</h1>
    <table border="1">
      <thead>
        <tr>
          <th v-for="(value, key) in datos[0]" :key="key">{{ key }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="dato in datos" :key="dato.id">
          <td v-for="(value, key) in dato" :key="key">{{ value }}</td>
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

<style scoped>
.datos-medicos-scroll {
  width: 100vw;
  height: 100vh;
  overflow: auto;
  box-sizing: border-box;
  padding: 2rem;
  background: #f8f8f8;
}
table {
  min-width: 600px;
  background: #fff;
}
</style>