<script lang="ts">
import { defineComponent } from 'vue'

import TweetCards from '../modules/tweets/TweetCards.vue'
import RightSidebar from '../components/shared/RightSidebar.vue'
import UserInfo from '../modules/user/UserInfo.vue'

export default defineComponent({
  name: 'UserProfile',
  components: {
    TweetCards,
    RightSidebar,
    UserInfo
  }
})
</script>

<template>
  <div class="grid grid-cols-5 col-span-4">
    <div class="col-span-3 flex flex-col ml-12 mb-12">
      <UserInfo />
      <TweetCards class="mt-12" />
    </div>
    <div class="col-span-2 mx-8 ml-16">
      <RightSidebar />
    </div>
  </div>
</template>
