<!-- VistaCoordinadorBoxes.vue -->
<template>
  <div class="boxes-main">
    <!-- Sidebar -->
    <div class="sidebar">
      <div class="profile-pic"></div>
      <div class="coordinador-nombre">
        Coordinador RedSalud<br />{{ nombreUsuario }}
      </div>
      <div class="sidebar-btn" @click="goToCoordinador">Especialistas</div>
      <div class="sidebar-btn sidebar-btn-activo">Boxes</div>
      <div class="sidebar-btn sidebar-btn-salir" @click="salir">Salir</div>
    </div>
    <!-- Card principal con listado de boxes -->
    <div class="boxes-card-root">
      <div class="boxes-card">
        <h2>Gestión de Boxes</h2>
        <div class="piso-selector">
          <label for="piso">Selecciona un piso:</label>
          <select id="piso" v-model="pisoSeleccionado">
            <option v-for="piso in pisosDisponibles" :key="piso" :value="piso">
              Piso {{ piso }}
            </option>
          </select>
        </div>
        <div v-if="cargando" class="cargando">Cargando boxes...</div>
        <div v-else-if="error" class="cargando" style="color:red;">{{ error }}</div>
        <div v-else class="boxes-list">
          <div
            class="box-detalle-card"
            v-for="box in boxesFiltrados"
            :key="box.codigo"
          >
            <div class="box-detalle-header">
              <span class="detalle-label">Código:</span>
              <span class="detalle-codigo">{{ box.codigo }}</span>
            </div>
            <div class="box-detalle-nombre">
              <span class="detalle-label">Nombre:</span>
              <span class="detalle-nombre">{{ box.nombre }}</span>
            </div>
            <button class="edit-btn" @click="goToHorario(box)">Ver Horario</button>
          </div>
          <div v-if="boxesFiltrados.length === 0" class="cargando">No hay boxes para este piso.</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VistaBoxes',
  data() {
    return {
      nombreUsuario: '',
      boxes: [],
      pisosDisponibles: [4, 5, 6, 7, 8, 9, 10, 12, 13],
      pisoSeleccionado: 4,
      cargando: false,
      error: null,
    }
  },
  computed: {
    boxesFiltrados() {
      // Filtra por piso y luego ordena de menor a mayor por código numérico
      return this.boxes
        .filter(box => {
          const codigo = box.codigo ? box.codigo.toString() : '';
          const piso = this.pisoSeleccionado.toString();
          if (['10', '12', '13'].includes(piso)) {
            return codigo.startsWith(piso);
          }
          return codigo.startsWith(piso);
        })
        .sort((a, b) => {
          // Ordenar de menor a mayor por código numérico
          const codA = parseInt(a.codigo, 10);
          const codB = parseInt(b.codigo, 10);
          return codA - codB;
        });
    }
  },
  methods: {
    salir() {
      this.$router.push('/');
    },
    goToCoordinador() {
      this.$router.push('/coordinador');
    },
    goToHorario(box) {
      this.$router.push({ path: '/horario', query: { codigo: box.codigo, nombre: box.nombre } });
    },
    async cargarBoxes() {
      this.cargando = true;
      this.error = null;
      try {
        const url = 'http://localhost:8000/boxes/';
        const response = await fetch(url);
        if (!response.ok) throw new Error('Error al cargar boxes');
        const data = await response.json();
        this.boxes = Array.isArray(data) ? data : [];
      } catch (e) {
        this.error = e.message || 'Error de red';
      } finally {
        this.cargando = false;
      }
    }
  },
  created() {
    this.nombreUsuario = localStorage.getItem('nombreUsuario') || 'Usuario';
    this.cargarBoxes();
  },
  watch: {
    '$route.query.recargar'(val) {
      if (val) this.cargarBoxes();
    }
  }
}
</script>

<style scoped>
.boxes-main {
  width: 100vw;
  height: 100vh;
  background: #009999;
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
  width: 120px;
  height: 120px;
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
  height: 48px;
  margin: 10px 0;
  border-radius: 12px;
  font-weight: 500;
  font-size: 20px;
  line-height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  background: #75C2A6;
  color: #000;
  user-select: none;
  transition: background 0.2s, color 0.2s;
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
.boxes-card-root {
  flex: 1;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  gap: 24px;
  padding: 40px 0;
  width: 100%;
}

.boxes-card {
  background: #fff;
  border-radius: 18px;
  padding: 2.5rem 2.5rem 2rem 2.5rem;
  min-width: 0;
  width: 98%;
  max-width: 600px;
  margin: 2vh auto 0 auto;
  box-shadow: 0 2px 18px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  height: auto;
}

.boxes-card h2 {
  margin-bottom: 1.5rem;
  font-size: 2.3rem;
  font-weight: 500;
  color: #009999;
  text-align: center;
  width: 100%;
}

.piso-selector {
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.piso-selector label {
  font-size: 1.2rem;
  font-weight: 500;
}

.piso-selector select {
  font-size: 1.2rem;
  padding: 0.3rem 1rem;
  border-radius: 8px;
  border: 1px solid #bbb;
}

/* SCROLLABLE LISTA DE BOXES */
.boxes-list {
  width: 100%;
  max-height: 420px;
  overflow-y: auto;
  margin-top: 1rem;
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.box-detalle-card {
  background: #f9f9f9;
  border-radius: 14px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  padding: 1.2rem 1.5rem 1.2rem 1.5rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  min-height: 80px;
}

.box-detalle-header, .box-detalle-nombre {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 0.5rem;
}

.detalle-label {
  font-weight: 600;
  color: #009999;
  margin-right: 4px;
  font-size: 1.08rem;
}

.detalle-codigo {
  font-weight: 600;
  color: #222;
  font-size: 1.08rem;
}

.detalle-nombre {
  color: #222;
  font-size: 1.08rem;
}

.edit-btn {
  background: #75C2A6;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 1.08rem;
  padding: 0.5rem 1.5rem;
  cursor: pointer;
  font-weight: 500;
  transition: background 0.2s;
  min-width: 110px;
  align-self: center;
  margin-left: auto;
}
.edit-btn:hover {
  background: #009999;
}

.cargando {
  font-size: 1.2rem;
  color: #009999;
  text-align: center;
  margin-top: 2rem;
}
.sidebar-btn-activo {
  background: #009999;
  color: #fff;
  pointer-events: none;
  cursor: default;
}
</style>