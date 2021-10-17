<script lang="ts">
import { defineComponent } from 'vue'
import Responses from '../../components/shared/Responses.vue'

export default defineComponent({
  name: 'TweetDetailDiscussion',
  components: {
    Responses
  },
  data (): {
    discussions: {
      author: string;
      content: string;
    }[]
    } {
    return {
      discussions: [
        {
          author: 'jirenmaa',
          content: 'Hello world'
        },
        {
          author: 'jirenmaa',
          content: 'Hello world'
        },
        {
          author: 'jirenmaa',
          content: 'Hello world'
        },
        {
          author: 'jirenmaa',
          content: 'Hello world'
        }
      ]
    }
  }
})
</script>

<template>
  <div class="divide-y divide-dark-grey">
    <div v-for="(discussion, index) in discussions" :key="index" class="p-4">
      <div class="grid grid-cols-12">
        <div class="col-span-1 mx-auto">
          <div class="w-10 h-10 bg-dark border border-dark-grey rounded-full"></div>
        </div>
        <div class="col-span-11 ml-2">
          <div class="flex items-center space-x-2">
            <div class="font-medium text-base">Jirenmaa</div>
            <span class="text-peach text-sm">@jirenmaa</span>
          </div>
          <div class="text-ms">
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Illo sequi minus exercitationem aperiam quas.
          </div>
          <Responses class="text-peach text-ms mt-4" />
        </div>
      </div>
    </div>
  </div>
</template>
