<script lang="ts">
import { defineComponent } from 'vue'

import Forms from '../components/shared/Forms.vue'
import TweetCards from '../modules/tweets/TweetCards.vue'
import RightSidebar from '../components/shared/RightSidebar.vue'

export default defineComponent({
  name: 'Home',
  components: {
    Forms,
    TweetCards,
    RightSidebar
  }
})
</script>

<template>
  <div class="grid grid-cols-5 col-span-4">
    <div class="col-span-3 space-y-12 mb-12 ml-12">
      <Forms />
      <TweetCards />
    </div>
    <div class="col-span-2 mx-8 ml-16">
      <RightSidebar />
    </div>
  </div>
</template>
