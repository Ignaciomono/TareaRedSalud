<template>
  <div class="login-root">
    <!-- Fondo y tarjeta central -->
    <div class="login-card">
      <div class="login-title">Iniciar Sesión</div>

      <!-- Usuario -->
      <div class="login-label usuario-label">Usuario</div>
      <input class="login-input usuario-input" type="text" />

      <!-- Línea bajo usuario -->
      <div class="login-line line1"></div>
      <div class="login-line line2"></div>

      <!-- Contraseña -->
      <div class="login-label password-label">Contraseña</div>
      <input class="login-input password-input" type="password" />

      <!-- Línea bajo contraseña -->
      <div class="login-line line3"></div>
      <div class="login-line line4"></div>

      <!-- Recordarme y Olvidé mi contraseña -->
      <div class="recordarme">Recordarme</div>
      <router-link to="/olvide-contraseña" class="olvide">Olvide mi contraseña</router-link>

      <!-- Botón LOGIN -->
      <div class="login-btn" @click="goToCoordinador">
        <span class="login-btn-text">LOGIN</span>
      </div>

      <!-- Botón para ir a Datos Médicos -->
      <router-link to="/datos-medicos">
        <button class="ir-datosmedicos-btn">Ir a Datos Médicos</button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    goToCoordinador() {
      this.$router.push('/coordinador');
    }
  }
}
</script>

<style scoped>
.login-root {
  position: relative;
  width: 1440px;
  height: 1024px;
  background: rgba(0, 153, 153, 0.53);
  font-family: 'Roboto', sans-serif;
}

/* Tarjeta central */
.login-card {
  position: absolute;
  width: 696px;
  height: 696px;
  left: 372px;
  top: 164px;
  background: #D9D9D9;
  backdrop-filter: blur(2px);
  border-radius: 10px;
}

/* Título */
.login-title {
  position: absolute;
  width: 294px;
  height: 56px;
  left: 573px;
  top: 231px;
  font-weight: 700;
  font-size: 48px;
  line-height: 56px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #85CCCC;
  transform: translate(-372px, -164px);
}

/* Usuario */
.login-label.usuario-label {
  position: absolute;
  width: 123px;
  height: 39px;
  left: 586px;
  top: 372px;
  font-weight: 400;
  font-size: 36px;
  line-height: 42px;
  color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  text-align: center;
  transform: translate(-372px, -164px);
}
.login-input.usuario-input {
  position: absolute;
  width: 216px;
  height: 39px;
  left: 504px;
  top: 372px;
  background: transparent;
  border: none;
  outline: none;
  font-size: 36px;
  color: #000;
  transform: translate(-372px, -164px);
}

/* Contraseña */
.login-label.password-label {
  position: absolute;
  width: 184px;
  height: 39px;
  left: 586px;
  top: 480px;
  font-weight: 400;
  font-size: 36px;
  line-height: 42px;
  color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  text-align: center;
  transform: translate(-372px, -164px);
}
.login-input.password-input {
  position: absolute;
  width: 216px;
  height: 39px;
  left: 504px;
  top: 480px;
  background: transparent;
  border: none;
  outline: none;
  font-size: 36px;
  color: #000;
  transform: translate(-372px, -164px);
}

/* Líneas */
.login-line {
  position: absolute;
  height: 0px;
  border: 1px solid #000000;
}
.line1 {
  width: 216px;
  left: 504px;
  top: 423px;
  transform: translate(-372px, -164px);
}
.line2 {
  width: 216px;
  left: 720px;
  top: 423px;
  transform: translate(-372px, -164px);
}
.line3 {
  width: 216px;
  left: 504px;
  top: 531px;
  transform: translate(-372px, -164px);
}
.line4 {
  width: 216px;
  left: 720px;
  top: 531px;
  transform: translate(-372px, -164px);
}

/* Recordarme */
.recordarme {
  position: absolute;
  width: 111px;
  height: 41px;
  left: 544px;
  top: 543px;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  text-align: center;
  transform: translate(-372px, -164px);
}

/* Olvide mi contraseña */
.olvide {
  box-sizing: border-box;
  position: absolute;
  width: 153px;
  height: 41px;
  left: 783px;
  top: 543px;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  color: #99CC00;
  border: 1px solid rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  text-align: center;
  justify-content: center;
  border-radius: 5px;
  transform: translate(-372px, -164px);
}

/* Botón LOGIN */
.login-btn {
  position: absolute;
  width: 294px;
  height: 70px;
  left: 573px;
  top: 639px;
  background: #99CC00;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  transform: translate(-372px, -164px);
}
.login-btn-text {
  font-weight: 700;
  font-size: 48px;
  line-height: 56px;
  color: #fff;
  text-align: center;
  width: 268px;
  height: 47px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Botón Ir a Datos Médicos */
.ir-datosmedicos-btn {
  margin-top: 30px;
  width: 220px;
  height: 45px;
  background: #009999;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  cursor: pointer;
  position: absolute;
  left: 50%;
  top: 750px;
  transform: translate(-50%, 0);
}
</style>