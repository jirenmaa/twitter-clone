<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ButtonSubmit',
  props: {
    padding: {
      type: String
    },
    context: {
      type: String
    }
  }
})
</script>

<template>
  <button
    type="submit"
    class="capitalize cursor-pointer rounded bg-dark-grey"
    :class="padding"
  >
    {{ context }}
  </button>
</template>
