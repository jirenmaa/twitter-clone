<script lang="ts">
import { defineComponent, ref, watch, reactive, onBeforeMount } from 'vue'
import store from '@/store'

import { fetchPublicTweets } from '@/modules/tweets/services/tweets'
import { Tweet } from '@/modules/tweets/types'

import ReplyForm from '@/components/ReplyForm.vue'
import TweetForms from '@/components/TweetForms.vue'
import TweetCards from '@/modules/tweets/TweetCards.vue'

import LoadingSpinner from '@/components/shared/LoadingSpinner.vue'

export default defineComponent({
  name: 'PublicTweets',
  components: {
    ReplyForm,
    TweetForms,
    TweetCards,
    LoadingSpinner
  },
  setup () {
    const state = reactive({
      tweets: ref<Array<Tweet>>([]),
      loading: true,
      replying: false
    })

    onBeforeMount(async () => {
      fetchTweets()
    })

    watch(store.getters.getReplying, _ => {
      state.replying = store.getters.getReplying.replying
    })

    async function fetchTweets () {
      state.loading = true
      state.tweets = await fetchPublicTweets('/tweets/')
      state.loading = false
    }

    return { state, fetchTweets }
  }
})
</script>

<template>
  <div
    v-show="state.replying"
    class="fixed top-0 left-0 w-full h-screen grid place-items-center bg-dark bg-opacity-70 z-50"
  >
    <ReplyForm class="border bg-dark" />
  </div>
  <TweetForms @tweetSent="fetchTweets" />
  <LoadingSpinner v-if="state.loading" class="grid place-items-center" />
  <div v-else class="flex flex-col space-y-4">
    <TweetCards
      v-for="(tweet, index) in state.tweets"
      v-bind:key="index" :tweet="tweet" />
  </div>
</template>
