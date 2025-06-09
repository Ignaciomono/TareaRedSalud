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
html, body {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  min-height: 100vh;
  min-width: 100vw;
  width: 100vw;
  height: 100vh;
}

.login-root {
  width: 100vw;
  height: 100vh;
  font-family: 'Roboto', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.login-card {
  width: 90vw;
  max-width: 500px;
  min-width: 280px;
  background: #D9D9D9;
  backdrop-filter: blur(2px);
  border-radius: 10px;
  padding: 2.5rem 2rem 3.5rem 2rem;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.login-title {
  font-weight: 700;
  font-size: 2.2rem;
  line-height: 2.5rem;
  color: #85CCCC;
  margin-bottom: 2.5rem;
  text-align: center;
}

.login-label {
  font-size: 1.5rem;
  color: rgba(0, 0, 0, 0.7);
  margin-bottom: 0.5rem;
  width: 100%;
  text-align: left;
}

.login-input {
  width: 100%;
  font-size: 1.3rem;
  background: transparent;
  border: none;
  border-bottom: 2px solid #000;
  outline: none;
  margin-bottom: 1.5rem;
  padding: 0.5rem 0;
}

.login-line {
  display: none;
}

.recordarme {
  font-size: 1rem;
  color: rgba(0, 0, 0, 0.7);
  margin-bottom: 1rem;
  width: 100%;
  text-align: left;
}

.olvide {
  font-size: 1rem;
  color: #99CC00;
  border: 1px solid rgba(0, 0, 0, 0.4);
  border-radius: 5px;
  padding: 0.2rem 0.5rem;
  margin-bottom: 1.5rem;
  margin-left: auto;
  text-align: right;
  display: inline-block;
}

.login-btn {
  width: 100%;
  max-width: 300px;
  height: 55px;
  background: #99CC00;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1.5rem auto 0 auto;
  cursor: pointer;
  transition: background 0.2s;
}
.login-btn:hover {
  background: #7fbf00;
}
.login-btn-text {
  font-weight: 700;
  font-size: 2rem;
  color: #fff;
  text-align: center;
}

.ir-datosmedicos-btn {
  margin-top: 2.5rem;
  width: 80vw;
  max-width: 220px;
  height: 45px;
  background: #009999;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-family: 'Roboto', sans-serif;
  cursor: pointer;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

@media (max-width: 600px) {
  .login-card {
    padding: 1.5rem 1rem 2rem 1rem;
    max-width: 98vw;
  }
  .login-title {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
  }
  .login-btn {
    height: 45px;
    font-size: 1.2rem;
  }
  .login-btn-text {
    font-size: 1.2rem;
  }
}
</style>