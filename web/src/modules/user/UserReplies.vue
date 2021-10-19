<script lang="ts">
import { defineComponent } from 'vue'
import Responses from '../../components/shared/Responses.vue'

export default defineComponent({
  name: 'UserReplies',
  components: {
    Responses
  },
  setup () {
    // eslint-disable-next-line
    function stopEvent(event: any) {
      // stop any default behavior of the event
      event.cancelBubble = true
      if (event.stopPropagation) {
        event.stopPropagation()
        event.preventDefault()
      }
    }

    // eslint-disable-next-line
    function redirect(this: any, event: any, url: string, parameters: any) {
      // redirect to the url with the given parameters
      const target = event.currentTarget.attributes['data-event']
      const routed = { name: url, params: parameters }

      if (target) {
        this.$router.push(routed)
        stopEvent(event)
      } else {
        this.$router.push(routed)
      }
    }

    return {
      redirect
    }
  }
})
</script>

<template>
user replies
</template>
