<script lang="ts">
import { defineComponent } from 'vue'

import { StateUser } from '@/modules/auth/types'
import { redirect } from '@/utils/helper'
import { logout } from '@/modules/auth/services/logout'

import IconHome from '@/icons/IconHome.vue'
import IconExplore from '@/icons/IconExplore.vue'
import IconBookmark from '@/icons/IconBookmark.vue'
import IconEmail from '@/icons/IconEmail.vue'
import IconMore from '@/icons/IconMore.vue'
import IconUser from '@/icons/IconUser.vue'

export default defineComponent({
  name: 'LeftSidebar',
  components: {
    IconHome,
    IconExplore,
    IconBookmark,
    IconEmail,
    IconUser,
    IconMore
  },
  props: {
    userInfo: {
      required: true,
      type: Object as () => StateUser
    }
  },
  setup () {
    const navigations = [
      ['home', '/', 'IconHome'],
      ['explore', '/explore', 'IconExplore'],
      ['bookmarks', '/bookmarks', 'IconBookmark'],
      ['profile', '/profile', 'IconUser'],
      ['messages', '/messages', 'IconEmail'],
      ['more', '/more', 'IconMore']
    ]

    return { navigations, redirect, logout }
  }
})
</script>

<template>
  <div class="sticky top-0">
    <div class="flex flex-col justify-between h-screen py-8">
      <div class="flex flex-col space-y-4">
        <div v-for="(value, index) in navigations" :key="index" class="flex">
          <router-link :to="value[1]" class="w-full flex items-center capitalize text-lg text-peach cursor-pointer rounded hover:text-current hover:bg-dark-grey hover:bg-opacity-30 space-x-2 py-2.5 pl-4">
            <component
              :is="value[2]"
              class="transform scale-75"></component>
            <span>{{ value[0] }}</span>
          </router-link>
        </div>
        <div class="flex">
          <div @click="logout" class="w-full capitalize text-base text-peach cursor-pointer rounded hover:text-red-500 hover:bg-red-400 hover:bg-opacity-20 py-2.5 pl-4">logout</div>
        </div>
      </div>
      <div class="flex flex-col">
        <div @click="redirect($event, 'user-tweet', { username: userInfo.username })" class="w-full flex items-center capitalize text-peach cursor-pointer rounded hover:bg-dark-grey hover:bg-opacity-30 space-x-3 py-2.5 pl-4">
          <div class="w-10 h-10 bg-dark border border-dark-grey rounded-full cursor-pointer"></div>
          <div class="flex flex-col text-ms">
            <span class="text-current">{{ userInfo.name || userInfo.username }}</span>
            <span class="text-mm">@{{ userInfo.username }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
