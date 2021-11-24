<script lang="ts">
import { defineComponent, ref, reactive } from 'vue'
import { redirect } from '@/utils/helper'

import { Tweet } from '@/modules/tweets/types'

import Responses from '@/components/Responses.vue'
import IconMore from '@/icons/IconMore.vue'

export default defineComponent({
  name: 'TweetCards',
  components: {
    IconMore,
    Responses
  },
  props: {
    tweet: Object as () => Tweet
  },
  setup (props) {
    const authorUsername = ref<string>(props.tweet?.author.username || '')
    const isResponded: boolean = (
      props.tweet?.responses !== undefined &&
      props.tweet?.responses.commented
    )
    const state = reactive({
      parameter: {
        id: props.tweet?.id,
        username: authorUsername?.value
      }
    })

    return { state, redirect, authorUsername, isResponded }
  }
})
</script>

<template>
  <div
    class="grid grid-cols-12 cursor-pointer border-b border-dark-grey hover:bg-dark"
    @click="redirect($event, 'tweet-detail', state.parameter)"
  >
    <div class="col-span-1 relative overflow-hidden mx-auto py-4 pl-4">
      <div class="w-12 h-12 bg-dark border border-dark-grey rounded-full"></div>
      <div
        v-if="isResponded"
        class="w-0.25 h-full bg-dark-grey mx-auto my-4"
      ></div>
    </div>
    <div class="col-span-11 space-y-2 ml-4 p-4">
      <div class="flex justify-between items-center">
        <div
          data-event="user-profile"
          class="inline-flex items-center cursor-pointer space-x-1 on-hover z-10"
          @click="redirect($event, 'user-tweet', { username: tweet?.author.username })"
        >
          <span class="font-medium text-base hovered">
            {{ tweet?.author.name || authorUsername }}
          </span>
          <span class="text-peach text-sm">@{{ authorUsername }}</span>
        </div>
        <div class="inline-flex cursor-pointer hover-more">
          <IconMore
            class="rounded-full transform scale-125 transition ease-in-out duration-200 p-1"
          />
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

<style lang="scss">
.hover-more:hover {
  svg {
    background: rgba(52, 211, 153, 0.1);
    stroke: #34d399;
  }
}
</style>
