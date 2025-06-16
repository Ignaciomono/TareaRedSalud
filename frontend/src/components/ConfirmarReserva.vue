<template>
  <div class="confirmar-main">
    <div class="confirmar-card">
      <h2>Confirmar Reserva</h2>
      <div class="box-info">
        <h3>Box Seleccionado</h3>
        <p><strong>Nombre:</strong> {{ box.nombre }}</p>
        <p><strong>Código:</strong> {{ box.codigo }}</p>
        <p v-if="box.ubicacion"><strong>Ubicación:</strong> {{ box.ubicacion }}</p>
      </div>
      <div class="horarios-info">
        <h3>Horarios Seleccionados</h3>
        <ul>
          <li v-for="(item, idx) in seleccion" :key="idx">
            <strong>{{ item.dia }}</strong> - {{ item.hora }}
          </li>
        </ul>
      </div>
      <div class="especialista-info">
        <h3>Selecciona un Especialista</h3>
        <select v-model="especialistaSeleccionado">
          <option disabled value="">Seleccione...</option>
          <option v-for="esp in especialistas" :key="esp.id" :value="esp.id">
            {{ esp.nombre }}
          </option>
        </select>
      </div>
      <div class="botones-acciones">
        <button class="btn-volver" @click="volver">Volver</button>
        <button class="btn-volver-horario" @click="volverHorario">Volver a Horario</button>
        <button
          class="btn-confirmar"
          :disabled="!especialistaSeleccionado"
          @click="confirmarReserva"
        >
          Confirmar
        </button>
      </div>
      <div v-if="mensaje" style="color:green; margin-top:1em;">{{ mensaje }}</div>
      <div v-if="error" style="color:red; margin-top:1em;">{{ error }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ConfirmarReserva',
  data() {
    return {
      seleccion: [],
      box: {},
      especialistas: [],
      especialistaSeleccionado: "",
      mensaje: "",
      error: ""
    };
  },
  async created() {
    try {
      this.seleccion = JSON.parse(this.$route.query.seleccion || '[]');
      const codigo = this.$route.query.codigo;
      if (codigo) {
        const response = await fetch(`http://localhost:8000/boxes/${codigo}/`);
        if (response.ok) {
          this.box = await response.json();
        }
      }
      // Cargar especialistas
      const respEsp = await fetch('http://localhost:8000/datos_medicos/');
      if (respEsp.ok) {
        this.especialistas = await respEsp.json();
      }
    } catch (e) {
      this.seleccion = [];
      this.box = {};
      this.especialistas = [];
    }
  },
  methods: {
    volver() {
      this.$router.back();
    },
    volverHorario() {
      // Redirige a la vista de horario del box actual
      this.$router.push({
        path: '/horario',
        query: { codigo: this.box.codigo }
      });
    },
    async confirmarReserva() {
      this.mensaje = "";
      this.error = "";
      try {
        const payload = {
          codigo_box: this.box.codigo,
          seleccion: this.seleccion,
          especialista_id: this.especialistaSeleccionado
        };
        const resp = await fetch('http://localhost:8000/reservar/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        if (resp.ok) {
          this.mensaje = "Reserva realizada con éxito.";
          setTimeout(() => {
            // Redirige a VistaBoxes y fuerza recarga
            this.$router.push({ path: '/boxes', query: { recargar: '1' } });
          }, 1200);
        } else {
          const data = await resp.json();
          this.error = data.detail || "Error al realizar la reserva.";
        }
      } catch (e) {
        this.error = "Error de conexión con el servidor.";
      }
    }
  }
};
</script>

<style scoped>
.confirmar-main {
  min-height: 100vh;
  background: #009999;
  display: flex;
  align-items: center;
  justify-content: center;
}
.confirmar-card {
  background: #fff;
  border-radius: 18px;
  padding: 2.5rem 2.5rem 2rem 2.5rem;
  min-width: 350px;
  max-width: 500px;
  box-shadow: 0 2px 18px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.confirmar-card h2 {
  color: #009999;
  font-size: 2rem;
  margin-bottom: 1.2rem;
  width: 100%;
  text-align: center;
}
.box-info, .horarios-info, .especialista-info {
  margin-bottom: 1.5rem;
  width: 100%;
}
.box-info h3, .horarios-info h3, .especialista-info h3 {
  color: #009999;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}
ul {
  padding-left: 1.2em;
}
.btn-volver {
  background: #75C2A6;
  color: #222;
  border: none;
  border-radius: 8px;
  padding: 0.7em 2em;
  font-size: 1.1em;
  margin-top: 1.2em;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s;
}
.btn-volver:hover {
  background: #009999;
  color: #fff;
}
.btn-confirmar {
  background: #009999;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 0.7em 2em;
  font-size: 1.1em;
  margin-top: 1.2em;
  margin-left: 1em;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s;
}
.btn-confirmar:disabled {
  background: #ccc;
  color: #888;
  cursor: not-allowed;
}
.especialista-info select {
  width: 100%;
  padding: 0.5em;
  border-radius: 6px;
  border: 1px solid #bbb;
  font-size: 1em;
  margin-top: 0.5em;
}
.botones-acciones {
  display: flex;
  gap: 1em;
  margin-top: 1.2em;
}
.btn-volver-horario {
  background: #75C2A6;
  color: #222;
  border: none;
  border-radius: 8px;
  padding: 0.7em 2em;
  font-size: 1.1em;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s;
}
.btn-volver-horario:hover {
  background: #009999;
  color: #fff;
}
</style>