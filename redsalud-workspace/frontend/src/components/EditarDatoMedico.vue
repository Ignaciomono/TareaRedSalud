<template>
  <div>
    <h2>Editar Dato Médico</h2>
    <form v-if="dato" @submit.prevent="editarDato">
      <div v-for="campo in camposSinId" :key="campo">
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
  computed: {
    camposSinId() {
      return this.dato ? Object.keys(this.dato).filter(campo => campo !== 'id') : [];
    }
  },
  mounted() {
    const id = this.$route.params.id;
    fetch(`http://localhost:8000/datos_medicos/${id}/`)
      .then(res => res.json())
      .then(data => { this.dato = data; });
  },
  methods: {
    editarDato() {
      const { id, ...datoSinId } = this.dato;
      fetch(`http://localhost:8000/datos_medicos/${id}/`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datoSinId)
      })
        .then(async res => {
          const data = await res.json();
          if (res.ok) {
            this.mensaje = "Dato médico actualizado correctamente";
          } else {
            this.mensaje = "Error al actualizar: " + JSON.stringify(data);
            console.error("Error al actualizar:", data);
          }
        })
        .catch(err => {
          this.mensaje = "Error al actualizar";
          console.error(err);
        });
    }
  }
}
</script>