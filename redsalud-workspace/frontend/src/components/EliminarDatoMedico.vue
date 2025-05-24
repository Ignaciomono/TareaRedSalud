<template>
  <div>
    <h2>Eliminar Dato Médico</h2>
    <div v-if="dato">
      <div v-for="(valor, campo) in dato" :key="campo">
        <strong>{{ campo }}:</strong> {{ valor }}
      </div>
      <button @click="eliminarDato">Eliminar</button>
    </div>
    <div v-if="mensaje">{{ mensaje }}</div>
    <div v-else-if="!dato">Cargando...</div>
  </div>
</template>

<script>
export default {
  name: 'EliminarDatoMedico',
  data() {
    return { dato: null, mensaje: "" };
  },
  mounted() {
    const id = this.$route.params.id;
    fetch(`http://localhost:8000/datos_medicos/${id}/`)
      .then(res => res.json())
      .then(data => { this.dato = data; });
  },
  methods: {
    eliminarDato() {
      fetch(`http://localhost:8000/datos_medicos/${this.dato.id}/`, {
        method: 'DELETE'
      })
        .then(() => { this.mensaje = "Dato médico eliminado correctamente"; })
        .catch(() => { this.mensaje = "Error al eliminar"; });
    }
  }
}
</script>