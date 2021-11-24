<script lang="ts">
import { defineComponent } from 'vue'

import store from '@/store'
import { StateUser } from '@/modules/auth/types'

import LeftSidebar from '@/components/shared/LeftSidebar.vue'
import RightSidebar from '@/components/shared/RightSidebar.vue'

export default defineComponent({
  name: 'Home',
  components: {
    LeftSidebar,
    RightSidebar
  },
  setup () {
    const user: StateUser = store.getters.getUser
    return { user }
  }
})
</script>

<template>
  <div class="grid grid-cols-10 h-screen mx-12">
    <div class="col-span-2">
      <LeftSidebar :userInfo="user"></LeftSidebar>
    </div>
    <div class="col-span-8 grid grid-cols-12">
      <div class="col-span-8 border-dark-grey border-l border-r mx-8">
        <router-view></router-view>
      </div>
      <div class="col-span-4">
        <RightSidebar></RightSidebar>
      </div>
    </div>
  </div>
</template>
