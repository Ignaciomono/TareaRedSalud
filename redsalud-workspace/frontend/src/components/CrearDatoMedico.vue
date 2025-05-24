<template>
  <div>
    <h2>Crear Dato Médico</h2>
    <form @submit.prevent="crearDato">
      <div v-for="campo in campos" :key="campo">
        <label :for="campo">{{ campo }}</label>
        <input :id="campo" v-model="nuevoDato[campo]" required />
      </div>
      <button type="submit">Crear</button>
    </form>
    <div v-if="mensaje">{{ mensaje }}</div>
    <router-link to="/datos-medicos"><button>Ver Lista</button></router-link>
    <router-link to="/"><button>Inicio</button></router-link>
  </div>
</template>

<script>
export default {
  name: 'CrearDatoMedico',
  data() {
    return {
      campos: [
        "rut", "nombre", "especialidad", "qir", "tiene_consulta", "tiene_proced", "proced_a_realizar",
        "piso_atencion", "nuevo_piso_desde_septiembre", "vigencia", "frecuencia", "dias_atencion",
        "cantidad_horas", "cantidad_minutos", "pctes_semanales", "lunes", "martes", "miercoles",
        "jueves", "viernes", "sabado", "horario_lunes", "horario_martes", "horario_miercoles",
        "horario_jueves", "horario_viernes", "horario_sabado", "movimiento_agenda", "correo", "telefono"
      ],
      nuevoDato: {},
      mensaje: ""
    };
  },
  methods: {
    crearDato() {
      fetch('http://localhost:8000/datos_medicos/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.nuevoDato)
      })
        .then(res => res.json())
        .then(() => {
          this.mensaje = "Dato médico creado correctamente";
          this.nuevoDato = {};
        })
        .catch(() => {
          this.mensaje = "Error al crear el dato médico";
        });
    }
  }
}
</script>