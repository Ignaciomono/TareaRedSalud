<!-- VistaCoordinadorEspecialistas.vue -->
<template>
  <div class="coordinador-especialistas-root">
    <div class="sidebar">
      <div class="profile-pic"></div>
      <div class="coordinador-nombre">Coordinador RedSalud<br />Rodolfo Estevia</div>
      <div class="sidebar-btn sidebar-btn-especialistas">Especialistas</div>
      <div class="sidebar-btn sidebar-btn-boxes" @click="goToBoxes">Boxes</div>
      <div class="sidebar-btn sidebar-btn-salir" @click="salir">Salir</div>
    </div>
    <!-- Aquí puedes agregar el contenido principal a la derecha del sidebar -->
  </div>
</template>

<script>
export default {
  name: 'Coordinador',
  methods: {
    salir() {
      this.$router.push('/');
    },
    goToBoxes() {
      this.$router.push('/boxes');
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
  /* Quita el padding-top para que la imagen quede arriba */
  padding-top: 0;
  box-sizing: border-box;
  position: relative;
}

/* Foto de perfil (Ellipse) */
.profile-pic {
  width: 200px;
  height: 200px;
  background: #D9D9D9 url('https://via.placeholder.com/200') center/cover no-repeat;
  border-radius: 50%;
  border: 2px solid #bbb;
  margin-top: 38px;
  margin-bottom: 10px;
}

/* Nombre coordinador */
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

/* Botones sidebar */
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

.sidebar-btn-especialistas,
.sidebar-btn-boxes {
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
</style>