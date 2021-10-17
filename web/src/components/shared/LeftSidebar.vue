<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'LeftSidebar',
  data (): { navigations: string[][] } {
    return {
      navigations: [
        ['home', '/'],
        ['explore', '/explore'],
        ['messages', '/messages'],
        ['bookmarks', '/bookmarks'],
        ['profile', '/profile'],
        ['more', '/more']
      ]
    }
  }
})
</script>

<template>
  <div class="flex flex-col space-y-2 text-3xl pt-8">
    <div class="flex flex-col space-y-2 sticky top-8 mx-8">
      <div class="w-24 h-24 bg-dark border border-dark-grey rounded-full mx-auto"></div>
      <div class="items-center text-center">
        <div class="font-medium text-2xl">Matt Dreamson</div>
        <div
          class="lowercase text-peach text-mm"
        >A Fool and His Money Are Soon Parted wadasdaw da sdaw da sad awd</div>
      </div>
      <div class="text-base pt-12">
        <span class="uppercase font-medium">menus</span>
        <div v-for="(navigation, index) in navigations" :key="index" class="mt-3">
          <router-link
            :to="navigation[1]"
            class="capitalize text-peach hover:text-current hover:underline"
          >{{ navigation[0] }}</router-link>
        </div>
      </div>
      <div class="text-base pt-6">
        <span class="uppercase font-medium">actions</span>
        <div class="mt-3">
          <router-link
            to="/"
            class="capitalize text-peach hover:text-current hover:underline hover:text-red-500"
          >logout</router-link>
        </div>
      </div>
    </div>
  </div>
</template>
