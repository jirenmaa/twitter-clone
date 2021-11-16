<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'LoadingSpinner'
})
</script>

<template>
  <div>
    <div class="lds-ring">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
  </div>
</template>

<style scoped>
.lds-ring {
  display: inline-block;
  position: relative;
  /* width: 80px;
  height: 80px; */
  width: 50px;
  height: 50px;
}
.lds-ring div {
  box-sizing: border-box;
  display: block;
  position: absolute;
  width: 38px;
  height: 38px;
  margin: 8px;
  border: 3px solid #ddd;
  border-radius: 50%;
  animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  border-color: #ddd transparent transparent transparent;
}
.lds-ring div:nth-child(1) {
  animation-delay: -0.45s;
}
.lds-ring div:nth-child(2) {
  animation-delay: -0.3s;
}
.lds-ring div:nth-child(3) {
  animation-delay: -0.15s;
}
@keyframes lds-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
