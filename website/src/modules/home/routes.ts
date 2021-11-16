import { RouteRecordRaw } from 'vue-router'

import Home from './index.vue'

import PublicTweets from '@/modules/tweets/TweetPublic.vue'
import TweetDetail from '@/modules/tweets/TweetDetail.vue'

const homeRoutes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        name: 'tweet-public',
        component: PublicTweets,
        meta: { requiresAuth: true }
      },
      {
        path: '/:username/status/:id',
        name: 'tweet-detail',
        component: TweetDetail,
        meta: { requiresAuth: true }
      }
    ]
  }
]

export default homeRoutes
