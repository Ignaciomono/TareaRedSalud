<template>
  <div class="horario-main">
    <!-- Sidebar igual que en VistaBoxes -->
    <div class="sidebar">
      <div class="profile-pic"></div>
      <div class="coordinador-nombre">
        Coordinador RedSalud<br />{{ nombreUsuario }}
      </div>
      <div class="sidebar-btn" @click="goToCoordinador">Especialistas</div>
      <div class="sidebar-btn" @click="goToBoxes">Boxes</div>
      <div class="sidebar-btn sidebar-btn-salir" @click="salir">Salir</div>
    </div>
    <!-- Card principal con scroll -->
    <div class="horario-card-root">
      <div class="horario-card">
        <h2>{{ titulo }}</h2>
        <button v-if="!modoReserva" class="btn-reservar" @click="activarReserva">Reservar</button>
        <div class="horario-scroll">
          <table class="horario-table">
            <thead>
              <tr>
                <th>Hora</th>
                <th v-for="dia in DIAS" :key="dia">{{ dia }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(hora, rowIdx) in horas" :key="hora">
                <td class="hora-label">{{ hora }}</td>
                <template v-for="(dia, colIdx) in DIAS">
                  <td
                    v-if="!estaOcupada(dia, hora)"
                    :rowspan="getRowspan(dia, hora)"
                    :class="[getReservaClase(dia, hora), celdaSeleccionada(dia, hora) ? 'seleccionada' : '']"
                    @click="seleccionarCelda(dia, hora)"
                    :style="modoReserva && !getReserva(dia, hora) ? 'cursor:pointer' : ''"
                  >
                    <div v-if="getReserva(dia, hora)">
                      <span class="reserva-nombre">{{ getReserva(dia, hora).nombre }}</span>
                      <span class="reserva-proc" v-if="getReserva(dia, hora).procedimiento && getReserva(dia, hora).procedimiento !== 'x'">
                        ({{ getReserva(dia, hora).procedimiento }})
                      </span>
                    </div>
                  </td>
                </template>
              </tr>
            </tbody>
          </table>
        </div>
        <button v-if="modoReserva" class="btn-ok" :disabled="!seleccion.length" @click="confirmarReserva">OK</button>
        <div class="leyenda">
          <div class="leyenda-block" style="background:#75C2A6"></div> Reserva
        </div>
        <div v-if="!reservas.length" class="cargando">No hay reservas para este box.</div>
      </div>
    </div>
  </div>
</template>

<script>
const DIAS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
const HORA_INICIO = 8 * 60 + 15; // 8:15
const HORA_FIN = 20 * 60; // 20:00
const INTERVALO = 15; // minutos

function minutosAHoraStr(mins) {
  const h = Math.floor(mins / 60);
  const m = mins % 60;
  return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}`;
}

function horaStrAMinutos(str) {
  const [h, m] = str.split(':').map(Number);
  return h * 60 + m;
}

export default {
  name: 'Horario',
  data() {
    return {
      nombreUsuario: '',
      titulo: '',
      DIAS,
      horas: [],
      reservas: [],
      reservasMapa: {},
      cargando: true,
      modoReserva: false,
      seleccion: [],
      boxInfo: {},
    };
  },
  created() {
    this.nombreUsuario = localStorage.getItem('nombreUsuario') || 'Usuario';
    this.generarHoras();
    this.cargarReservas();
  },
  watch: {
  '$route'(to, from) {
    // Siempre recarga reservas al entrar a la ruta
    this.cargarReservas();
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
    generarHoras() {
      const horas = [];
      for (let m = HORA_INICIO; m <= HORA_FIN; m += INTERVALO) {
        horas.push(minutosAHoraStr(m));
      }
      this.horas = horas;
    },
    activarReserva() {
      this.modoReserva = true;
      this.seleccion = [];
    },
    seleccionarCelda(dia, hora) {
      if (!this.modoReserva) return;
      if (this.getReserva(dia, hora)) return;
      const idx = this.seleccion.findIndex(sel => sel.dia === dia && sel.hora === hora);
      if (idx >= 0) {
        this.seleccion.splice(idx, 1);
      } else {
        this.seleccion.push({ dia, hora });
      }
    },
    celdaSeleccionada(dia, hora) {
      return this.seleccion.some(sel => sel.dia === dia && sel.hora === hora);
    },
    async cargarReservas() {
      this.cargando = true;
      try {
        const boxCodigo = this.$route.query.codigo;
        const response = await fetch(`http://localhost:8000/boxes/${boxCodigo}/`);
        if (!response.ok) throw new Error('Error al cargar reservas');
        const data = await response.json();
        this.titulo = data.nombre || 'Horario del Box';
        this.reservas = this.parseReservasString(data.reservas || '');
        this.boxInfo = data; // Guardar info completa del box
        if (!this.reservas.length) {
          this.titulo = 'No hay reservas para este box';
        }
      } catch (e) {
        this.titulo = 'Error al cargar horario';
        this.reservas = [];
      }
      this.prepararMapaReservas();
      this.cargando = false;
    },
    confirmarReserva() {
      // Redirige a ConfirmarReserva.vue pasando la selección y el código del box
      this.$router.push({
        path: '/confirmar-reserva',
        query: {
          seleccion: JSON.stringify(this.seleccion),
          codigo: this.boxInfo.codigo
        }
      });
    },
    parseReservasString(reservasStr) {
      if (!reservasStr) return [];
      return reservasStr.split('\n').map(linea => {
        const partes = linea.split('|').map(p => p.trim());
        if (partes.length !== 4) return null;
        const [nombre, procedimiento, dia, horario] = partes;
        if (!horario || !horario.includes('a')) return null;
        const [horaInicio, horaFin] = horario.split('a').map(h => h.trim());
        // Validar formato HH:MM
        const horaRegex = /^\d{2}:\d{2}$/;
        if (!horaInicio || !horaFin || !horaRegex.test(horaInicio) || !horaRegex.test(horaFin)) return null;
        return {
          nombre: nombre.replace(/\(\*\)/g, '').trim(),
          procedimiento,
          dia,
          horaInicio,
          horaFin
        };
      }).filter(r => r && r.horaInicio && r.horaFin);
    },
    prepararMapaReservas() {
      this.reservasMapa = {};
      for (const dia of DIAS) {
        this.reservasMapa[dia] = {};
        for (const hora of this.horas) {
          this.reservasMapa[dia][hora] = { reserva: null, rowspan: 1, ocupada: false };
        }
      }
      for (const reserva of this.reservas) {
        const dia = reserva.dia;
        if (!reserva.horaInicio || !reserva.horaFin) continue;
        // Validar formato HH:MM
        const horaRegex = /^\d{2}:\d{2}$/;
        if (!horaRegex.test(reserva.horaInicio) || !horaRegex.test(reserva.horaFin)) continue;
        const inicio = horaStrAMinutos(reserva.horaInicio);
        const fin = horaStrAMinutos(reserva.horaFin);
        let primerBloque = null;
        let bloques = 0;
        for (let m = HORA_INICIO, idx = 0; m < HORA_FIN; m += INTERVALO, idx++) {
          const horaStr = minutosAHoraStr(m);
          if (m >= inicio && m < fin) {
            if (primerBloque === null) primerBloque = horaStr;
            bloques++;
          }
        }
        if (primerBloque && bloques > 0) {
          this.reservasMapa[dia][primerBloque] = {
            reserva,
            rowspan: bloques,
            ocupada: false
          };
          let m = horaStrAMinutos(primerBloque) + INTERVALO;
          for (let i = 1; i < bloques; i++, m += INTERVALO) {
            const horaStr = minutosAHoraStr(m);
            this.reservasMapa[dia][horaStr] = {
              reserva: null,
              rowspan: 0,
              ocupada: true
            };
          }
        }
      }
    },
    getReserva(dia, hora) {
      return this.reservasMapa[dia] && this.reservasMapa[dia][hora]
        ? this.reservasMapa[dia][hora].reserva
        : null;
    },
    getRowspan(dia, hora) {
      return this.reservasMapa[dia] && this.reservasMapa[dia][hora]
        ? this.reservasMapa[dia][hora].rowspan
        : 1;
    },
    estaOcupada(dia, hora) {
      return this.reservasMapa[dia] && this.reservasMapa[dia][hora]
        ? this.reservasMapa[dia][hora].ocupada
        : false;
    },
    getReservaClase(dia, hora) {
      return this.getReserva(dia, hora) ? 'reserva-block' : '';
    },
    getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    },
    sumarIntervalo(hora, minutos) {
      const [h, m] = hora.split(':').map(Number);
      const total = h * 60 + m + minutos;
      const nh = Math.floor(total / 60);
      const nm = total % 60;
      return `${nh.toString().padStart(2, '0')}:${nm.toString().padStart(2, '0')}`;
    },
  }
};
</script>

