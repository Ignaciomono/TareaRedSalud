<template>
  <div class="especialista-detalle-root">
    <!-- Sidebar -->
    <div class="sidebar">
      <div class="profile-pic"></div>
      <div class="coordinador-nombre">
        Coordinador RedSalud<br />{{ nombreUsuario }}
      </div>
      <div class="sidebar-btn" @click="goToCoordinador">Especialistas</div>
      <div class="sidebar-btn" @click="goToBoxes">Boxes</div>
      <div class="sidebar-btn sidebar-btn-salir" @click="salir">Salir</div>
    </div>
    <!-- Card principal con detalle -->
    <div class="especialista-detalle-card-root">
      <div v-if="especialistas.length > 0">
        <div
          class="especialista-detalle-card"
          v-for="(especialista, idx) in especialistas"
          :key="especialista.id"
        >
          <h2>Detalle Especialista {{ especialistas.length > 1 ? idx + 1 : '' }}</h2>
          <div class="detalle-row"><span class="detalle-label">Nombre:</span> {{ especialista.nombre }}</div>
          <div class="detalle-row"><span class="detalle-label">RUT:</span> {{ especialista.rut }}</div>
          <div class="detalle-row"><span class="detalle-label">Especialidad:</span> {{ especialista.especialidad }}</div>
          <div class="detalle-row" v-if="especialista.correo"><span class="detalle-label">Correo:</span> {{ especialista.correo }}</div>
          <div class="detalle-row" v-if="especialista.telefono"><span class="detalle-label">Teléfono:</span> {{ especialista.telefono }}</div>
          <div class="detalle-row" v-if="especialista.lunes"><span class="detalle-label">Lunes:</span> {{ especialista.lunes }}</div>
          <div class="detalle-row" v-if="especialista.martes"><span class="detalle-label">Martes:</span> {{ especialista.martes }}</div>
          <div class="detalle-row" v-if="especialista.miercoles"><span class="detalle-label">Miércoles:</span> {{ especialista.miercoles }}</div>
          <div class="detalle-row" v-if="especialista.jueves"><span class="detalle-label">Jueves:</span> {{ especialista.jueves }}</div>
          <div class="detalle-row" v-if="especialista.viernes"><span class="detalle-label">Viernes:</span> {{ especialista.viernes }}</div>
          <div class="detalle-row" v-if="especialista.sabado"><span class="detalle-label">Sábado:</span> {{ especialista.sabado }}</div>
          <div class="detalle-row" v-if="especialista.horario_lunes"><span class="detalle-label">Horario Lunes:</span> {{ especialista.horario_lunes }}</div>
          <div class="detalle-row" v-if="especialista.horario_martes"><span class="detalle-label">Horario Martes:</span> {{ especialista.horario_martes }}</div>
          <div class="detalle-row" v-if="especialista.horario_miercoles"><span class="detalle-label">Horario Miércoles:</span> {{ especialista.horario_miercoles }}</div>
          <div class="detalle-row" v-if="especialista.horario_jueves"><span class="detalle-label">Horario Jueves:</span> {{ especialista.horario_jueves }}</div>
          <div class="detalle-row" v-if="especialista.horario_viernes"><span class="detalle-label">Horario Viernes:</span> {{ especialista.horario_viernes }}</div>
          <div class="detalle-row" v-if="especialista.horario_sabado"><span class="detalle-label">Horario Sábado:</span> {{ especialista.horario_sabado }}</div>
          <div class="detalle-row" v-if="especialista.movimiento_agenda"><span class="detalle-label">Movimiento Agenda:</span> {{ especialista.movimiento_agenda }}</div>
          <div class="detalle-row" v-if="especialista.pctes_semanales"><span class="detalle-label">Pacientes Semanales:</span> {{ especialista.pctes_semanales }}</div>
          <div class="detalle-row" v-if="especialista.cantidad_horas"><span class="detalle-label">Cantidad Horas:</span> {{ especialista.cantidad_horas }}</div>
          <div class="detalle-row" v-if="especialista.cantidad_minutos"><span class="detalle-label">Cantidad Minutos:</span> {{ especialista.cantidad_minutos }}</div>
          <div class="detalle-row" v-if="especialista.dias_atencion"><span class="detalle-label">Días Atención:</span> {{ especialista.dias_atencion }}</div>
        </div>
      </div>
      <div v-else class="cargando">Cargando especialista...</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VistaEspecialista',
  data() {
    return {
      nombreUsuario: '',
      especialistas: []
    }
  },
  mounted() {
    this.nombreUsuario = localStorage.getItem('nombreUsuario') || 'Usuario';
    this.cargarEspecialistas();
  },
  methods: {
    goToCoordinador() {
      this.$router.push('/coordinador');
    },
    goToBoxes() {
      this.$router.push('/boxes');
    },
    salir() {
      localStorage.removeItem('nombreUsuario');
      this.$router.push('/');
    },
    async cargarEspecialistas() {
      // ids puede ser "5" o "5,7"
      const idsParam = this.$route.query.ids;
      if (!idsParam) return;
      const ids = idsParam.split(',').map(id => id.trim());
      try {
        // Si hay más de un id, busca todos
        const requests = ids.map(id =>
          fetch(`http://localhost:8000/datos_medicos/${id}/`).then(res => res.ok ? res.json() : null)
        );
        const results = await Promise.all(requests);
        this.especialistas = results.filter(e => e);
      } catch (e) {
        this.especialistas = [];
      }
    }
  }
}
</script>

<style scoped>
.especialista-detalle-root {
  width: 100vw;
  height: 100vh;
  background: rgba(0, 153, 153, 0.53);
  font-family: 'Roboto', sans-serif;
  display: flex;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Sidebar */
.sidebar {
  width: 250px;
  height: 100vh;
  background: #D9D9D9;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 0;
  box-sizing: border-box;
  position: relative;
}

.profile-pic {
  width: 200px;
  height: 200px;
  background: #D9D9D9 url('https://via.placeholder.com/200') center/cover no-repeat;
  border-radius: 50%;
  border: 2px solid #bbb;
  margin-top: 38px;
  margin-bottom: 10px;
}

.coordinador-nombre {
  width: 160px;
  margin: 10px 0 30px 0;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  color: #000;
}

.sidebar-btn {
  width: 90%;
  height: 56px;
  margin: 10px 0;
  border-radius: 12px;
  font-weight: 500;
  font-size: 28px;
  line-height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
  user-select: none;
}

.sidebar-btn {
  background: #75C2A6;
  color: #000;
}

.sidebar-btn-salir {
  background: #ff6666;
  color: #fff;
  margin-top: auto;
  margin-bottom: 30px;
}

.sidebar-btn-salir:hover {
  background: #ff3333;
}

/* Card principal */
.especialista-detalle-card-root {
  flex: 1;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  gap: 24px;
  padding: 40px 0;
  width: 100%;
}

.especialista-detalle-card {
  background: #fff;
  border-radius: 14px;
  padding: 2.5rem 2.5rem 2rem 2.5rem;
  min-width: 400px;
  max-width: 600px;
  width: 100%;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin: 0;
}

.especialista-detalle-card h2 {
  margin-bottom: 1.5rem;
  font-size: 2rem;
  font-weight: 500;
  color: #009999;
  text-align: center;
  width: 100%;
}

.detalle-row {
  margin-bottom: 0.7rem;
  font-size: 1.1rem;
  color: #222;
  width: 100%;
}

.detalle-label {
  font-weight: 600;
  color: #009999;
  margin-right: 8px;
}

.cargando {
  font-size: 1.2rem;
  color: #009999;
  text-align: center;
}
</style>