<script lang="ts">
import { defineComponent } from 'vue'
import Responses from '../../components/shared/Responses.vue'

export default defineComponent({
  name: 'TweetCards',
  components: {
    Responses
  },
  setup () {
    // eslint-disable-next-line
    function stopEvent(event: any) {
      // stop any default behavior of the event
      event.cancelBubble = true
      if (event.stopPropagation) {
        event.stopPropagation()
        event.preventDefault()
      }
    }

    // eslint-disable-next-line
    function redirect(this: any, event: any, url: string, parameters: any) {
      // redirect to the url with the given parameters
      const target = event.currentTarget.attributes['data-event']
      const routed = { name: url, params: parameters }

      if (target) {
        this.$router.push(routed)
        stopEvent(event)
      } else {
        this.$router.push(routed)
      }
    }

    return {
      redirect
    }
  }
})
</script>

<template>
  <div class="flex flex-col space-y-4">
    <!-- simple tweet -->
    <div
      class="grid grid-cols-12 border border-dark-grey rounded p-4"
      @click="redirect($event, 'tweet-detail', { username: 'matt_dreaming', id: '1' })"
    >
      <div class="col-span-1 mx-auto">
        <div class="w-10 h-10 bg-dark border border-dark-grey rounded-full"></div>
      </div>
      <div class="col-span-11 ml-4">
        <div
          class="inline-flex items-center cursor-pointer space-x-2 on-hover"
          @click="redirect($event, 'user-profile', { username: 'matt_dreaming' })"
          data-event="user-profile"
        >
          <div class="font-medium text-lg hovered">Matt Dreamson</div>
          <span class="text-peach text-sm">@matt_dreaming</span>
        </div>
        <div
          class="text-ms"
        >Lorem ipsum, dolor sit amet consectetur adipisicing elit. Illo sequi minus exercitationem aperiam quas. Aliquam similique quisquam cum totam. Nisi ullam eos accusantium, veritatis tenetur fugit nulla quia officiis maxime!</div>
        <Responses class="text-peach text-ms mt-4" />
      </div>
    </div>
    <!-- tweet with author response -->
    <div class="grid grid-cols-12 border border-dark-grey rounded p-4">
      <div class="col-span-1 relative overflow-hidden mx-auto">
        <div class="w-10 h-10 bg-dark border border-dark-grey rounded-full"></div>
        <div class="w-0.25 h-full bg-dark-grey mx-auto my-4"></div>
      </div>
      <div class="col-span-11 ml-4">
        <div class="flex items-center space-x-2">
          <div class="font-medium text-lg">Matt Dreamson</div>
          <span class="text-peach text-sm">@matt_dreaming</span>
        </div>
        <div
          class="text-ms"
        >Lorem ipsum, dolor sit amet consectetur adipisicing elit. Illo sequi minus exercitationem aperiam quas. Aliquam similique quisquam cum totam. Nisi ullam eos accusantium, veritatis tenetur fugit nulla quia officiis maxime!</div>
        <Responses class="text-peach text-ms mt-4" />
      </div>
      <div class="grid grid-cols-12 items-center col-span-12 cursor-pointer mt-4">
        <div class="col-span-1 relative overflow-hidden mx-auto">
          <div class="w-8 h-8 bg-dark border border-dark-grey rounded-full"></div>
        </div>
        <div class="col-span-11 text-peach hover:underline text-ms ml-4">Show this thread</div>
      </div>
    </div>
    <!-- tweet with picture -->
    <div class="grid grid-cols-12 border border-dark-grey rounded p-4">
      <div class="col-span-1 mx-auto">
        <div class="w-10 h-10 bg-dark border border-dark-grey rounded-full"></div>
      </div>
      <div class="col-span-11 ml-4">
        <div class="flex items-center space-x-2">
          <div class="font-medium text-lg">Matt Dreamson</div>
          <span class="text-peach text-sm">@matt_dreaming</span>
        </div>
        <div>
          <div class="overflow-hidden max-h-72">
            <img
              alt="test tweet picture"
              src="../../assets/eemu.jpg"
              class="w-full rounded-md mt-2"
            />
          </div>
          <Responses class="text-peach text-ms mt-4" />
        </div>
      </div>
    </div>
    <!-- tweet with picture & content -->
    <div class="grid grid-cols-12 border border-dark-grey rounded p-4">
      <div class="col-span-1 mx-auto">
        <div class="w-10 h-10 bg-dark border border-dark-grey rounded-full"></div>
      </div>
      <div class="col-span-11 ml-4">
        <div class="flex items-center space-x-2">
          <div class="font-medium text-lg">Matt Dreamson</div>
          <span class="text-peach text-sm">@matt_dreaming</span>
        </div>
        <div>
          <div
            class="text-ms"
          >Lorem ipsum, dolor sit amet consectetur adipisicing elit. Illo sequi minus exercitationem aperiam quas. Aliquam similique quisquam cum totam. Nisi ullam eos accusantium, veritatis tenetur fugit nulla quia officiis maxime!</div>
          <div class="overflow-hidden max-h-72">
            <img
              alt="test tweet picture"
              src="../../assets/eemu.jpg"
              class="w-full rounded-md mt-2"
            />
          </div>
          <Responses class="text-peach text-ms mt-4" />
        </div>
      </div>
    </div>
    <!-- tweet with picture & content & author response -->
    <div class="grid grid-cols-12 border border-dark-grey rounded p-4">
      <div class="col-span-1 relative overflow-hidden mx-auto">
        <div class="w-10 h-10 bg-dark border border-dark-grey rounded-full"></div>
        <div class="w-0.25 h-full bg-dark-grey mx-auto my-4"></div>
      </div>
      <div class="col-span-11 ml-4">
        <div class="flex items-center space-x-2">
          <div class="font-medium text-lg">Matt Dreamson</div>
          <span class="text-peach text-sm">@matt_dreaming</span>
        </div>
        <div>
          <div
            class="text-ms"
          >Lorem ipsum, dolor sit amet consectetur adipisicing elit. Illo sequi minus exercitationem aperiam quas. Aliquam similique quisquam cum totam. Nisi ullam eos accusantium, veritatis tenetur fugit nulla quia officiis maxime!</div>
          <div class="overflow-hidden max-h-72">
            <img
              alt="test tweet picture"
              src="../../assets/eemu.jpg"
              class="w-full rounded-md mt-2"
            />
          </div>
          <Responses class="text-peach text-ms mt-4" />
        </div>
      </div>
      <div class="grid grid-cols-12 items-center col-span-12 cursor-pointer mt-4">
        <div class="col-span-1 relative overflow-hidden mx-auto">
          <div class="w-8 h-8 bg-dark border border-dark-grey rounded-full"></div>
        </div>
        <div class="col-span-11 text-peach hover:underline text-ms ml-4">Show this thread</div>
      </div>
    </div>
  </div>
</template>
