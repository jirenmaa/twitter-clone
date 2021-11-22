<script lang="ts">
import { defineComponent, ref, watch, onMounted, reactive } from 'vue'
import axiosInstance from '@/services/axios'

import store from '@/store'
import { TweetAuthor } from '@/modules/tweets/types'

import ButtonSubmit from '@/components/shared/ButtonSubmit.vue'
import IconImage from '@/icons/FormImage.vue'
import IconClose from '@/icons/IconClose.vue'

export default defineComponent({
  name: 'ReplyForm',
  components: {
    ButtonSubmit,
    IconImage,
    IconClose
  },
  setup () {
    const tweetReplied = reactive({
      author: { name: '', username: '', avatar: '' },
      tweetId: '',
      content: '',
      picture: '',
      dataFetch: false
    })
    const picture = ref<HTMLImageElement>(new Image())
    const tweetInput = ref<HTMLElement>()
    const state = reactive({
      picture: ref<File>(),
      imgAlt: '',
      tweet: '',
      error: '',
      tweeting: false
    })

    watch(store.getters.getReplying, _ => {
      const datas = store.getters.getReplying
      if (datas.replying) {
        tweetReplied.author = datas.author as TweetAuthor
        tweetReplied.tweetId = datas.tweetId
        tweetReplied.content = datas.content
        tweetReplied.picture = datas.picture
        tweetReplied.dataFetch = true
      }
    })

    async function closeReply () {
      await store.commit('setResetState')
    }

    async function sendReply () {
      state.tweeting = true
      const formData = new FormData()

      // append data to form-data
      if (state.tweet || state.picture) {
        formData.append('tweet', tweetReplied.tweetId)
        formData.append('content', state.tweet)
        formData.append('pictures', state.picture ? state.picture : '')
      }

      await axiosInstance.post('/tweets/comment/', formData)
        // clear reply form
        .then(() => {
          store.commit('setSuccess', true)
          if (tweetInput.value && picture.value) {
            tweetInput.value.innerText = 'Tweet your reply'
            picture.value.src = '#'
          }
        })
      state.tweeting = false
    }

    async function uploadPicture (event: Event) {
      // get file image from event
      const fileImage = event.target as HTMLInputElement
      // save file to state
      if (fileImage.files !== null) state.picture = fileImage.files[0]
      // render image preview
      if (picture.value !== undefined) {
        picture.value.src = URL.createObjectURL(state.picture)
      }
    }

    return {
      state,
      tweetReplied,
      picture,
      tweetInput,
      sendReply,
      closeReply,
      uploadPicture
    }
  }
})
</script>

<template>
  <form
    @submit.prevent="sendReply"
    class="grid grid-cols-12 relative w-form form-wrap overflow-y-auto rounded border"
    :class="[
      { 'border-green-500': state.tweeting },
      { 'border-dark-grey': !state.tweeting }
    ]"
  >
    <div class="col-span-12 sticky top-0 bg-dark border-b border-dark-grey py-2 px-4 z-50">
      <div class="inline-flex cursor-pointer hover:bg-dark-grey transform transition ease-in-out duration-300 rounded-full p-1" @click="closeReply">
        <IconClose class="rounded-full transform scale-125 p-1" />
      </div>
    </div>
    <div class="col-span-1 relative overflow-hidden mx-auto py-4 pl-4 px-4">
      <div class="w-12 h-12 bg-dark border border-dark-grey rounded-full"></div>
      <div class="w-0.25 h-3/4 bg-dark-grey mx-auto my-4"></div>
    </div>
    <div class="col-span-11 text-ms ml-4 p-4 px-4">
      <div class="flex text-base space-x-1">
        <span class="font-medium">
          {{ tweetReplied.author.name || tweetReplied.author.username }}
        </span>
        <span class="text-peach text-sm">@{{ tweetReplied.author.username }}</span>
      </div>
      <div class="space-y-4">
        <div class="text-base space-x-1">
          <span>{{ tweetReplied.content }}</span>
          <span v-if="tweetReplied.picture" class="break-all text-blue-400">
            <a :href="tweetReplied.picture">
              {{ tweetReplied.picture.split('/').pop() }}
            </a>
          </span>
        </div>
        <div class="space-x-1 text-peach text-sm">
          <span>Replying to</span>
          <span class="text-blue-400">@{{ tweetReplied.author.username }}</span>
        </div>
      </div>
    </div>
    <div class="col-span-1 relative overflow-hidden mx-auto mt-4 pl-4 px-4">
      <div class="w-12 h-12 bg-dark border border-dark-grey rounded-full"></div>
    </div>
    <div class="col-span-11 max-h-56 ml-4 mt-4 px-8">
      <div
        ref="tweetInput"
        class="forms text-base text-gray-500"
        contenteditable="true"
        @input="(e) => (state.tweet = (e.target as HTMLElement).innerText)"
      >
        Tweet your reply
      </div>
      <div class="overflow-hidden border border-dark-grey rounded-md my-2">
        <img ref="picture" :alt="state.imgAlt" class="w-full rounded-md" src="#" />
      </div>
      <div
        class="flex justify-between items-center mt-4 pt-2 pb-4"
      >
        <div class="inline-flex image-hover transition ease-in-out duration-300">
          <input
            id="upload-image"
            class="hidden"
            type="file"
            accept="image/*"
            @change="uploadPicture($event)"
          />
          <label for="upload-image" title="Media" class="cursor-pointer">
            <IconImage class="rounded-full transform scale-125 transition ease-in-out duration-300 p-1" />
          </label>
        </div>
        <ButtonSubmit :padding="'px-8 py-1.5'" :context="'reply'" />
      </div>
    </div>
  </form>
</template>

<style lang="scss">
.form-wrap {
  scroll-behavior: smooth;
  scrollbar-width: thin;
  scrollbar-color: #ddd #222;
}
.form-wrap::-webkit-scrollbar {
  width: 3px !important;
  background: #222;
}
.form-wrap::-webkit-scrollbar-thumb {
  background-color: #ddd;
  border: 3px solid #ddd;
}
.forms {
  word-wrap: break-word;
}
.image-hover:hover {
  svg {
    background: rgba(52, 211, 153, 0.1);
    path {
      stroke: #34d399;
    }
  }
  color: #34d399;
}
</style>
