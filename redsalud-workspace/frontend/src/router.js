import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import DatosMedicos from './components/DatosMedicos.vue'
import OlvideContraseña from './components/OlvideContraseña.vue'
import Coordinador from './components/Coordinador.vue'
import VistaBoxes from './components/VistaBoxes.vue'
import AgregarBoxes from './components/AgregarBoxes.vue'
// Importing components for routing


const routes = [
  { path: '/', component: Home },
  { path: '/datos-medicos', component: DatosMedicos },
  { path: '/olvide-contraseña', component: OlvideContraseña },
  { path: '/coordinador', component: Coordinador },
  { path: '/boxes', component: VistaBoxes },
  { path: '/agregar-boxes', component: AgregarBoxes }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router