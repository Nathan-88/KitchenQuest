<script setup>
import Navbar from '@/components/Navbar.vue';
</script>
<template>
  <div>
    <Navbar :showsearch="true" />
    <section>
      <h1>Sorry, Error processing your request</h1>
      <p>This may be due to bad connection or Invalid request</p>
      <img src="@/assets/images/alert-error.svg" alt="reconstruct your query" class="error-image">
    </section>
  </div>
</template>
<style scoped>
section{
  width: 100%;
  padding: 50px;
  text-align: center;
  min-height: 25rem;
}
h1{
  font-weight: 600;
  font-size: 2rem;
}
p{
  font-size: 1.5rem;
}
.error-image{
    margin: 30px;
    height: 200px;
    width: 200px;
}
</style>