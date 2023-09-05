<script setup>
import { RouterView } from 'vue-router'
import Footer from './components/Footer.vue';
</script>

<template>
  <RouterView v-slot="{ Component, route }">
    <transition :name="route.meta.transition">
      <component :is="Component"/>
    </transition>
  </RouterView>
  <Footer />
</template>

<style scoped>
.slide-left-enter-active,
.slide-left-leave-active,
.slide-right-enter-active,
.slide-right-leave-active{
  transition: opacity 0.5s, transform 0.5s;
}
.slide-left-enter-from,
.slide-right-leave-to{
  opacity: 1;
  transform: translateX(-100%);
}
.slide-left-leave-to,
.slide-right-enter-from{
  opacity: 1;
  transform: translateX(100%);
}
</style>