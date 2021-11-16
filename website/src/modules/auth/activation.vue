<script lang="ts">
import { defineComponent, reactive } from 'vue'

import router from '@/routes'
import activationService from './services/activation'

export default defineComponent({
  name: 'Activation',
  setup () {
    const state = reactive({
      loading: false,
      email: '',
      success: false,
      isResetActivation: false
    })

    /**
     * send new activation for user
     *
     * @param {string} email
     * @returns {Promise<void>}
     */
    async function sendNewActivation (): Promise<void> {
      const errors = await activationService.resetActivation(state.email)
      state.success = !!errors
    }

    /**
     * send activation to backend
     *
     * @param {string} key
     * @returns {Promise<void>}
     */
    async function sendActivation (): Promise<void> {
      const key = (router.currentRoute.value.query.key as string) || ''

      const response = await activationService.activate(key)
      state.success = response || false
    }

    sendActivation()

    return { state, sendActivation, sendNewActivation }
  }
})
</script>

<template>
  <div
    class="grid place-items-center h-screen"
    v-if="!state.loading && !state.isResetActivation"
  >
    <div class="space-y-4" v-if="state.success">
      <div class="font-jakarta font-medium capitalize text-8xl">
        Welcome &#127881;
      </div>
      <div class="text-lg space-x-2">
        <span>Your account has been activated.</span>
        <router-link to="/login" class="text-blue-500 hover:underline"
          >login now</router-link
        >
      </div>
    </div>
    <div class="space-y-4 mx-60" v-else>
      <div class="font-jakarta leading-tight font-medium text-6xl">
        It appears that your activation link has expired &#x270B;
      </div>
      <div class="text-lg space-x-2">
        <span>Do you want us to send you a new activation links?</span>
        <span class="cursor-pointer text-blue-500 hover:underline"
          @click="(e) => state.isResetActivation = true"
          >Yes send me a new one</span
        >
      </div>
    </div>
  </div>
  <div class="grid place-items-center h-screen" v-else>
    <form class="space-y-6" @submit.prevent="sendNewActivation">
      <div v-if="state.success" class="text-green-500 w-96">
        We have send new account activation link to your email! 🎉
      </div>
      <div class="flex flex-col space-y-4">
        <label for="email" class="capitalize font-medium text-xl">your email</label>
        <input
          class="w-96 bg-dark text-base rounded-sm px-4 p-3"
          type="email"
          name="email"
          placeholder="account@gmail.com"
          v-model="state.email"
        />
      </div>
      <div class="flex flex-col space-y-4">
        <button
          class="w-96 bg-dark hover:bg-black border border-dark-grey rounded-sm capitalize text-base px-4 p-3"
        >reset activation</button>
      </div>
    </form>
  </div>
</template>
