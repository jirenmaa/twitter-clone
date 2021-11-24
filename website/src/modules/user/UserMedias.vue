<script lang="ts">
import { defineComponent, ref, watch, reactive, onBeforeMount } from 'vue'
import router from '@/routes'
import store from '@/store'

import { Tweet } from '@/modules/tweets/types'
import { fetchPublicTweets } from '@/modules/tweets/services/tweets'

import ReplyForm from '@/components/ReplyForm.vue'
import TweetCards from '@/modules/tweets/TweetCards.vue'
import LoadingSpinner from '@/components/shared/LoadingSpinner.vue'

export default defineComponent({
  name: 'UserMedias',
  components: {
    ReplyForm,
    TweetCards,
    LoadingSpinner
  },
  setup () {
    const state = reactive({
      medias: ref<Array<Tweet>>([]),
      loading: true,
      replying: false
    })

    onBeforeMount(async () => {
      const username: string = router.currentRoute.value?.params
        ?.username as string
      state.medias = await fetchPublicTweets(`/${username}/medias`)
      state.loading = false
    })

    watch(store.getters.getReplying, _ => {
      state.replying = store.getters.getReplying.replying
    })

    return { state }
  }
})
</script>

<template>
  <div v-show="state.replying" class="fixed top-0 left-0 w-full h-screen grid place-items-center bg-dark bg-opacity-70 z-50">
    <ReplyForm class="border bg-dark" />
  </div>
  <LoadingSpinner v-if="state.loading" class="grid place-items-center mt-12" />
  <div class="mb-4">
    <TweetCards
      v-for="(tweet, index) in state.medias"
      v-bind:key="index" :tweet="tweet" />
  </div>
</template>
