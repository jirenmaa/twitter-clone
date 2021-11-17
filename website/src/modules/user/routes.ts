import { RouteRecordRaw } from 'vue-router'

import UserProfile from '@/modules/user/index.vue'
import UserTweets from '@/modules/user/UserTweets.vue'
import UserReplies from '@/modules/user/UserReplies.vue'
import UserMedias from '@/modules/user/UserMedias.vue'
import UserLikes from '@/modules/user/UserLikes.vue'

const userRoutes: RouteRecordRaw[] = [
  {
    path: '/:username',
    name: 'user-profile',
    component: UserProfile,
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        name: 'user-tweet',
        component: UserTweets,
        meta: { requiresAuth: true }
      },
      {
        path: '/:username/replies',
        name: 'user-reply',
        component: UserReplies,
        meta: { requiresAuth: true }
      },
      {
        path: '/:username/medias',
        name: 'user-media',
        component: UserMedias,
        meta: { requiresAuth: true }
      },
      {
        path: '/:username/likes',
        name: 'user-like',
        component: UserLikes,
        meta: { requiresAuth: true }
      }
    ]
  }
]

export default userRoutes
