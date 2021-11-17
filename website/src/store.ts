import { createStore } from 'vuex'

import stateAuth from '@/modules/auth/store'

import StoreTweetReply from '@/modules/tweets/store'
import authentication from '@/modules/auth/store/store'

export default createStore({
  modules: {
    auth: authentication,
    tweet: StoreTweetReply
  },
  plugins: [stateAuth]
})
