<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'UserInfo'
})
</script>

<template>
  <div class="flex flex-col items-center space-y-4 mt-8">
    <div
      class="w-40 h-40 bg-dark border border-dark-grey rounded-full cursor-pointer"
    ></div>
    <div class="flex flex-col text-center">
      <h1 class="font-medium text-3xl">
        Matt Dreamson
      </h1>
      <div class="w-3/4 text-peach mx-auto">
        A Fool and His Money Are Soon Parted wadasdaw da sdaw da sad awd
      </div>
    </div>
  </div>
  <div class="grid grid-cols-4 text-center text-peach border border-dark-grey rounded cursor-pointer mt-4">
    <div class="hover:bg-dark text-current border-b-2 border-peach py-4">Tweets</div>
    <div class="hover:bg-dark py-4">Replies</div>
    <div class="hover:bg-dark py-4">Media</div>
    <div class="hover:bg-dark py-4">Likes</div>
  </div>
</template>
