<script lang="ts">
import { defineComponent, ref, reactive } from 'vue'
import axiosInstance from '@/services/axios'

import store from '@/store'
import { StateUser } from '@/modules/auth/types'

import FormImage from '@/icons/FormImage.vue'

export default defineComponent({
  name: 'TweetForms',
  components: {
    FormImage
  },
  setup (_, { emit }) {
    const user: StateUser = store.getters.getUser
    const picture = ref<HTMLImageElement>(new Image())
    const tweetInput = ref<HTMLElement>()
    const state = reactive({
      picture: ref<File>(),
      imgAlt: '',
      tweet: '',
      error: '',
      tweeting: false
    })

    async function sendTweet () {
      state.tweeting = true
      const formData = new FormData()

      // append data to form-data
      if (state.tweet || state.picture) {
        formData.append('content', state.tweet)
        formData.append('pictures', state.picture ? state.picture : '')
      }

      // post data to api
      await axiosInstance.post('/tweets/', formData).then(() => {
        state.tweeting = false
        // clear form
        if (tweetInput.value && picture.value) {
          tweetInput.value.innerText = 'What\'s in your mind?'
          picture.value.src = '#'
        }

        emit('tweetSent')
      })
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

    return { state, user, picture, tweetInput, sendTweet, uploadPicture }
  }
})
</script>

<template>
  <form
    @submit.prevent="sendTweet"
    class="flex flex-col rounded border mt-8 p-4"
    :class="[
      { 'border-green-500': state.tweeting },
      { 'border-dark-grey': !state.tweeting }
    ]"
  >
    <div class="flex items-center space-x-4">
      <div class="w-10 h-10 bg-dark border border-dark-grey rounded-full"></div>
      <div class="text-lg font-medium">{{ user.username }}</div>
    </div>
    <div class="form-wrap overflow-y-auto max-h-56 ml-10 pl-4">
      <div
        ref="tweetInput"
        contenteditable="true"
        class="forms text-gray-500"
        @input="(e) => (state.tweet = (e.target as HTMLElement).innerText)"
      >
        What's in your mind?
      </div>
    </div>
    <div class="overflow-hidden rounded-md ml-10 pl-4 my-2">
      <img
        ref="picture"
        :alt="state.imgAlt"
        class="w-full rounded-md"
        src="#"
      />
    </div>
    <div class="ml-10 pl-4">
      <div
        class="flex justify-between items-center border-t border-dark-grey pt-4"
      >
        <div class="flex space-x-4">
          <div
            class="inline-flex space-x-2 transition ease-in-out duration-300"
          >
            <div class="flex items-center cursor-pointer image-hover space-x-2">
              <input
                id="uploadPicture"
                class="hidden"
                type="file"
                accept="image/*"
                @change="uploadPicture($event)"
              />
              <label for="uploadPicture" title="Media" class="cursor-pointer">
                <FormImage
                  class="rounded-full transform scale-125 transition ease-in-out duration-300 p-1"
                />
              </label>
            </div>
          </div>
        </div>
        <button
          type="submit"
          class="cursor-pointer rounded bg-dark-grey px-8 py-1.5"
        >
          Tweet
        </button>
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
