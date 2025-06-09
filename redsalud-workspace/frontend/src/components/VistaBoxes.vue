<!-- VistaCoordinadorBoxes.vue -->
<template>
  <div class="coordinador-root">
    <!-- Sidebar -->
    <div class="sidebar"></div>
    <div class="sidebar-btn1"></div>
    <div class="sidebar-btn2"></div>

    <!-- Contenedor principal -->
    <div class="main-card"></div>
    <div class="titulo">Gestión de Boxes</div>

    <!-- Botón Añadir -->
    <div class="add-btn">
      <span class="add-btn-text">Añadir</span>
    </div>

    <!-- Tabla principal -->
    <div class="table-bg"></div>
    <div class="table-header"></div>
    <div class="table-line line5"></div>
    <div class="table-line line7"></div>
    <div class="table-line line6"></div>
    <div class="table-line line8"></div>
    <div class="table-line line9"></div>
    <div class="table-line line10"></div>
    <div class="table-line line11"></div>

    <!-- Columnas -->
    <div class="col-box">Box</div>
    <div class="col-especialista">Especialista</div>

    <!-- Filas de ejemplo -->
    <div class="editar editar1">Editar</div>
    <div class="editar editar2">Editar</div>
    <div class="editar editar3">Editar</div>
    <div class="editar editar4">Editar</div>
    <div class="editar editar5">Editar</div>
  </div>
</template>

<style scoped>
.coordinador-root {
  position: relative;
  width: 1440px;
  height: 1024px;
  background: rgba(0, 153, 153, 0.53);
  font-family: 'Roboto', sans-serif;
}

/* Sidebar */
.sidebar {
  position: absolute;
  width: 99px;
  height: 1024px;
  left: 0;
  top: 0;
  background: #D9D9D9;
}
.sidebar-btn1 {
  position: absolute;
  width: 99px;
  height: 76px;
  left: 0;
  top: 342px;
  background: #75C2A6;
  border-radius: 0px 12px 12px 0px;
}
.sidebar-btn2 {
  position: absolute;
  width: 120px;
  height: 76px;
  left: 1px;
  top: 436px;
  background: #75C2A6;
  border-radius: 0px 12px 12px 0px;
}

/* Main card */
.main-card {
  position: absolute;
  width: 1238px;
  height: 840px;
  left: 151px;
  top: 90px;
  background: #D9D9D9;
  border-radius: 12px;
}

/* Título */
.titulo {
  position: absolute;
  width: 390px;
  height: 95px;
  left: 200px;
  top: 128px;
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #000;
}

/* Botón Añadir */
.add-btn {
  position: absolute;
  width: 222px;
  height: 77px;
  left: 1132px;
  top: 137px;
  background: rgba(0, 153, 153, 0.53);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.add-btn-text {
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  color: #fff;
  text-align: center;
}

/* Tabla principal */
.table-bg {
  position: absolute;
  width: 1144px;
  height: 630px;
  left: 198px;
  top: 252px;
  background: #C4C4C4;
  border-radius: 12px;
}
.table-header {
  position: absolute;
  width: 1144px;
  height: 105px;
  left: 198px;
  top: 252px;
  background: #75C2A6;
  border-radius: 12px 12px 0px 0px;
}

/* Líneas */
.table-line {
  position: absolute;
  border: 1px solid #000;
}
.line5 {
  width: 630px;
  left: 1132px;
  top: 252px;
  transform: rotate(90deg);
}
.line7 {
  width: 630px;
  left: 427px;
  top: 252px;
  transform: rotate(90deg);
}
.line6 {
  width: 1144px;
  left: 1342px;
  top: 357px;
  transform: rotate(180deg);
}
.line8 {
  width: 1142px;
  left: 1342px;
  top: 462px;
  transform: rotate(180deg);
}
.line9 {
  width: 1144px;
  left: 1342px;
  top: 567px;
  transform: rotate(180deg);
}
.line10 {
  width: 1144px;
  left: 1342px;
  top: 672px;
  transform: rotate(180deg);
}
.line11 {
  width: 1144px;
  left: 1342px;
  top: 777px;
  transform: rotate(180deg);
}

/* Columnas */
.col-box {
  position: absolute;
  width: 227px;
  height: 105px;
  left: 200px;
  top: 252px;
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #000;
}
.col-especialista {
  position: absolute;
  width: 705px;
  height: 105px;
  left: 427px;
  top: 252px;
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #000;
}

/* Editar botones de ejemplo */
.editar {
  position: absolute;
  width: 210px;
  height: 105px;
  left: 1132px;
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #000;
  background: transparent;
}
.editar1 { top: 357px; }
.editar2 { top: 462px; }
.editar3 { top: 567px; }
.editar4 { top: 672px; }
.editar5 { top: 777px; }
</style>