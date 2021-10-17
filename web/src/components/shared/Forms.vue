<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Forms'
})
</script>

<template>
  <div class="flex flex-col mt-8">
    <div class="flex items-center space-x-4">
      <div class="w-10 h-10 bg-dark border border-dark-grey rounded-full"></div>
      <div class="text-lg font-medium">Matt Dreamson</div>
    </div>
    <div class="form-wrap overflow-y-auto max-h-56 ml-10 pl-4">
      <div contenteditable="true" class="forms text-gray-500">What's on your mind?</div>
    </div>
  </div>
</template>

<style lang="scss">
.form-wrap {
  scroll-behavior: smooth;
  scrollbar-width: thin;
  scrollbar-color: #ddd #222;
}
.form-wrap::-webkit-scrollbar {
  width: 3px !important;
  background: #222;
}
.form-wrap::-webkit-scrollbar-thumb {
  background-color: #ddd;
  border: 3px solid #ddd;
}
.forms {
  word-wrap: break-word;
}
</style>
