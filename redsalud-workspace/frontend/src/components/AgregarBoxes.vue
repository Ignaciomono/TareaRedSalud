<template>
  <div class="boxes-main">
    <!-- Sidebar -->
    <div class="sidebar">
      <div class="profile-pic"></div>
      <div class="coordinador-nombre">Coordinador RedSalud<br />Rodolfo Estevia</div>
      <div class="sidebar-btn" @click="goToCoordinador">Especialistas</div>
      <div class="sidebar-btn" @click="goToBoxes">Boxes</div>
      <div class="sidebar-btn sidebar-btn-salir" @click="salir">Salir</div>
    </div>
    <!-- Card principal -->
    <div class="boxes-root">
      <div class="boxes-card">
        <div class="boxes-header">
          <h2>Asignación de Especialistas</h2>
        </div>
        <form class="asignacion-form">
          <div class="form-group">
            <label for="box">Box:</label>
            <select id="box" v-model="boxSeleccionado">
              <option disabled value="">Seleccione un Box</option>
              <option v-for="box in boxes" :key="box" :value="box">{{ box }}</option> 
            </select>
          </div>
          <div class="form-group">
            <label for="especialista">Especialista:</label>
            <select id="especialista" v-model="especialistaSeleccionado">
              <option disabled value="">Seleccione un Especialista</option>
              <option
                v-for="esp in especialistas"
                :key="esp.nombre + esp.procedimiento"
                :value="esp.nombre + '|' + esp.procedimiento"
              >
                {{ esp.nombre }} - {{ esp.procedimiento }}
              </option>
            </select>
          </div>
          <button class="asignar-btn" type="button">Asignar</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AgregarBoxes',
  data() {
    return {
      boxes: this.generarBoxes(),
      especialistas: [
        { nombre: 'Dr. Pérez', procedimiento: 'Consulta médica' },
        { nombre: 'Dra. López', procedimiento: 'Ecografía Obstétrica' },
        { nombre: 'Dr. Soto', procedimiento: 'Control Post operatorio' },
        { nombre: 'Dra. Ruiz', procedimiento: 'Consulta médica' },
        { nombre: 'Dr. Díaz', procedimiento: 'Ecografía Obstétrica' }
      ],
      boxSeleccionado: '',
      especialistaSeleccionado: ''
    }
  },
  methods: {
    salir() {
      this.$router.push('/');
    },
    goToCoordinador() {
      this.$router.push('/coordinador');
    },
    goToBoxes() {
      this.$router.push('/boxes');
    },
    generarBoxes() {
      const boxes = [];
      for (let piso = 4; piso <= 13; piso++) {
        for (let i = 1; i <= 10; i++) {
          const numero = piso * 100 + i;
          boxes.push(`Piso ${piso} - Box ${numero}`);
        }
      }
      return boxes;
    },
  }
}
</script>

<style scoped>
.boxes-main {
  display: flex;
  width: 100vw;
  height: 100vh;
  background: #00a9ad;
}

/* Sidebar */
.sidebar {
  width: 250px;
  height: 100vh;
  background: #D9D9D9;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
  padding-top: 38px;
  position: relative;
}

.profile-pic {
  width: 200px;
  height: 200px;
  background: #D9D9D9 url('https://via.placeholder.com/200') center/cover no-repeat;
  border-radius: 50%;
  border: 2px solid #bbb;
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
.boxes-root {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.boxes-card {
  background: #fff;
  border-radius: 14px;
  padding: 2.5rem 2.5rem 2rem 2.5rem;
  min-width: 400px;
  max-width: 600px;
  width: 100%;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.boxes-header {
  width: 100%;
  margin-bottom: 2rem;
}
.boxes-header h2 {
  margin: 0;
  font-size: 2.2rem;
  font-weight: 500;
  text-align: center;
}

.asignacion-form {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

label {
  font-size: 1.2rem;
  color: #222;
  margin-bottom: 0.2rem;
}

select {
  height: 45px;
  border-radius: 10px;
  border: none;
  background: #d1d1d1;
  font-size: 1.1rem;
  padding: 0 1rem;
  color: #222;
  outline: none;
}

.asignar-btn {
  background: #75C2A6;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 2rem;
  padding: 0.6rem 2.2rem;
  cursor: pointer;
  font-weight: 500;
  align-self: flex-end;
  transition: background 0.2s;
}
.asignar-btn:hover {
  background: #009999;
}

/* Responsive */
@media (max-width: 900px) {
  .boxes-card {
    min-width: 0;
    padding: 1rem;
  }
  .boxes-header h2 {
    font-size: 1.2rem;
  }
  .asignar-btn {
    font-size: 1.2rem;
    padding: 0.5rem 1.2rem;
  }
}

.procedimiento-info {
  margin-top: 0.5rem;
  font-size: 1.1rem;
  color: #009999;
}
</style>