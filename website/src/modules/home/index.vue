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
  <div class="grid grid-cols-5 h-screen">
    <LeftSidebar
      class="col-span-1 border-r border-dark-grey h-full"
      :userInfo="user"
    />
    <div class="col-span-4 grid grid-cols-5">
      <div class="col-span-3 space-y-12 mb-12 ml-12">
        <router-view></router-view>
      </div>
      <div class="col-span-2 mx-8 ml-16">
        <RightSidebar />
      </div>
    </div>
  </div>
</template>
