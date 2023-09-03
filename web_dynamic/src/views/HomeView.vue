<script setup>
import Navbar from '../components/Navbar.vue'
import Explore from '../components/Explore.vue';
import Trending from '../components/Trending.vue';
import Diet from '../components/Diet.vue';
import { ref } from 'vue';
import router from '../router/index'


const searchText = ref("")
const getRecipe = () => {
    router.push({name: 'search', params: { ingredient: searchText.value }})
}
</script>

<template>
  <!-- Hero Section -->
  <header>
    <section class="nav-container">
      <div id="navbar-container">
        <Navbar />
      </div>
      <h1 class="shadow_heading">request</h1>
      <div class="hero-text-container">
        <p class="hero-text">Discover Recipes for</p>
        <p class="hero-text">Delicious Foods around</p>
        <p class="hero-text">the World</p>
      </div>
      <div class="search">
        <input v-model="searchText" @keypress.enter.prevent="getRecipe" name="recipe_search" id="recipe-search" placeholder="Search for Recipes">
        <button @click="getRecipe" type="submit">Go</button>
      </div>
    </section>
    <section class="red_box"></section>
    <div class="dots"></div>
    <img src="../assets/images/Rectangle 2.png" alt="food" class="food-image">
  </header>
  <main>
    <!-- Random Section -->
    <section class="random">
      <div class="quote">
        <span class="red-bar"></span>
        <p>The internet famous always pan just got a huge update</p>
      </div>
      <div class="quote-two">
        <h3>the world</h3>
        <p>people find themselves with a collection of ingredients but lack the inspiration to create a meal. KitchenQuest will bridge that gap by suggesting recipes that can be prepared using the ingredients the user already has</p>
      </div>
    </section>
    <!-- Diet Recipe Section -->
    <Diet />
    <!-- Trending Section -->
    <Trending />
    <!-- Explore Section -->
    <Explore />
  </main>
</template>

<style scoped>

header {
    width: 100%;
    display: flex;
    flex-direction: row;
    height: 600px;
    display: grid;
    grid-template-columns: repeat(6, 1fr);
}
.nav-container {
    grid-column: 1/5;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.red_box{
    grid-column: 5/7;
    width: 100%;
    height: 600px;
    background-color: var(--red-color);
    flex-shrink: 0;
}
.shadow_heading{
    color: #EBE6E6;
    font-family: Poppins;
    font-size: 120px;
    font-style: normal;
    font-weight: 600;
    line-height: 160%; /* 320px */
    display: flex;
    width: 100%;
    height: 150px;
    flex-direction: column;
    justify-content: center;
    flex-shrink: 0;
    padding: 30px;
}
.hero-text-container {
    color: var(--blue-theme-color);
    font-family: var(--primary-font);
    font-size: 50px;
    font-style: normal;
    font-weight: 700;
    line-height: 90%;
    letter-spacing: -4.1px;
    width: 80%;
    margin-left: 100px;
    position: relative;
    top: -40px;
}
.hero-text:nth-child(4){
    top: -120px;
}
.hero-text:nth-child(5) {
    top: -150px;
}
div.dots {
    width: 100%;
    background-image: url('../assets/images/Vector.svg');
    background-repeat: repeat;
    background-size: 34px;
    width: 350px;
    height: 75%;
    position: absolute;
    right: 20%;
    top: 20%;
    background-color: transparent;
}
.food-image {
    position: absolute;
    top: 20%;
    right: 12%;
    height: 500px;
    width: 500px;
}
div.search {
    background-color: white;
    margin-left: 100px;
    height: 50px;
    width: 350px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    box-shadow: 0px 15px 40px 0px rgba(0, 0, 0, 0.10);
    /* positioning it using its base position, which is down */
    position: relative;
    top: 0px;
}
/* div.search:has(input:focus-visible){
    border-width: 1px;
} */

div.search input{
    height: 100%;
    border-width: 0;
    outline: none;
    font-size: 18px ;
}
div.search input{
    grid-column: 1/3;
    padding-inline: 10px;
}
div.search input::placeholder{
    color: rgb(221, 211, 211);
}
div.search input[type=text]:focus-visible {
    outline-width: 0;
}
div.search button{
    grid-column: 3/4;
    border-radius: 200px 4px 4px 4px;
    background: var(--red-color);
    cursor: pointer;
    outline: none;
    border: none;
}

/* MAin Content */
main {
    padding-inline: 5px;
    min-width: 80%;
}
@media(min-width: 500px) {
    main {
        padding-inline: 30px;
    }
}

/* Random Section */
section.random{
    min-height: 90px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    grid-template-rows: auto;
    margin-top: 20px;
}
section.random div.quote{
    /* background-color: green; */
    width: 100%;
    /* grid-column: 1/2; */
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    gap: 10px;
    align-self: center;
}
div.quote .red-bar{
    background: var(--red-color);
    display: inline-block;
    width: 10px;
    height: 45px;
    flex-shrink: 0;
}
div.quote p {
    width: 25ch;
    color: var(--blue-theme-color);
    font-weight: 600;
    letter-spacing: -1.1px;
    /* background-color: blue; */
}
section.random div.quote-two{
    /* grid-column: 2/3; */
    width: 100%;
    justify-self: end;
    display: flex;
    flex-direction: column;
    /* padding-left: 100px; */
}
div.quote-two h3{
    color: var(--blue-theme-color);
    font-weight: 600;
    text-align: right;
    font-size: 30px;
    font-style: normal;
    letter-spacing: -2.1px;
}
div.quote-two p{
    max-width: 43ch;
    color: var(--hash-color);
    text-align: right;
    align-self: flex-end;
    font-weight: 400;
}


/* Recipe Section */

/* Trending Section */
section.trending{
    width: 100%;
    min-height: 380px;
    display: grid;
    grid-template-rows: 70px 1fr;
    grid-template-columns: 1fr;
    row-gap: 30px;
}
section.trending-list{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    grid-template-rows: auto;
    row-gap: 50px;
    width: 100%;
    min-height: 350px;
    margin-bottom: 30px;
}
section.trending .trending-recipe{
    width: 70%;
    height: 240px;
    border-radius: 100px 0px 100px 0px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    position: relative;
    margin-top: 50px;
    margin-inline: auto;
}
.trending-recipe:nth-child(odd){
    background-color: white;
}
div.recipe-content{
    margin-top: 70px;
}
div.trending-recipe img{
    width: 200px;
    height: 200px;
    position: absolute;
    top: -80px;
}
div.trending-recipe h3{
    font-size: 15px;
    font-weight: 700;
}
div.trending-recipe p{
    font-size: 12px;
    width: 80%;
    margin: auto;
}
/* Explore Section */

</style>
