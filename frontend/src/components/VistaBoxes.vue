<!-- VistaCoordinadorBoxes.vue -->
<template>
  <div class="boxes-main">
    <div class="sidebar">
      <div class="profile-pic"></div>
      <div class="coordinador-nombre">Coordinador RedSalud<br />Rodolfo Estevia</div>
      <div class="sidebar-btn" @click="goToCoordinador">Especialistas</div>
      <div class="sidebar-btn">Boxes</div>
      <div class="sidebar-btn sidebar-btn-salir" @click="salir">Salir</div>
    </div>
    <div class="boxes-root">
      <div class="boxes-card">
        <div class="boxes-header">
          <h2>Gestión de Boxes</h2>
          <button class="add-btn" @click="goToAgregarBoxes">Añadir</button>
        </div>
        <table class="boxes-table">
          <thead>
            <tr>
              <th>Box</th>
              <th>Especialista</th>
              <th>Procedimiento</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(box, i) in boxes" :key="i" >
              <td>{{ box.nombre }}</td>
              <td>{{ box.especialista }}</td>
              <td>{{ box.procedimiento }}</td>
              <td><button class="edit-btn">Editar</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VistaBoxes',
  data() {
    return {
      boxes: [
        { nombre: 'Box 1', especialista: 'Dr. Pérez', procedimiento: 'Consulta médica' },
        { nombre: 'Box 2', especialista: 'Dra. López', procedimiento: 'Ecografía Obstétrica' },
        { nombre: 'Box 3', especialista: 'Dr. Soto', procedimiento: 'Control Post operatorio' },
        { nombre: 'Box 4', especialista: 'Dra. Ruiz', procedimiento: 'Consulta médica' },
        { nombre: 'Box 5', especialista: 'Dr. Díaz', procedimiento: 'Ecografía Obstétrica' }
      ]
    }
  },
  methods: {
    salir() {
      this.$router.push('/');
    },
    goToAgregarBoxes() {
      this.$router.push('/agregar-boxes');
    },
    goToCoordinador() {
      this.$router.push('/coordinador');
    }
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

/* Boxes content */
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
  min-width: 600px;
  max-width: 900px;
  width: 100%;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}

.boxes-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.boxes-header h2 {
  margin: 0;
  font-size: 2.2rem;
  font-weight: 500;
}

.add-btn {
  background: #75C2A6;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 1.3rem;
  padding: 0.6rem 2.2rem;
  cursor: pointer;
  font-weight: 500;
  transition: background 0.2s;
}
.add-btn:hover {
  background: #009999;
}

.boxes-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  background: #e5e5e5;
  border-radius: 10px;
  overflow: hidden;
}

.boxes-table th, .boxes-table td {
  padding: 1rem 1.2rem;
  font-size: 1.5rem;
  text-align: left;
}

.boxes-table thead th {
  background: #75C2A6;
  color: #222;
  font-weight: 500;
  border: none;
}

.boxes-table tbody tr {
  border-top: 1px solid #bbb;
}

.boxes-table tbody tr:last-child td {
  border-bottom: none;
}

.edit-btn {
  background: transparent;
  color: #222;
  border: none;
  font-size: 1.3rem;
  cursor: pointer;
  font-weight: 500;
  transition: color 0.2s;
}
.edit-btn:hover {
  color: #009999;
}

/* Responsive */
@media (max-width: 900px) {
  .boxes-card {
    min-width: 0;
    padding: 1rem;
  }
  .boxes-table th, .boxes-table td {
    font-size: 1rem;
    padding: 0.5rem 0.7rem;
  }
  .boxes-header h2 {
    font-size: 1.2rem;
  }
}
</style>