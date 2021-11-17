<script lang="ts">
import { defineComponent, ref, reactive, watch, onBeforeMount } from 'vue'
import { redirect, dashToCamelCase, camelToDashCase } from '@/utils/helper'
import router from '@/routes'

import { keyItems, UserInfo } from '@/modules/user/types'
import { fetchUserInfo } from '@/modules/user/services/info'

export default defineComponent({
  name: 'UserInfo',
  setup () {
    const state = reactive({
      default: 'user-tweet',
      currentTab: '',
      tabArrays: ['userTweet', 'userReply', 'userMedia', 'userLike'],
      tabActive: ref<keyItems>({
        userTweet: false,
        userReply: false,
        userMedia: false,
        userLike: false
      }),
      performer: ref<UserInfo>({
        username: '',
        name: '',
        avatar: ''
      }),
      active: 'text-current border-b-2 border-peach'
    })

    watch(router.currentRoute, route => {
      setUserInfo()
      const routeName = dashToCamelCase(
        (route.name || state.default).toString()
      )
      state.tabActive[routeName] = true
      state.currentTab = routeName
    })

    onBeforeMount(async () => {
      setUserInfo()
      state.currentTab = dashToCamelCase(
        (router.currentRoute.value.name || state.default).toString()
      )
      state.tabActive[state.currentTab] = true
    })

    function checkActiveTab (tab: string, currentTab: string): boolean {
      return state.tabActive[currentTab] === true && currentTab === tab
    }

    async function setUserInfo (): Promise<void> {
      const { username, name, avatar } = await fetchUserInfo(
        router.currentRoute.value?.params?.username as string
      )
      state.performer = { username, name, avatar } as UserInfo
    }

    return { state, checkActiveTab, camelToDashCase, redirect }
  }
})
</script>

<template>
  <div v-if="state.performer" class="flex flex-col items-center space-y-4 mt-8">
    <div class="w-40 h-40 bg-dark border border-dark-grey rounded-full"></div>
    <div class="flex flex-col text-center space-y-2">
      <h1 class="font-medium text-3xl">{{ state.performer.username }}</h1>
      <div class="w-3/4 text-peach mx-auto">
        The worst thing about being at the top of the career ladder is that
        there's a long way to fall.
      </div>
    </div>
  </div>
  <div
    class="grid grid-cols-4 text-center text-peach border border-dark-grey rounded cursor-pointer mt-4"
  >
    <div
      v-for="(item, index) in state.tabArrays"
      v-bind:key="index"
      class="capitalize hover:bg-dark py-4"
      :class="{ [state.active]: checkActiveTab(item, state.currentTab) }"
      @click="
        redirect($event, camelToDashCase(item), {
          username: state.performer.username
        })
      "
    >
      {{ camelToDashCase(item).split("-")[1] }}
    </div>
  </div>
</template>
