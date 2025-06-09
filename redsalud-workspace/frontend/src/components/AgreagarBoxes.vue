
<template>
  <div class="coordinador-root">
    <!-- Barra lateral -->
    <div class="sidebar"></div>
    <div class="sidebar-btn1"></div>
    <div class="sidebar-btn2"></div>

    <!-- Contenedor principal -->
    <div class="main-card"></div>
    <div class="titulo">Asignación de Especialistas</div>

    <!-- Selector de Box -->
    <div class="label-box">Box:</div>
    <div class="box-select"></div>
    <div class="box-select-label">Seleccione un Box</div>

    <!-- Selector de Especialista -->
    <div class="label-especialista">Especialista:</div>
    <div class="especialista-select"></div>
    <div class="especialista-select-label">Seleccione un Especialista</div>

    <!-- Botón Asignar -->
    <div class="asignar-btn">
      <span class="asignar-text">Asignar</span>
    </div>
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
  left: 156px;
  top: 92px;
  background: #D9D9D9;
  border-radius: 12px;
}

/* Título */
.titulo {
  position: absolute;
  width: 605px;
  height: 95px;
  left: 205px;
  top: 130px;
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #000;
}

/* Box selector */
.label-box {
  position: absolute;
  width: 165px;
  height: 50px;
  left: 246px;
  top: 305px;
  font-weight: 400;
  font-size: 20px;
  line-height: 23px;
  display: flex;
  align-items: center;
  color: #000;
}
.box-select {
  position: absolute;
  width: 380px;
  height: 50px;
  left: 246px;
  top: 355px;
  background: #C4C4C4;
  border-radius: 12px;
}
.box-select-label {
  position: absolute;
  width: 165px;
  height: 50px;
  left: 299px;
  top: 355px;
  font-weight: 400;
  font-size: 20px;
  line-height: 23px;
  display: flex;
  align-items: center;
  color: #000;
}

/* Especialista selector */
.label-especialista {
  position: absolute;
  width: 165px;
  height: 50px;
  left: 246px;
  top: 418px;
  font-weight: 400;
  font-size: 20px;
  line-height: 23px;
  display: flex;
  align-items: center;
  color: #000;
}
.especialista-select {
  position: absolute;
  width: 528px;
  height: 50px;
  left: 246px;
  top: 462px;
  background: #C4C4C4;
  border-radius: 12px;
}
.especialista-select-label {
  position: absolute;
  width: 259px;
  height: 50px;
  left: 299px;
  top: 462px;
  font-weight: 400;
  font-size: 20px;
  line-height: 23px;
  display: flex;
  align-items: center;
  color: #000;
}

/* Botón Asignar */
.asignar-btn {
  position: absolute;
  width: 222px;
  height: 77px;
  left: 1137px;
  top: 811px;
  background: rgba(0, 153, 153, 0.53);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.asignar-text {
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  color: #fff;
  text-align: center;
  width: 222px;
  height: 77px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>