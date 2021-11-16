<script lang="ts">
import { defineComponent, reactive } from 'vue'
import router from '@/routes'

import { ErrorLogin } from './types'
import loginService from './services/login'

import LoadingSpinner from '@/components/shared/LoadingSpinner.vue'

export default defineComponent({
  name: 'Login',
  components: {
    LoadingSpinner
  },
  setup () {
    const errors = reactive<ErrorLogin>({ detail: '' })
    const state = reactive({
      email: '',
      password: '',
      submitted: false
    })

    async function login (): Promise<void> {
      state.submitted = true
      const error = await loginService.authenticate(state.email, state.password)

      if (error) errors.detail = error || ''
      else router.push('/')
      state.submitted = false
    }

    return { state, errors, login }
  }
})
</script>

<template>
  <div class="grid grid-cols-2 h-screen">
    <div class="col-span-1 grid place-items-center">
      <div class="ml-20">
        <h1 class="font-semibold uppercase text-10xl leading-tight tracking-tighter">roll in</h1>
        <div class="w-4/5 text-sm">
          Popular culture is a place where pity is called compassion, flattery
          is called love, propaganda is called knowledge, tension is called
          peace, and gossip is called news.
        </div>
      </div>
    </div>
    <div class="col-span-1 grid place-items-center">
      <LoadingSpinner v-if="state.submitted" />
      <form
        v-else
        @submit.prevent="login"
        class="border-t border-dark-grey space-y-6 pt-8"
        :class="{ 'hidden': state.submitted }"
      >
        <div class="flex flex-col space-y-4">
          <label for="email" class="capitalize font-medium text-xl">your email</label>
          <input
            class="w-input bg-dark rounded-sm px-4 p-3 text-base"
            type="email"
            name="email"
            placeholder="account@gmail.com"
            v-model="state.email"
          />
        </div>
        <div class="flex flex-col space-y-4">
          <label for="email" class="capitalize font-medium text-xl">your password</label>
          <input
            class="w-input bg-dark rounded-sm px-4 p-3 text-base"
            type="password"
            name="password"
            placeholder="************"
            v-model="state.password"
          />
        </div>
        <div v-if="errors.detail" class="text-red-500 rounded-sm">
          {{ errors.detail }}
        </div>
        <div class="flex flex-col space-y-4">
          <button
            class="w-input bg-dark hover:bg-black border border-dark-grey rounded-sm capitalize text-base px-4 p-3"
          >login</button>
        </div>
        <div class="text-ms">
          <div class="space-x-1">
            <span>Are you new here?</span>
            <router-link to="/register" class="text-blue-500 hover:underline">Join us here &#x1F448;</router-link>
          </div>
          <div class="space-x-1">
            <span>Cannot remember your password?</span>
            <router-link to="/" class="text-blue-500 hover:underline">Let us handle that &#x1F44C;</router-link>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
