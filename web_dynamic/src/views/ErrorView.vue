<script setup>
import Navbar from '../components/Navbar.vue';
</script>
<template>
  <div>
    <Navbar :showsearch="true" />
    <section>
      <h1>Sorry, Error processing your request</h1>
      <p>This may be due to bad connection or Invalid request</p>
    </section>
  </div>
</template>
<style scoped>
section{
  width: 100%;
  padding: 50px;
  text-align: center;
  height: 400px;
}
h1{
  font-weight: 600;
  font-size: 50px;
}
p{
  font-size: 24px;
}
</style>