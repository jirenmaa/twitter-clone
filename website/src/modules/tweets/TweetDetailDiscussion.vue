<script lang="ts">
import { defineComponent, onBeforeMount, reactive, ref } from 'vue'
import { redirect } from '@/utils/helper'
import { TweetReplies } from './types'
import { fetchTweetDiscussion } from '@/modules/tweets/services/tweets'

import LoadingSpinner from '@/components/shared/LoadingSpinner.vue'
import Responses from '@/components/Responses.vue'

export default defineComponent({
  name: 'TweetDetailDiscussion',
  components: {
    LoadingSpinner,
    Responses
  },
  props: {
    tweetId: {
      type: String
    }
  },
  setup (props) {
    const state = reactive({
      replies: ref<Array<TweetReplies>>([]),
      loading: true
    })

    onBeforeMount(async () => {
      state.replies = await fetchTweetDiscussion(`/tweets/replies/${props.tweetId}`)
      state.loading = false
    })

    return { state, redirect }
  }
})
</script>

<template>
  <LoadingSpinner v-if="state.loading" class="grid place-items-center my-12" />
  <div v-else class="divide-y divide-dark-grey">
    <div v-for="(discussion, index) in state.replies" :key="index" class="p-4">
      <div class="grid grid-cols-12">
        <div class="col-span-1 mx-auto">
          <div
            class="w-10 h-10 bg-dark border border-dark-grey rounded-full cursor-pointer"
            @click="
              redirect($event, 'user-tweet', {
                username: discussion?.author.username
              })
            "
          ></div>
        </div>
        <div class="col-span-11 ml-2">
          <div
            class="inline-flex items-center cursor-pointer on-hover space-x-2"
            @click="
              redirect($event, 'user-tweet', {
                username: discussion?.author.username
              })
            "
          >
            <div class="font-medium text-base hovered">
              {{ discussion?.author.name || discussion?.author.username }}
            </div>
            <span class="text-peach text-sm"
              >@{{ discussion?.author.username }}</span
            >
          </div>
          <div
            v-html="discussion?.content"
            class="break-words text-ms mt-2"
          ></div>
          <div
            v-if="discussion?.pictures"
            class="overflow-hidden max-h-72 rounded-md border border-dark-grey"
          >
            <img
              alt="test tweet picture"
              class="w-full rounded-md"
              :src="discussion?.pictures"
            />
          </div>
          <Responses
            :tweetId="discussion?.id"
            class="text-peach text-ms mt-4"
          />
        </div>
      </div>
    </div>
  </div>
</template>
