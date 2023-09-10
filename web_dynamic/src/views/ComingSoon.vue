<script setup>
import Navbar from '@/components/Navbar.vue';
</script>
<template>
  <div>
    <Navbar :showsearch="true" />
    <section>
      <h1>Coming Soon...</h1>
      <p>This Feature is still under development</p>
      <img src="@/assets/images/development.png" alt="reconstruct your query" class="error-image">
    </section>
  </div>
</template>
<style scoped>
section{
  width: 100%;
  padding: 50px;
  text-align: center;
  min-height: 25em;
}
h1{
  font-weight: 600;
  font-size: 50px;
}
p{
  font-size: 24px;
}
.error-image{
    margin: 30px;
    height: 300px;
    width: 300px;
}
</style>