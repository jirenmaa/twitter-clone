<script lang="ts">
import { defineComponent, ref, watch, reactive } from 'vue'

import store from '@/store'
import { Tweet } from '@/modules/tweets/types'
import { redirect } from '@/utils/helper'

import ReplyForm from '@/components/ReplyForm.vue'
import Responses from '@/components/Responses.vue'

export default defineComponent({
  name: 'TweetCards',
  components: {
    ReplyForm,
    Responses
  },
  props: {
    tweet: Object as () => Tweet
  },
  setup (props) {
    const authorUsername = ref<string>(props.tweet?.author.username || '')
    const parameter = {
      id: props.tweet?.id,
      username: authorUsername?.value
    }
    const state = reactive({
      replying: false
    })

    watch(store.getters.getReplying, _ => {
      state.replying = store.getters.getReplying.replying
    })

    const isResponded = (
      props.tweet?.responses !== undefined &&
      props.tweet?.responses.commented
    )

    return { state, redirect, authorUsername, parameter, isResponded }
  }
})
</script>

<template>
  <div
    v-if="state.replying"
    class="fixed top-0 left-0 w-full h-screen grid place-items-center bg-dark bg-opacity-90 z-50"
  >
    <ReplyForm class="border bg-dark" />
  </div>
  <div
    class="grid grid-cols-12 cursor-pointer border border-dark-grey rounded hover:bg-dark"
    @click="redirect($event, 'tweet-detail', parameter)"
  >
    <div class="col-span-1 relative overflow-hidden mx-auto py-4 pl-4">
      <div class="w-12 h-12 bg-dark border border-dark-grey rounded-full"></div>
      <div
        v-if="isResponded"
        class="w-0.25 h-full bg-dark-grey mx-auto my-4"
      ></div>
    </div>
    <div class="col-span-11 space-y-2 ml-4 p-4">
      <div class="flex items-center">
        <div
          data-event="user-profile"
          class="inline-flex items-center cursor-pointer space-x-1 on-hover"
          @click="redirect($event, 'user-tweet', { username: authorUsername })"
        >
          <span class="font-medium text-lg hovered">
            {{ tweet?.author.name || authorUsername }}
          </span>
          <span class="text-peach text-sm">@{{ authorUsername }}</span>
        </div>
      </div>
      <div v-html="tweet?.content" class="break-words text-ms pb-2"></div>
      <div
        v-if="tweet?.pictures"
        class="overflow-hidden border border-dark-grey rounded max-h-80"
      >
        <img class="w-full rounded-md" :src="tweet?.pictures" />
      </div>
      <Responses
        :responses="tweet?.responses"
        :tweetId="tweet?.id || ''"
        :authors="tweet?.author"
        :picture="tweet?.pictures"
        :content="tweet?.content"

        :class="{'pt-2': tweet?.pictures}"
        class="text-peach text-ms mt-4"
      />
    </div>
    <div
      v-if="isResponded"
      class="col-span-12 grid grid-cols-12 border-t border-dark-grey cursor-pointer items-center rounded-b bg-dark hover:bg-opacity-50 transition ease-in-out duration-200 mt-4"
    >
      <div class="col-span-1 relative overflow-hidden mx-auto p-4">
        <div
          class="w-9 h-9 bg-dark border border-dark-grey rounded-full mx-auto ml-1.5"
        ></div>
      </div>
      <div
        class="col-span-11 inline-flex text-peach hover:underline text-ms ml-4 p-4"
      >
        <span>Show this thread</span>
      </div>
    </div>
  </div>
</template>
