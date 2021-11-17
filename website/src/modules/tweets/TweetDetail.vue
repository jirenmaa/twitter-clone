<script lang="ts">
import { defineComponent, ref, watch, reactive, onBeforeMount } from 'vue'
import moment from 'moment'

import { redirect } from '@/utils/helper'
import router from '@/routes'
import store from '@/store'

import { fetchPublicDetailTweet } from '@/modules/tweets/services/tweets'
import { Tweet } from './types'

import ReplyForm from '@/components/ReplyForm.vue'
import Responses from '@/components/Responses.vue'
import TweetDetailDiscussion from '@/modules/tweets/TweetDetailDiscussion.vue'

import LoadingSpinner from '@/components/shared/LoadingSpinner.vue'
import ArrowLeft from '@/icons/ArrowLeft.vue'

export default defineComponent({
  name: 'TweetDetail',
  components: {
    ReplyForm,
    Responses,
    TweetDetailDiscussion,
    ArrowLeft,
    LoadingSpinner
  },
  setup () {
    const state = reactive({
      id: router.currentRoute.value.params.id,
      tweet: ref<Array<Tweet>>([]),
      loading: true,
      replying: false
    })

    onBeforeMount(async () => {
      state.tweet = await fetchPublicDetailTweet(`/tweets/${state.id}`)
      state.loading = false
    })

    watch(store.getters.getReplying, _value => {
      state.replying = store.getters.getReplying.replying
    })

    function scrollTopThread () {
      return window.scrollTo(0, 0)
    }

    return { state, redirect, moment, scrollTopThread }
  }
})
</script>

<template>
  <div class="relative">
    <div
      v-show="state.replying"
      class="fixed top-0 left-0 w-full h-screen grid place-items-center bg-dark bg-opacity-90 z-50"
    >
      <ReplyForm class="border bg-dark" />
    </div>
    <div
      class="flex items-center space-x-6 border-b border-l border-r border-dark-grey bg-body cursor-pointer sticky top-0 z-20 p-4"
    >
      <router-link
        to="/"
        class="transition ease-in-out duration-200 rounded-full hover:bg-dark-grey p-1"
      >
        <ArrowLeft class="transform scale-90" />
      </router-link>
      <div class="font-medium text-lg" @click="scrollTopThread">Thread</div>
    </div>
    <LoadingSpinner
      v-if="state.loading"
      class="grid place-items-center mt-12"
    />
    <div
      class="flex flex-col border border-dark-grey rounded space-y-4 my-8 p-4"
      v-if="state.tweet"
    >
      <div class="flex items-center space-x-4">
        <div
          class="w-14 h-14 bg-dark border border-dark-grey rounded-full cursor-pointer"
          @click="
            redirect($event, 'user-tweet', {
              username: state.tweet[0]?.author.username
            })
          "
        ></div>
        <div
          class="flex flex-col cursor-pointer on-hover"
          @click="
            redirect($event, 'user-tweet', {
              username: state.tweet[0]?.author.username
            })
          "
        >
          <div class="font-medium text-base hovered">
            {{ state.tweet[0]?.author.name || state.tweet[0]?.author.username }}
          </div>
          <span class="text-peach text-sm"
            >@{{ state.tweet[0]?.author.username }}</span
          >
        </div>
      </div>
      <div class="text-xl">
        {{ state.tweet[0]?.content }}
      </div>
      <picture
        v-if="state.tweet[0]?.pictures"
        class="border border-dark-grey rounded"
      >
        <img
          alt="test tweet picture"
          class="w-full rounded-md"
          :src="state.tweet[0]?.pictures"
        />
      </picture>
      <div class="divide-y divide-dark-grey space-y-3">
        <div class="flex text-peach text-ms space-x-2">
          <span>{{
            moment(state.tweet[0]?.created_at).format("h:mm a • MMMM Do, YYYY")
          }}</span>
          <span>•</span>
          <span>Tweeted From Web</span>
        </div>
        <div class="flex text-base space-x-6 pt-3">
          <div class="space-x-1">
            <span class="text-white">{{
              state.tweet[0]?.responses?.comments_count
            }}</span>
            <span class="text-peach">Replies</span>
          </div>
          <div class="space-x-1">
            <span class="text-white">0</span>
            <span class="text-peach">Retweets</span>
          </div>
          <div class="space-x-1">
            <span class="text-white">{{
              state.tweet[0]?.responses?.likes_count
            }}</span>
            <span class="text-peach">Likes</span>
          </div>
        </div>
        <div class="pt-3">
          <Responses
            :responses="state.tweet[0]?.responses"
            :tweetId="state.tweet[0]?.id || ''"
            :authors="state.tweet[0]?.author"
            :picture="state.tweet[0]?.pictures"
            :content="state.tweet[0]?.content"
            :details="true"
            class="text-peach text-ms"
          />
        </div>
      </div>
    </div>
    <div
      v-if="state.tweet[0]"
      class="flex flex-col border border-dark-grey rounded space-y-4 my-8"
    >
      <TweetDetailDiscussion :tweetId="state.tweet[0]?.id" />
    </div>
  </div>
</template>
