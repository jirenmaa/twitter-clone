<script lang="ts">
import { defineComponent } from 'vue'
import store from '@/store'
import { StateUser } from '@/modules/auth/types'

import UserInfo from '@/modules/user/UserInfo.vue'
import RightSidebar from '@/components/shared/RightSidebar.vue'
import LeftSidebar from '@/components/shared/LeftSidebar.vue'

export default defineComponent({
  name: 'UserProfile',
  components: {
    UserInfo,
    RightSidebar,
    LeftSidebar
  },
  setup () {
    const user: StateUser = store.getters.getUser
    return { user }
  }
})
</script>

<template>
  <div class="grid grid-cols-5 h-screen">
    <LeftSidebar class="col-span-1 border-r border-dark-grey h-full" :userInfo="user" />
    <div class="grid grid-cols-5 col-span-4">
      <div class="col-span-3 flex flex-col ml-12 mb-12">
        <UserInfo :userInfo="user" />
        <router-view></router-view>
      </div>
      <div class="col-span-2 mx-8 ml-16">
        <RightSidebar />
      </div>
    </div>
  </div>
</template>
