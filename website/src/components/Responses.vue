<script lang="ts">
import { defineComponent, watch } from 'vue'

import {
  responseLikeUnlineTweet,
  responseReplyTweet,
  responseReplyDetailTweet
} from '@/modules/tweets/services/actions'

import store from '@/store'
import {
  TweetAuthor,
  TweetResponse,
  StoreTweetReply
} from '@/modules/tweets/types'
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
      store.commit('setReplyState', {
        replying: true,
        tweetId: tweetId,
        author: authors,
        picture: picture,
        content: content
      } as StoreTweetReply)
    }

    watch(store.getters.getReplying, data => {
      if (data.replying && data.success) {
        const tweetPublic = document.querySelector(
          `div[response-id='${data.tweetId}']`
        )
        const tweetDetail = document.querySelector(
          `div[response-detail-id='${data.tweetId}']`
        )

        if (tweetDetail === null) {
          console.log('in tweet public')
          responseReplyTweet(tweetPublic as Element)
          store.commit('setResetState')
        }
        if (tweetPublic && tweetDetail) {
          console.log('in tweet detail')
          responseReplyDetailTweet(tweetDetail as Element)
        }
      }
    })

    async function likeTweet (event: Event, id: string): Promise<void> {
      stopEvent(event)

      const tweet = document.querySelector(`div[response-id='${id}']`)
      responseLikeUnlineTweet(event, tweet as HTMLElement, id)
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
        :data-count="responses?.comments_count"
      >
        <span class="hover-reply">
          <TweetReply class="rounded-full transform scale-125 p-1" />
        </span>
        <span v-if="!details" class="hover-reply">{{
          formatNumWithAbbreviation(responses?.comments_count as number)
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
        <span v-if="0" class="hover-retweet">{{ formatNumWithAbbreviation(0) }}</span>
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
          v-if="!details"
          class="hover-like"
          >{{ formatNumWithAbbreviation(responses?.likes_count as number) }}</span
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
