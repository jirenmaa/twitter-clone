<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'App'
})
</script>

<template>
  <router-view></router-view>
</template>

<style lang="scss">
* {
  font-weight: 300;
  font-family: "Poppins", sans-serif;
  box-sizing: border-box;
  outline: none !important;
}

html {
  scroll-behavior: smooth;
  scrollbar-width: thin;
  scrollbar-color: #ddd #222;
}

html::-webkit-scrollbar {
  width: 5px !important;
  background: #222;
}

html::-webkit-scrollbar-thumb {
  background-color: #ddd;
  border: 3px solid #ddd;
}

body {
  color: #ccc;
  background: #131313;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.on-hover {
  &:hover {
    .hovered {
      text-decoration: underline;
    }
  }
}
</style>
