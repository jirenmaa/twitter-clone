<script lang="ts">
import { defineComponent, ref, reactive, onBeforeMount } from 'vue'

import { Tweet } from '@/modules/tweets/types'
import { fetchPublicTweets } from '@/modules/tweets/services/tweets'

import TweetCards from '@/modules/tweets/TweetCards.vue'
import LoadingSpinner from '@/components/shared/LoadingSpinner.vue'

export default defineComponent({
  name: 'UserReplies',
  components: {
    TweetCards,
    LoadingSpinner
  },
  setup () {
    const state = reactive({
      userReplies: ref<Array<Tweet>>([]),
      loding: true
    })

    onBeforeMount(async () => {
      state.userReplies = await fetchPublicTweets('/user/comments')
      state.loding = false
    })

    return { state }
  }
})
</script>

<template>
  <LoadingSpinner v-if="state.loding" class="grid place-items-center mt-12" />
  <div class="space-y-4 mt-12">
    <TweetCards
      v-for="(tweet, index) in state.userReplies"
      v-bind:key="index"
      :tweet="tweet"
    />
  </div>
</template>
