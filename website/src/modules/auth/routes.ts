import { RouteRecordRaw } from 'vue-router'

import Login from './login.vue'
import Register from './register.vue'
import Activation from './activation.vue'

const authRoutes: RouteRecordRaw[] = [
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: { authenticated: true }
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta: { authenticated: true }
  },
  {
    path: '/activation',
    name: 'activation',
    component: Activation
  }
]

export default authRoutes
