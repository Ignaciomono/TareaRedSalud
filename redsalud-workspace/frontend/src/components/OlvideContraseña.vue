<template>
  <div class="olvide-root">
    <div class="olvide-card">
      <!-- Flecha volver -->
      <span class="arrow-left" @click="goHome">&#8592;</span>
      <!-- Título -->
      <div class="olvide-title">Olvide mi contraseña</div>
      <!-- Subtítulo -->
      <div class="olvide-subtitle">Contactar con el administrador de RedSalud</div>
      <!-- Email con icono -->
      <span class="at-sign">@</span>
      <div class="olvide-email">adminredsalud@gmail.com</div>
      <!-- Teléfono con icono -->
      <span class="phone-icon">&#128222;</span>
      <div class="olvide-phone">+56 9 666 666 66</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OlvideContraseña',
  methods: {
    goHome() {
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
.olvide-root {
  position: relative;
  width: 1440px;
  height: 1024px;
  background: rgba(0, 153, 153, 0.53);
  font-family: 'Roboto', sans-serif;
}

/* Tarjeta central */
.olvide-card {
  position: absolute;
  width: 696px;
  height: 696px;
  left: 372px;
  top: 164px;
  background: #D9D9D9;
  backdrop-filter: blur(2px);
  border-radius: 10px;
}

/* Flecha volver */
.arrow-left {
  position: absolute;
  width: 48px;
  height: 48px;
  left: 395px;
  top: 183px;
  font-size: 48px;
  color: #1E1E1E;
  cursor: pointer;
}

/* Título */
.olvide-title {
  position: absolute;
  width: 455px;
  height: 56px;
  left: 493px;
  top: 231px;
  font-weight: 700;
  font-size: 48px;
  line-height: 56px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #85CCCC;
}

/* Subtítulo */
.olvide-subtitle {
  position: absolute;
  width: 470px;
  height: 75px;
  left: 485px;
  top: 351px;
  font-weight: 400;
  font-size: 36px;
  line-height: 42px;
  display: flex;
  align-items: center;
  text-align: center;
  color: rgba(0, 0, 0, 0.7);
}

/* Email */
.olvide-email {
  position: absolute;
  width: 204px;
  height: 21px;
  left: 521px;
  top: 479px;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  display: flex;
  align-items: center;
  text-align: center;
  text-decoration-line: underline;
  color: rgba(0, 0, 0, 0.7);
}

/* Teléfono */
.olvide-phone {
  position: absolute;
  width: 124px;
  height: 19px;
  left: 521px;
  top: 541px;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #000;
}

/* Iconos */
.at-sign {
  position: absolute;
  width: 28px;
  height: 25px;
  left: 490px;
  top: 479px;
  font-size: 24px;
  color: #1E1E1E;
  border: 4px solid #1E1E1E;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.phone-icon {
  position: absolute;
  width: 28px;
  height: 25px;
  left: 490px;
  top: 539px;
  font-size: 24px;
  color: #1E1E1E;
  border: 4px solid #1E1E1E;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>