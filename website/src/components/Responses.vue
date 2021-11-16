<script lang="ts">
import { defineComponent } from 'vue'
import axiosInstance from '@/services/axios'

import store from '@/store'
import { Tweet, TweetAuthor, TweetResponse } from '@/modules/tweets/types'
import { stopEvent, formatNumWithAbbreviation } from '@/utils/helper'

import TweetReply from '@/icons/TweetReply.vue'
import TweetRetweet from '@/icons/TweetRetweet.vue'
import TweetLike from '@/icons/TweetLike.vue'
import TweetShare from '@/icons/TweetShare.vue'

export default defineComponent({
  name: 'Responses',
  components: {
    TweetReply,
    TweetRetweet,
    TweetLike,
    TweetShare
  },
  props: {
    responses: { type: Object as () => TweetResponse | undefined },
    authors: { type: Object as () => TweetAuthor | undefined },
    picture: { type: String as () => string | undefined },
    content: { type: String as () => string | undefined },
    tweetId: { type: String, required: true },
    details: {
      type: Boolean,
      default: false
    }
  },
  setup () {
    async function replyTweet (
      event: Event,
      authors: TweetAuthor | undefined,
      picture: string | undefined,
      content: string | undefined,
      tweetId: string
    ): Promise<void> {
      stopEvent(event)

      console.log('responses', authors)
      store.commit('setTweetId', tweetId)
      store.commit('setAuthor', authors)
      store.commit('setContent', content)
      store.commit('setPicture', picture)
      store.commit('setReplying', true)
    }

    async function likeTweet (event: Event, id: string): Promise<void> {
      stopEvent(event)

      const tweat = document.querySelector(`div[response-id='${id}']`)
      const domLike = tweat?.children[2].children[0]

      if (domLike !== undefined) {
        let likeCount = Number(domLike.getAttribute('data-count'))

        if (domLike.getAttribute('data-liked') === 'true') {
          await axiosInstance.delete(`/tweets/like/${id}`)
          likeCount -= 1
          domLike.classList.remove('liked')
          domLike.setAttribute('data-liked', 'false')
        } else {
          await axiosInstance.put(`/tweets/like/${id}`)
          likeCount += 1
          domLike.classList.add('liked')
          domLike.setAttribute('data-liked', 'true')
        }

        domLike.setAttribute('data-count', likeCount.toString());
        (domLike
          .children[1] as HTMLElement).innerText = formatNumWithAbbreviation(
          likeCount
        )
      }
    }

    return { likeTweet, replyTweet, formatNumWithAbbreviation }
  }
})
</script>

<template>
  <div class="grid grid-cols-4 text-peach" :response-id="tweetId">
    <div
      class="inline-flex space-x-2"
      data-type="reply"
      :class="{ 'mx-auto': details }"
    >
      <div
        class="flex items-center cursor-pointer response-hover space-x-2"
        @click="replyTweet($event, authors, picture, content, tweetId)"
      >
        <span class="hover-reply">
          <TweetReply class="rounded-full transform scale-125 p-1" />
        </span>
        <span v-if="responses?.comments_count" class="hover-reply">{{
          responses?.comments_count
        }}</span>
      </div>
    </div>
    <div
      class="inline-flex space-x-2"
      data-type="retweet"
      :class="{ 'mx-auto': details }"
    >
      <div class="flex items-center cursor-pointer response-hover space-x-2">
        <span class="hover-retweet">
          <TweetRetweet class="rounded-full transform scale-125 p-1" />
        </span>
        <span v-if="0" class="hover-retweet">{{ 0 }}</span>
      </div>
    </div>
    <div
      class="inline-flex space-x-2"
      data-type="like"
      :class="{ 'mx-auto': details }"
    >
      <div
        class="flex items-center cursor-pointer response-hover space-x-2"
        :class="{ liked: responses?.liked }"
        :data-count="responses?.likes_count"
        :data-liked="responses?.liked"
        @click="likeTweet($event, tweetId)"
      >
        <span class="hover-like">
          <TweetLike class="rounded-full transform scale-125 p-1" />
        </span>
        <span
          class="hover-like"
          >{{ formatNumWithAbbreviation((responses?.likes_count as number)) }}</span
        >
      </div>
    </div>
    <div class="inline-flex space-x-2" :class="{ 'mx-auto': details }">
      <div class="flex items-center cursor-pointer response-hover space-x-2">
        <span class="hover-share">
          <TweetShare class="rounded-full transform scale-125 p-1" />
        </span>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.liked {
  svg {
    fill: crimson;
    path {
      stroke: crimson !important;
    }
  }
  span {
    color: crimson !important;
  }
}

.response-hover:hover {
  .hover-reply {
    svg {
      background: rgba(52, 211, 153, 0.1);
      path {
        stroke: #34d399;
      }
    }
    color: #34d399;
  }
  .hover-retweet {
    svg {
      background-color: rgba(91, 91, 241, 0.1);
      path {
        stroke: rgb(91, 91, 241);
      }
    }
    color: rgb(91, 91, 241);
  }
  .hover-like {
    svg {
      background-color: rgba(220, 20, 60, 0.1);
      path {
        stroke: crimson;
      }
    }
    color: crimson;
  }
  .hover-share {
    svg {
      background-color: rgba(91, 91, 241, 0.1);
      path {
        stroke: rgb(91, 91, 241);
      }
    }
    color: rgb(91, 91, 241);
  }
}
</style>
