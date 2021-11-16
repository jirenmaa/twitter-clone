<script lang="ts">
import { defineComponent, ref, reactive, onBeforeMount } from 'vue'
import axiosInstance from '@/services/axios'

import { Tweet } from '@/modules/tweets/types'
import { fetchPublicTweets } from '@/modules/tweets/services/tweets'

import TweetForms from '@/components/TweetForms.vue'
import TweetCards from './TweetCards.vue'

import LoadingSpinner from '@/components/shared/LoadingSpinner.vue'

export default defineComponent({
  name: 'PublicTweets',
  components: {
    TweetForms,
    TweetCards,
    LoadingSpinner
  },
  setup () {
    const state = reactive({
      tweets: ref<Array<Tweet>>([]),
      loading: true
    })

    async function fetchTweets () {
      state.loading = true
      state.tweets = await fetchPublicTweets('/tweets/')
      state.loading = false
    }

    onBeforeMount(async () => {
      fetchTweets()
    })

    return { state, fetchTweets }
  }
})
</script>

<template>
  <TweetForms @tweetSent="fetchTweets" />
  <LoadingSpinner v-if="state.loading" class="grid place-items-center" />
  <div v-else class="flex flex-col space-y-4">
    <TweetCards
      v-for="(tweet, index) in state.tweets"
      v-bind:key="index"
      :tweet="tweet"
    />
  </div>
</template>
