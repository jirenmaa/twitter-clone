<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ArrowLeft'
})
</script>

<template>
  <svg
    width="24"
    height="24"
    viewBox="0 0 24 24"
    stroke-width="2"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M19 12H5"
      stroke="#ccc"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <path
      d="M12 19L5 12L12 5"
      stroke="#ccc"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
</template>
