<script lang="ts">
import { defineComponent, ref, reactive, watch, onBeforeMount } from 'vue'
import router from '@/routes'
import { redirect, dashToCamelCase, camelToDashCase } from '@/utils/helper'

import { StateUser } from '@/modules/auth/types'
import { keyItems } from '@/modules/user/types'

export default defineComponent({
  name: 'UserInfo',
  props: {
    userInfo: {
      required: true,
      type: Object as () => StateUser
    }
  },
  setup () {
    const state = reactive({
      default: 'user-tweet',
      currentTab: '',
      tabArrays: [
        'userTweet',
        'userReply',
        'userMedia',
        'userLike'
      ],
      tabActive: ref<keyItems>({
        userTweet: false,
        userReply: false,
        userMedia: false,
        userLike: false
      }),
      active: 'text-current border-b-2 border-peach'
    })

    function checkActiveTab (tab: string): boolean {
      if (
        state.tabActive[state.currentTab] === true &&
        state.currentTab === tab
      ) {
        return true
      }

      return false
    }

    watch(router.currentRoute, route => {
      const routeName = dashToCamelCase(
        (route.name || state.default).toString()
      )
      state.tabActive[routeName] = true
      state.currentTab = routeName
    })

    onBeforeMount(() => {
      state.currentTab = dashToCamelCase(
        (router.currentRoute.value.name || state.default).toString()
      )
      state.tabActive[state.currentTab] = true
    })

    return { state, redirect, checkActiveTab, camelToDashCase }
  }
})
</script>

<template>
  <div v-if="userInfo" class="flex flex-col items-center space-y-4 mt-8">
    <div class="w-40 h-40 bg-dark border border-dark-grey rounded-full"></div>
    <div class="flex flex-col text-center space-y-2">
      <h1 class="font-medium text-3xl">{{ userInfo.username }}</h1>
      <div class="w-3/4 text-peach mx-auto">
        The worst thing about being at the top of the career ladder is that there's a long way to fall.
      </div>
    </div>
  </div>
  <div class="grid grid-cols-4 text-center text-peach border border-dark-grey rounded cursor-pointer mt-4">
    <div
      v-for="(item, index) in state.tabArrays"
      v-bind:key="index"
      class="capitalize hover:bg-dark py-4"
      :class="{[state.active]: checkActiveTab(item)}"
      @click="redirect($event, camelToDashCase(item), { username: userInfo.username })"
    >{{ camelToDashCase(item).split('-')[1] }}</div>
  </div>
</template>
