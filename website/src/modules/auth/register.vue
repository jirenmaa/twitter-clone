<script lang="ts">
import { defineComponent, reactive } from 'vue'

import { ErrorRegister } from './types'
import registerService from './services/register'

import LoadingSpinner from '@/components/shared/LoadingSpinner.vue'

export default defineComponent({
  name: 'Register',
  components: {
    LoadingSpinner
  },
  setup () {
    const errors = reactive<ErrorRegister>({ email: '' })
    const state = reactive({
      success: '',
      email: '',
      password: '',
      submitted: false
    })

    async function register (): Promise<void> {
      state.submitted = true
      const error = await registerService.register(state.email, state.password)

      if (error) errors.email = error?.email[0]
      else state.success = 'We have send account activation link to your email! 🎉'
      state.submitted = false
    }

    return { state, errors, register }
  }
})
</script>

<template>
  <div class="grid grid-cols-2 h-screen">
    <div class="col-span-1 grid place-items-center">
      <div class="ml-20">
        <h1
          class="font-semibold uppercase text-10xl leading-tight tracking-tighter"
        >
          join us
        </h1>
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
        @submit.prevent="register"
        class="border-t border-dark-grey space-y-6 pt-8"
      >
        <div v-if="state.success" class="text-green-500">
          {{ state.success }}
        </div>
        <div class="flex flex-col space-y-4">
          <label for="email" class="capitalize font-medium text-xl"
            >your email</label
          >
          <span v-if="errors.email" class="text-red-500 text-ms my-2">
            {{ errors.email }}
          </span>
          <input
            class="w-input bg-dark rounded-sm px-4 p-3 text-base"
            type="email"
            name="email"
            placeholder="account@gmail.com"
            v-model="state.email"
          />
        </div>
        <div class="flex flex-col space-y-4">
          <label for="email" class="capitalize font-medium text-xl"
            >your password</label
          >
          <input
            class="w-input bg-dark rounded-sm px-4 p-3 text-base"
            type="password"
            name="password"
            placeholder="************"
            v-model="state.password"
          />
        </div>
        <div class="flex flex-col space-y-4">
          <button
            class="w-input bg-dark hover:bg-black border border-dark-grey rounded-sm capitalize text-base px-4 p-3"
          >
            register
          </button>
        </div>
        <div class="text-ms">
          <div class="space-x-1">
            <span>Already have an account?</span>
            <router-link to="/login" class="text-blue-500 hover:underline"
              >Login here &#x1F448;</router-link
            >
          </div>
          <div class="space-x-1">
            <span>Cannot remember your password?</span>
            <router-link to="/" class="text-blue-500 hover:underline"
              >Let us handle that &#x1F44C;</router-link
            >
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
