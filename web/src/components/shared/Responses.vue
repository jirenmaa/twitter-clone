<script lang="ts">
import { defineComponent } from 'vue'

import TweetReply from '../../icons/TweetReply.vue'
import TweetRetweet from '../../icons/TweetRetweet.vue'
import TweetLike from '../../icons/TweetLike.vue'
import TweetShare from '../../icons/TweetShare.vue'

export default defineComponent({
  name: 'Responses',
  components: {
    TweetReply,
    TweetRetweet,
    TweetLike,
    TweetShare
  },
  props: {
    replies: { type: Number, default: 0 },
    retweets: { type: Number, default: 0 },
    likes: { type: Number, default: 0 },
    shares: { type: Number, default: 0 },
    inDetail: { type: Boolean, default: false }
  }
})
</script>

<template>
  <div class="grid grid-cols-4 text-peach">
    <div class="inline-flex space-x-2" :class="{'mx-auto': inDetail}">
      <div class="flex items-center cursor-pointer response-hover space-x-2">
        <span class="hover-reply">
          <TweetReply class="rounded-full transform scale-125 p-1" />
        </span>
        <span v-if="replies" class="hover-reply">{{ replies }}</span>
      </div>
    </div>
    <div class="inline-flex space-x-2" :class="{'mx-auto': inDetail}">
      <div class="flex items-center cursor-pointer response-hover space-x-2">
        <span class="hover-retweet">
          <TweetRetweet class="rounded-full transform scale-125 p-1" />
        </span>
        <span v-if="retweets" class="hover-retweet">{{ retweets }}</span>
      </div>
    </div>
    <div class="inline-flex space-x-2" :class="{'mx-auto': inDetail}">
      <div class="flex items-center cursor-pointer response-hover space-x-2">
        <span class="hover-like">
          <TweetLike class="rounded-full transform scale-125 p-1" />
        </span>
        <span v-if="likes" class="hover-like">{{ likes }}</span>
      </div>
    </div>
    <div class="inline-flex space-x-2" :class="{'mx-auto': inDetail}">
      <div class="flex items-center cursor-pointer response-hover space-x-2">
        <span class="hover-share">
          <TweetShare class="rounded-full transform scale-125 p-1" />
        </span>
        <span v-if="shares" class="hover-share">{{ shares }}</span>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
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
