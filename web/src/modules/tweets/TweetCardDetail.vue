<script lang="ts">
import { defineComponent } from 'vue'
import Responses from '../../components/shared/Responses.vue'
import TweetDetailDiscussion from './TweetDetailDiscussion.vue'

import ArrowLeft from '../../icons/ArrowLeft.vue'

export default defineComponent({
  name: 'TweetCardDetail',
  components: {
    Responses,
    TweetDetailDiscussion,

    ArrowLeft
  },
  setup () {
    function scrollTop () {
      window.scrollTo(0, 0)
    }

    return {
      scrollTop
    }
  }
})
</script>

<template>
  <div
    class="flex items-center space-x-6 border-b border-l border-r border-dark-grey bg-body cursor-pointer sticky top-0 z-50 p-4"
  >
    <router-link to="/" class="transition ease-in-out duration-200 rounded-full hover:bg-dark-grey p-1">
      <ArrowLeft class="transform scale-90" />
    </router-link>
    <div class="font-medium text-lg" @click="scrollTop">Thread</div>
  </div>
  <div class="flex flex-col border border-dark-grey rounded space-y-4 my-8 p-4">
    <div class="flex items-center space-x-4">
      <div class="w-14 h-14 bg-dark border border-dark-grey rounded-full"></div>
      <div class="flex flex-col">
        <div class="font-medium text-base">Matt Dreamson</div>
        <span class="text-peach text-sm">@matt_dreaming</span>
      </div>
    </div>
    <div class="text-lg">
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Illo sequi minus
      exercitationem aperiam quas. Aliquam similique quisquam cum totam. Nisi
      ullam eos accusantium, veritatis tenetur fugit nulla quia officiis maxime!
    </div>
    <picture>
      <img
        alt="test tweet picture"
        src="../../assets/eemu.jpg"
        class="w-full rounded-md mt-2"
      />
    </picture>
    <div class="divide-y divide-dark-grey space-y-3">
      <div class="flex text-peach text-ms space-x-2">
        <span>8:26 PM</span>
        <span>•</span>
        <span>Oct 17, 2021</span>
        <span>•</span>
        <span>Tweeted From Web</span>
      </div>
      <div class="flex text-base space-x-6 pt-3">
        <div class="space-x-1">
          <span class="text-white">100</span>
          <span class="text-peach">Replies</span>
        </div>
        <div class="space-x-1">
          <span class="text-white">100</span>
          <span class="text-peach">Retweets</span>
        </div>
        <div class="space-x-1">
          <span class="text-white">100</span>
          <span class="text-peach">Likes</span>
        </div>
      </div>
      <div class="pt-3">
        <Responses class="text-peach text-ms" :inDetail="true" />
      </div>
    </div>
  </div>
  <div class="flex flex-col border border-dark-grey rounded space-y-4 my-8">
    <TweetDetailDiscussion />
  </div>
</template>
