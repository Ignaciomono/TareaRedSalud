<!-- VistaCoordinadorEspecialistas.vue -->
<template>
  <div class="coordinador-especialistas-root">
    <!-- Barra lateral -->
    <div class="sidebar"></div>
    <!-- Foto de perfil (Ellipse) -->
    <div class="profile-pic"></div>
    <!-- Nombre coordinador -->
    <div class="coordinador-nombre">Coordinador RedSalud<br />Rodolfo Estevia</div>
    <!-- Botón Especialistas -->
    <div class="sidebar-btn-especialistas">Especialistas</div>
    <!-- Botón Boxes -->
    <div class="sidebar-btn-boxes" @click="goToBoxes">Boxes</div>
    <!-- Botón Salir -->
    <div class="sidebar-btn-salir" @click="salir">Salir</div>
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
      // Lógica para navegar a la sección de Boxes
      this.$router.push('/boxes');
    }
  }
}
</script>

<style scoped>
.coordinador-especialistas-root {
  position: relative;
  width: 1440px;
  height: 1024px;
  background: rgba(0, 153, 153, 0.53);
  font-family: 'Roboto', sans-serif;
}

/* Sidebar */
.sidebar {
  position: absolute;
  width: 250px;
  height: 1024px;
  left: 0;
  top: 0;
  background: #D9D9D9;
}

/* Foto de perfil (Ellipse) */
.profile-pic {
  position: absolute;
  width: 200px;
  height: 200px;
  left: 25px;
  top: 38px;
  background: #D9D9D9 url('https://via.placeholder.com/200') center/cover no-repeat;
  border-radius: 50%;
  border: 2px solid #bbb;
}

/* Nombre coordinador */
.coordinador-nombre {
  position: absolute;
  width: 160px;
  height: 38px;
  left: 45px;
  top: 244px;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #000;
  flex-direction: column;
}

/* Botón Especialistas */
.sidebar-btn-especialistas {
  position: absolute;
  width: 270px;
  height: 76px;
  left: 0;
  top: 342px;
  background: #75C2A6;
  border-radius: 0px 12px 12px 0px;
  font-weight: 500;
  font-size: 36px;
  line-height: 42px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #000;
  padding-left: 45px;
}

/* Botón Boxes */
.sidebar-btn-boxes {
  position: absolute;
  width: 249px;
  height: 76px;
  left: 1px;
  top: 436px;
  background: #75C2A6;
  border-radius: 0px 12px 12px 0px;
  font-weight: 500;
  font-size: 36px;
  line-height: 42px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #000;
  padding-left: 45px;
}

/* Botón Salir */
.sidebar-btn-salir {
  position: absolute;
  width: 249px;
  height: 76px;
  left: 1px;
  top: 530px;
  background: #ff6666;
  border-radius: 0px 12px 12px 0px;
  font-weight: 500;
  font-size: 36px;
  line-height: 42px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #fff;
  padding-left: 45px;
  cursor: pointer;
  transition: background 0.2s;
}
.sidebar-btn-salir:hover {
  background: #ff3333;
}
</style>