import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import store from '@/store'

import homeRoutes from '@/modules/home/routes'
import authRoutes from '@/modules/auth/routes'
import userRoutes from '@/modules/user/routes'

const routes: RouteRecordRaw[] = [
  ...authRoutes,
  ...homeRoutes,
  ...userRoutes
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, _, next) => {
  const authenticated = store.getters.getIsAuthenticated
  const requiredLogin = to.matched.some(record => record.meta.requiresAuth)
  const alreadyLogged = to.matched.some(record => record.meta.authenticated)

  // redirect user to login page if user is not authenticated
  if (!authenticated && requiredLogin) next({ name: 'login' })
  else if (authenticated && alreadyLogged) next({ name: 'home' })
  else next()
})

export default router
