<!-- VistaCoordinadorEspecialistas.vue -->
<template>
  <div class="coordinador-especialistas-root">
    <div class="sidebar">
      <div class="profile-pic"></div>
      <div class="coordinador-nombre">
        Coordinador RedSalud<br />{{ nombreUsuario }}
      </div>
      <div class="sidebar-btn sidebar-btn-activo">Especialistas</div>
      <div class="sidebar-btn" @click="goToBoxes">Boxes</div>
      <div class="sidebar-btn sidebar-btn-salir" @click="salir">Salir</div>
    </div>
    <!-- Listado de especialistas a la derecha -->
    <div class="especialistas-list-root">
      <h2>Especialistas</h2>
      <div class="buscador-root">
        <input
          type="text"
          v-model="busqueda"
          placeholder="Buscar por nombre o especialidad..."
          class="buscador-input"
        />
      </div>
      <div v-if="especialistasFiltrados.length === 0">No se encontraron especialistas.</div>
      <div v-else>
        <div
          v-for="(esp, idx) in especialistasFiltrados"
          :key="esp.nombre + '-' + esp.especialidad"
          class="especialista-card"
        >
          <div class="especialista-nombre">{{ esp.nombre }}</div>
          <div class="especialista-especialidad">{{ esp.especialidad }}</div>
          <button class="ver-btn" @click="verEspecialista(esp)">Ver</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Coordinador',
  data() {
    return {
      nombreUsuario: '',
      especialistas: [],
      busqueda: ''
    }
  },
  computed: {
    especialistasFiltrados() {
      if (!this.busqueda) return this.especialistas;
      const texto = this.busqueda.toLowerCase();
      return this.especialistas.filter(e =>
        (e.nombre && e.nombre.toLowerCase().includes(texto)) ||
        (e.especialidad && e.especialidad.toLowerCase().includes(texto))
      );
    }
  },
  mounted() {
    this.nombreUsuario = localStorage.getItem('nombreUsuario') || 'Usuario';
    this.cargarEspecialistas();
  },
  methods: {
    salir() {
      localStorage.removeItem('nombreUsuario');
      this.$router.push('/');
    },
    goToBoxes() {
      this.$router.push('/boxes');
    },
    async cargarEspecialistas() {
      try {
        const res = await fetch('http://localhost:8000/datos_medicos/');
        let data = await res.json();
        // Agrupa especialistas por nombre+especialidad y guarda todos los ids
        const map = {};
        data.forEach(item => {
          const key = item.nombre + '|' + item.especialidad;
          if (!map[key]) {
            map[key] = {
              nombre: item.nombre,
              especialidad: item.especialidad,
              ids: [item.id], // lista de ids
              ruts: [item.rut]
            };
          } else {
            map[key].ids.push(item.id);
            map[key].ruts.push(item.rut);
          }
        });
        // Ordena por nombre
        this.especialistas = Object.values(map).sort((a, b) =>
          a.nombre.localeCompare(b.nombre)
        );
      } catch (e) {
        this.especialistas = [];
      }
    },
    verEspecialista(esp) {
      // Si hay más de un id, los manda como string separados por coma
      const ids = esp.ids.join(',');
      this.$router.push({
        path: '/vista-especialista',
        query: { ids, nombre: esp.nombre, especialidad: esp.especialidad }
      });
    }
  }
}
</script>

<style scoped>
.coordinador-especialistas-root {
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

.sidebar-btn-activo {
  background: #009999;
  color: #fff;
  pointer-events: none;
  cursor: default;
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

/* Especialistas List */
.especialistas-list-root {
  flex: 1;
  padding: 40px 30px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.especialistas-list-root h2 {
  margin-bottom: 20px;
  font-size: 2rem;
  color: #222;
}

.especialista-card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  padding: 18px 28px;
  margin-bottom: 18px;
  min-width: 320px;
  display: flex;
  align-items: center;
  gap: 30px;
}

.especialista-nombre {
  font-size: 1.2rem;
  font-weight: 600;
  color: #009999;
  min-width: 140px;
}

.especialista-especialidad {
  font-size: 1.1rem;
  color: #222;
  min-width: 140px;
}

.ver-btn {
  background: #75C2A6;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  padding: 8px 22px;
  cursor: pointer;
  transition: background 0.2s;
}
.ver-btn:hover {
  background: #009999;
}

.buscador-root {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  margin-bottom: 18px;
}
.buscador-input {
  width: 350px;
  padding: 10px 18px;
  border-radius: 8px;
  border: 1px solid #bbb;
  font-size: 1.1rem;
  outline: none;
}
</style>