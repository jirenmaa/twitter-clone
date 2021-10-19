import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

import Home from '../views/Home.vue'
import UserProfile from '../views/UserProfile.vue'
import TweetDetail from '../modules/tweets/TweetDetail.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: { requiresAuth: true }
  },
  {
    path: '/:username/status/:id',
    name: 'tweet-detail',
    component: TweetDetail,
    meta: { requiresAuth: true }
  },
  {
    path: '/:username',
    name: 'user-profile',
    component: UserProfile,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
