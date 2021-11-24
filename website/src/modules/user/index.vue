<script lang="ts">
import { defineComponent, watch } from 'vue'
import { StateUser } from '@/modules/auth/types'
import store from '@/store'

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
  <div class="grid grid-cols-10 h-screen mx-12">
    <div class="col-span-2 text-justify">
      <LeftSidebar :userInfo="user"></LeftSidebar>
    </div>
    <div class="col-span-8 grid grid-cols-12 text-justify">
      <div class="col-span-8 border-dark-grey border-l border-r mx-8">
        <UserInfo :userInfo="user" />
        <router-view :key="$route.fullPath"></router-view>
      </div>
      <div class="col-span-4 text-justify">
        <RightSidebar></RightSidebar>
      </div>
    </div>
  </div>
</template>
