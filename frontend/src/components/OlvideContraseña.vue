<template>
  <div class="olvide-root">
    <div class="olvide-card">
      <!-- Flecha volver -->
      <div class="arrow-left" @click="volver" aria-label="Volver" tabindex="0">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
          <path d="M15 18l-6-6 6-6" stroke="#1E1E1E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <!-- Título -->
      <div class="olvide-title">Olvide mi contraseña</div>
      <!-- Subtítulo -->
      <div class="olvide-subtitle">Contactar con el administrador de RedSalud</div>
      <!-- Email con icono -->
      <div class="olvide-row">
        <span class="at-sign">@</span>
        <span class="olvide-email">adminredsalud@gmail.com</span>
      </div>
      <!-- Teléfono con icono -->
      <div class="olvide-row">
        <span class="phone-icon">&#128222;</span>
        <span class="olvide-phone">+56 9 666 666 66</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OlvideContraseña',
  methods: {
    volver() {
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
.olvide-root {
  min-height: 100vh;
  min-width: 100vw;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 153, 153, 0.53);
  font-family: 'Roboto', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
}

.olvide-card {
  background: #D9D9D9;
  border-radius: 14px;
  padding: 2.5rem 2rem 2.5rem 2rem;
  min-width: 320px;
  max-width: 420px;
  width: 100%;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.arrow-left {
  position: absolute;
  left: 1.5rem;
  top: 1.5rem;
  font-size: 2rem;
  color: #1E1E1E;
  cursor: pointer;
  transition: color 0.2s;
}
.arrow-left:hover {
  color: #009999;
}

.olvide-title {
  font-weight: 700;
  font-size: 2rem;
  line-height: 2.5rem;
  color: #009999;
  margin-top: 1.5rem;
  margin-bottom: 1rem;
  text-align: center;
}

.olvide-subtitle {
  font-weight: 400;
  font-size: 1.2rem;
  line-height: 1.5rem;
  color: rgba(0, 0, 0, 0.7);
  margin-bottom: 2.2rem;
  text-align: center;
}

.olvide-row {
  display: flex;
  align-items: center;
  margin-bottom: 1.2rem;
  width: 100%;
  justify-content: center;
}

.at-sign, .phone-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  color: #1E1E1E;
  border: 2px solid #1E1E1E;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  margin-right: 0.7rem;
  background: #fff;
}

.olvide-email {
  font-size: 1rem;
  color: rgba(0, 0, 0, 0.7);
  text-decoration: underline;
  word-break: break-all;
}

.olvide-phone {
  font-size: 1rem;
  color: #000;
}

@media (max-width: 500px) {
  .olvide-card {
    min-width: 0;
    max-width: 98vw;
    padding: 1rem 0.5rem 1.5rem 0.5rem;
  }
  .olvide-title {
    font-size: 1.2rem;
  }
  .olvide-subtitle {
    font-size: 1rem;
  }
}
</style>