<style scoped>
.horario-main {
  width: 100vw;
  min-height: 100vh;
  background: #009999;
  font-family: 'Roboto', sans-serif;
  display: flex;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Sidebar igual que en VistaBoxes */
.sidebar {
  width: 250px;
  height: 100vh;
  background: #D9D9D9;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 0;
  box-sizing: border-box;
  position: relative;
}

.profile-pic {
  width: 120px;
  height: 120px;
  background: #D9D9D9 url('https://via.placeholder.com/200') center/cover no-repeat;
  border-radius: 50%;
  border: 2px solid #bbb;
  margin-top: 38px;
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
  height: 48px;
  margin: 10px 0;
  border-radius: 12px;
  font-weight: 500;
  font-size: 20px;
  line-height: 38px;
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

/* Card principal con scroll */
.horario-card-root {
  flex: 1;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  gap: 24px;
  padding: 40px 0;
  width: 100%;
  min-width: 0;
}

.horario-card {
  background: #fff;
  border-radius: 18px;
  padding: 2.5rem 2.5rem 2rem 2.5rem;
  min-width: 0;
  width: 98%;
  max-width: 1200px;
  margin: 0 auto;
  box-shadow: 0 2px 18px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  height: auto;
}

.horario-card h2 {
  margin-bottom: 1.5rem;
  font-size: 2.3rem;
  font-weight: 500;
  color: #009999;
  text-align: center;
  width: 100%;
}

.horario-scroll {
  width: 100%;
  max-height: 70vh;
  overflow-x: auto;
  overflow-y: auto;
  margin-bottom: 1.5rem;
}

.horario-table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  min-width: 900px;
}
.horario-table th,
.horario-table td {
  border: 1px solid #e0e0e0;
  text-align: center;
  min-width: 110px;
  padding: 0.3rem 0.2rem;
  font-size: 1rem;
  vertical-align: middle;
}
.hora-label {
  font-weight: 600;
  color: #009999;
  background: #f5f5f5;
  min-width: 70px;
}
.reserva-block {
  background: #75C2A6;
  color: #222;
  border-radius: 8px;
  font-weight: 500;
  font-size: 1rem;
  padding: 0.2rem 0.4rem;
}
.reserva-nombre {
  font-weight: 700;
}
.reserva-proc {
  font-weight: 400;
  font-size: 0.95em;
  margin-left: 0.3em;
}
.leyenda {
  display: flex;
  align-items: center;
  margin-top: 1.2rem;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}
.leyenda-block {
  width: 80px;
  height: 28px;
  border-radius: 8px;
  margin-right: 12px;
  background: #75C2A6;
}
.cargando {
  font-size: 1.2rem;
  color: #009999;
  text-align: center;
  margin-top: 2rem;
}
.btn-reservar {
  background: #009999;
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 0.7em 2em;
  font-size: 1.2em;
  margin-bottom: 1.2em;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s;
}
.btn-reservar:hover {
  background: #007777;
}
.btn-ok {
  background: #75C2A6;
  color: #222;
  border: none;
  border-radius: 8px;
  padding: 0.7em 2em;
  font-size: 1.2em;
  margin-top: 1.2em;
  cursor: pointer;
  font-weight: 600;
  transition: background 0.2s;
}
.btn-ok:hover {
  background: #009999;
  color: #fff;
}
.seleccionada {
  outline: 3px solid #009999;
  background: #e0f7f4 !important;
}
</style>