<script lang="ts">
import { defineComponent, onBeforeMount, reactive, ref } from 'vue'
import axiosInstance from '@/services/axios'
import { redirect } from '@/utils/helper'

import { TweetReplies } from './types'

import Responses from '@/components/Responses.vue'
import LoadingSpinner from '@/components/shared/LoadingSpinner.vue'

export default defineComponent({
  name: 'TweetDetailDiscussion',
  components: {
    Responses,
    LoadingSpinner
  },
  props: {
    tweetId: {
      type: String
    }
  },
  setup (props) {
    const state = reactive({
      replies: ref<Array<TweetReplies>>([]),
      loading: false
    })

    onBeforeMount(async () => {
      state.loading = true
      await axiosInstance.get(`/tweets/replies/${props.tweetId}`).then(res => {
        state.replies = res.data
      })
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
            class="overflow-hidden rounded-md max-h-72"
            v-if="discussion?.pictures"
          >
            <img
              alt="test tweet picture"
              class="w-full rounded-md mt-2"
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
