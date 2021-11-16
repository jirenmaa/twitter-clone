<script lang="ts">
import { defineComponent, reactive } from 'vue'

import { redirect } from '@/utils/helper'
import { logout } from '@/modules/auth/services/logout'

import { StateUser } from '@/modules/auth/types'

export default defineComponent({
  name: 'LeftSidebar',
  props: {
    userInfo: {
      required: true,
      type: Object as () => StateUser
    }
  },
  setup () {
    const state = reactive({
      navigations: [
        ['home', '/'],
        ['explore', '/explore'],
        ['messages', '/messages'],
        ['bookmarks', '/bookmarks'],
        ['profile', '/profile'],
        ['more', '/more']
      ]
    })
    return { state, redirect, logout }
  }
})
</script>

<template>
  <div v-if="userInfo" class="pt-8">
    <div class="sticky top-8">
      <div class="flex flex-col space-y-2 mx-8">
        <div
          class="w-24 h-24 bg-dark border border-dark-grey rounded-full cursor-pointer mx-auto"
          @click="redirect($event, 'user-tweet', { username: userInfo.username })"
        ></div>
        <div class="items-center text-center space-y-2">
          <div
            class="font-medium text-2xl cursor-pointer"
            @click="redirect($event, 'user-tweet', { username: userInfo.username })"
          >
            {{ userInfo.username }}
          </div>
          <div class="lowercase text-peach text-mm">
            A Fool and His Money Are Soon Parted wadasdaw da sdaw da sad awd
          </div>
        </div>
      </div>
      <div class="text-base pt-12 mx-8">
        <span class="uppercase font-medium">menus</span>
        <div
          v-for="(navigation, index) in state.navigations"
          :key="index"
          class="mt-3"
        >
          <router-link
            :to="navigation[1]"
            class="capitalize text-peach hover:text-current hover:underline"
            >{{ navigation[0] }}</router-link
          >
        </div>
      </div>
      <div class="text-base space-y-3 pt-6 mx-8">
        <span class="uppercase font-medium">actions</span>
        <div
          @click="logout"
          class="capitalize text-peach cursor-pointer hover:text-current hover:underline hover:text-red-500"
          >logout</div
        >
      </div>
    </div>
  </div>
</template>
