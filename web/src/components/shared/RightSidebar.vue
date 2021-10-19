<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'RightSidebar'
})
</script>

<template>
  <div class="flex flex-col sticky space-y-8 mt-8 top-8">
    <div class="flex flex-col space-y-4">
      <span class="uppercase font-medium">people you may know</span>
      <div class="relative space-y-3">
        <div class="on-hover cursor-pointer flex items-center space-x-4">
          <div class="w-9 h-9 bg-dark border border-dark-grey rounded-full"></div>
          <div class="items-center">
            <div class="hovered text-base font-medium">Carmela Conway</div>
            <div class="lowercase text-peach text-mm">Elvis Has Left The Building</div>
          </div>
        </div>
        <div class="on-hover cursor-pointer flex items-center space-x-4">
          <div class="w-9 h-9 bg-dark border border-dark-grey rounded-full"></div>
          <div class="items-center">
            <div class="hovered text-base font-medium">Ivory Cherry</div>
            <div class="lowercase text-peach text-mm">A Lot on One’s Plate</div>
          </div>
        </div>
        <div class="on-hover cursor-pointer flex items-center space-x-4">
          <div class="w-9 h-9 bg-dark border border-dark-grey rounded-full"></div>
          <div class="items-center">
            <div class="hovered text-base font-medium">Joann Cabrera</div>
            <div class="lowercase text-peach text-mm">Mountain Out of a Molehill</div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex flex-col space-y-4">
      <span class="uppercase font-medium">suggestion</span>
      <div class="relative space-y-4">
        <div class="on-hover flex items-center cursor-pointer space-x-4">
          <div class="items-center">
            <div class="hovered text-base font-medium">#isolate</div>
            <div class="text-peach text-mm">Trending 5 Tweets</div>
          </div>
        </div>
        <div class="on-hover flex items-center cursor-pointer space-x-4">
          <div class="items-center">
            <div class="hovered text-base font-medium">#shiver</div>
            <div class="text-peach text-mm">Trending 30 Tweets</div>
          </div>
        </div>
        <div class="on-hover flex items-center cursor-pointer space-x-4">
          <div class="items-center">
            <div class="hovered text-base font-medium">#propose</div>
            <div class="text-peach text-mm">Trending 15 Tweets</div>
          </div>
        </div>
        <div class="on-hover flex items-center cursor-pointer space-x-4">
          <div class="items-center">
            <div class="hovered text-base font-medium">#interfere</div>
            <div class="text-peach text-mm">Trending 23 Tweets</div>
          </div>
        </div>
        <div class="on-hover flex items-center cursor-pointer space-x-4">
          <div class="items-center">
            <div class="hovered text-base font-medium">#abandon</div>
            <div class="text-peach text-mm">Trending 102 Tweets</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
