<template>
  <div>
    <h2>Editar Dato Médico</h2>
    <form v-if="dato" @submit.prevent="editarDato">
      <div v-for="(valor, campo) in dato" :key="campo">
        <label :for="campo">{{ campo }}</label>
        <input :id="campo" v-model="dato[campo]" />
      </div>
      <button type="submit">Guardar Cambios</button>
    </form>
    <div v-if="mensaje">{{ mensaje }}</div>
    <div v-else-if="!dato">Cargando...</div>
  </div>
</template>

<script>
export default {
  name: 'EditarDatoMedico',
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
    editarDato() {
      fetch(`http://localhost:8000/datos_medicos/${this.dato.id}/`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.dato)
      })
        .then(res => res.json())
        .then(() => { this.mensaje = "Dato médico actualizado correctamente"; })
        .catch(() => { this.mensaje = "Error al actualizar"; });
    }
  }
}
</script>