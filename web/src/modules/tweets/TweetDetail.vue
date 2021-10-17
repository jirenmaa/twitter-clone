<script lang="ts">
import { defineComponent } from 'vue'

import TweetCardDetail from './TweetCardDetail.vue'
import RightSidebar from '../../components/shared/RightSidebar.vue'

export default defineComponent({
  name: 'TweetDetail',
  components: {
    TweetCardDetail,
    RightSidebar
  }
})
</script>

<template>
  <div class="grid grid-cols-5 col-span-4">
    <div class="col-span-3 mb-12 ml-12">
      <TweetCardDetail />
    </div>
    <div class="col-span-2 mx-8 ml-16">
      <RightSidebar />
    </div>
  </div>
</template>
