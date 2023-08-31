<script setup>
import Navbar from '../components/Navbar.vue';
</script>

<template>
  <Navbar :showsearch="true" />

  <main>
    <div class="recipe-container">
      <div class="recipe_image">
      <img class="recipe-image" src="../assets/images/Rectangle 30.png" alt="recipe">
      </div>
      <div class="recipe-summary">
        <h1 class="recipe-title"></h1>
        <p></p>
      </div>
      <div class="box"></div>
      <div class="savedrecipebox"></div>
    </div>
  </main>
</template>

<style scoped>
div.recipe-container{
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    text-align: center;
    justify-content: center;
    align-items: center;
    padding: 0px 20px;
    margin: 0px 20px;
}

div.recipe_image{
margin-top: 10px;
}

div.recipe_image .recipe-image {
    width: 100%;
    height: auto;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

header{
    width: 100%;
    /* margin-inline: 20px; */
}
</style>
