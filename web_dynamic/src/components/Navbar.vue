<script setup>
import { RouterLink } from 'vue-router';
import router from '../router/index'
import { ref } from 'vue';


const props = defineProps({
  showsearch: Boolean
})

const searchText = ref("")
const getRecipe = () => {
    router.push({name: 'search', params: { ingredient: searchText.value }})
}
</script>

<template>
  <nav class="navbar">
      <a href="/"><img class="logo" src="../assets/images/Logo.svg" alt="kitchen Quest"></a>
      <ul>
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/about">About</RouterLink></li>
        <li><RouterLink to="#trending">Trending</RouterLink></li>
        <li><RouterLink to="/saved_recipes">Favourites</RouterLink></li>
      </ul>
      <div v-if="props.showsearch" class="nav-search">
          <input v-model="searchText" @keypress.enter.prevent="getRecipe" type="text" name="nav_search" id="nav-search" placeholder="Search for Recipes">
          <button @click="getRecipe" type="submit"><img class="icon" src="../assets/images/search.svg" alt="search"></button>
      </div>
  </nav>
</template>

<style>
#navbar{
    width: 100%;
}
.navbar {
    display: flex;
    /* grid-template-columns: repeat(3, 1fr); */
    justify-content: space-around;
    align-items: center;
    /* gap: 30px; */
    flex-direction: row;
    margin: 10px 0px 0px 50px;
    max-width: 100%;
    /* grid-row: 1/2; */
}
.navbar img.logo {
    grid-column: 1/2;
    width: 150px;
    height: 50px;
}
.navbar ul {
    /* grid-column: 2/5; */
    list-style: none;
    display: flex;
    max-width: 100%;
    justify-content: space-around;
    align-items: center;
    gap: 50px;
    font-family: Poppins;
    font-size: 24px;
    font-style: normal;
    font-weight: 600;
    /* line-height: 140%; 33.6px */
}
.navbar a{
    color: var(--grayscale-50);
    text-decoration: none;
}
.nav-search{
    height: 35px;
    width: 300px;
    display: flex;
    background: var(--white);
    box-shadow: 0px 15px 40px 0px rgba(0, 0, 0, 0.10);
    border-radius: 5px;
    background-color: white;
}

.nav-search input{
    border: none;
    outline: none;
    width: 75%;
    height: 100%;
    font-size: 1.2rem;
    font-style: normal;
    font-weight: 400;
    padding: 0 15px;
    border-radius: 5px;
}

.nav-search button{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 25%;
    height: 100%;
    line-height: 40px;
    text-align: center;
    background: var(--red-color);
    border-radius: 200px 4px 4px 4px;
    border-style: none;
    cursor: pointer;
    outline: none;
}

.nav-search img.icon{
    width: 30px;
    height: 30px;
    padding-left: 3px;
    color: var(--white);
}
</style>