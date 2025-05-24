import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import DatosMedicos from './components/DatosMedicos.vue';
import CrearDatoMedico from './components/CrearDatoMedico.vue';
import DetalleDatoMedico from './components/DetalleDatoMedico.vue';
import EditarDatoMedico from './components/EditarDatoMedico.vue';
import EliminarDatoMedico from './components/EliminarDatoMedico.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/datos-medicos', component: DatosMedicos },
  { path: '/datos-medicos/crear', component: CrearDatoMedico },
  { path: '/datos-medicos/:id', component: DetalleDatoMedico, props: true },
  { path: '/datos-medicos/:id/editar', component: EditarDatoMedico, props: true },
  { path: '/datos-medicos/:id/eliminar', component: EliminarDatoMedico, props: true }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;