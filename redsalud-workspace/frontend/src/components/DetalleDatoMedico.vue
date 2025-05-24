<template>
  <div>
    <h2>Detalle Dato Médico</h2>
    <div v-if="dato">
      <div v-for="(valor, campo) in dato" :key="campo">
        <strong>{{ campo }}:</strong> {{ valor }}
      </div>
    </div>
    <div v-else>Cargando...</div>
  </div>
</template>

<script>
export default {
  name: 'DetalleDatoMedico',
  data() {
    return { dato: null };
  },
  mounted() {
    const id = this.$route.params.id;
    fetch(`http://localhost:8000/datos_medicos/${id}/`)
      .then(res => res.json())
      .then(data => { this.dato = data; });
  }
}
</script>