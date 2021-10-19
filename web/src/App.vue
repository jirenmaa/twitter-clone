<script lang="ts">
import { defineComponent } from 'vue'
import LeftSidebar from './components/shared/LeftSidebar.vue'

export default defineComponent({
  name: 'App',
  components: {
    LeftSidebar
  }
})
</script>

<template>
  <div class="grid grid-cols-5 h-screen">
    <LeftSidebar class="col-span-1 border-r border-dark-grey h-full" />
    <router-view></router-view>
  </div>
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
