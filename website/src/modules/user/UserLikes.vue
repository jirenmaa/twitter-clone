<script lang="ts">
import { defineComponent, ref, reactive, onBeforeMount } from 'vue'
import router from '@/routes'

import { Tweet } from '@/modules/tweets/types'
import { fetchPublicTweets } from '@/modules/tweets/services/tweets'

import TweetCards from '@/modules/tweets/TweetCards.vue'
import LoadingSpinner from '@/components/shared/LoadingSpinner.vue'

export default defineComponent({
  name: 'UserLikes',
  components: {
    TweetCards,
    LoadingSpinner
  },
  setup () {
    const state = reactive({
      likes: ref<Array<Tweet>>([]),
      loading: true
    })

    onBeforeMount(async () => {
      const username: string = router.currentRoute.value?.params
        ?.username as string
      state.likes = await fetchPublicTweets(`/${username}/likes`)
      state.loading = false
    })

    return { state }
  }
})
</script>

<template>
  <LoadingSpinner v-if="state.loading" class="grid place-items-center mt-12" />
  <div class="space-y-4 mt-12">
    <TweetCards
      v-for="(tweet, index) in state.likes"
      v-bind:key="index" :tweet="tweet" />
  </div>
</template>
