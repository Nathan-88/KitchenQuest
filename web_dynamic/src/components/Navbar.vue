<script setup>
import { RouterLink } from 'vue-router';
const props = defineProps({
  showsearch: Boolean
})
</script>

<template>
  <nav class="navbar">
      <a href="/"><img class="logo" src="/static/images/Logo.svg" alt="kitchen Quest"></a>
      <ul>
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/about">About</RouterLink></li>
        <li><RouterLink to="#trending">Trending</RouterLink></li>
        <li><RouterLink to="/saved_recipes">Favourites</RouterLink></li>
      </ul>
      <div v-if="props.showsearch" class="nav-search">
          <input type="text" name="nav_search" id="nav-search" placeholder="Search for Recipes">
          <button type="submit"><img class="icon" src="/static/images/search.svg" alt="search"></button>
      </div>
  </nav>
</template>