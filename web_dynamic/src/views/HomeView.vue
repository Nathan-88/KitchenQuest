<script setup>
import Navbar from '@/components/Navbar.vue'
import Explore from '@/components/Explore.vue';
import Trending from '@/components/Trending.vue';
import Diet from '@/components/Diet.vue';
import { ref } from 'vue';
import { getRecipe } from '@/utilities';

const searchText = ref("")

</script>

<template>
    <!-- Ignore the div, for animation -->
  <div>
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
            <input v-model="searchText" @keypress.enter.prevent="() => getRecipe(searchText)" name="recipe_search" id="recipe-search" placeholder="Search for Recipes">
            <button @click="() => getRecipe(searchText)" type="submit">Go</button>
          </div>
        </section>
        <section class="red_box"></section>
        <div class="dots"></div>
        <img src="@/assets/images/Rectangle2.png" alt="food" class="food-image">
      </header>
      <main>
        <!-- Random Section -->
        <section class="random">
          <div class="quote">
            <span class="red-bar"></span>
            <p>Welcome to KitchenQuest - Your Culinary Companion</p>
          </div>
          <div class="quote-two">
            <h3>Our Mission</h3>
            <p>Our mission is simple: to help you create memorable meals effortlessly. With KitchenQuest, you'll discover new recipes, make the most of the ingredients you have, and savor the joy of cooking.</p>
          </div>
        </section>
        <!-- Diet Recipe Section -->
        <Diet />
        <!-- Trending Section -->
        <Trending />
        <!-- Explore Section -->
        <Explore />
      </main>
  </div>
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
    position: relative;
    grid-column: 1/7;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}
@media(max-width: 799px){
    .nav-container::before{
        position: absolute;
        content: "";
        background-color: red;
        width: 45%;
        height: 100%;
        top: 0px;
        right: 0px;
        z-index: -1;
        opacity: 0.7;
    }
}


.shadow_heading{
    color: #EBE6E6;
    font-family: Poppins;
    font-size: 85px;
    font-style: normal;
    font-weight: 600;
    line-height: 160%; /* 320px */
    display: flex;
    width: 100%;
    height: 150px;
    flex-direction: column;
    justify-content: center;
    flex-shrink: 0;
    padding: 10px;
}
.hero-text-container {
    color: var(--blue-theme-color);
    font-family: var(--primary-font);
    font-size: 35px;
    font-style: normal;
    font-weight: 700;
    line-height: 90%;
    letter-spacing: -2.1px;
    width: 80%;
    margin-left: 70px;
    position: relative;
    top: -50px;
}
.hero-text:nth-child(4){
    top: -120px;
}
.hero-text:nth-child(5) {
    top: -150px;
}
.red_box,
div.dots,
img.food-image{
    display: none;
}
div.search {
    background-color: white;
    margin-left: 20px;
    height: 50px;
    width: 300px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    box-shadow: 0px 15px 40px 0px rgba(0, 0, 0, 0.10);
    /* positioning it using its base position, which is down */
    position: relative;
    top: 0px;
}

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
    background: var(--blue-theme-color);
    cursor: pointer;
    outline: none;
    border: none;
    color: white;
    font-size: 20px;
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
    margin-top: 40px;
    row-gap: 40px;
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
    box-shadow: 5px 10px 5px -10px rgba(0,0,0,0.2);
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
    text-align: center;
    margin: auto;
}
section.random div.quote-two{
    /* grid-column: 2/3; */
    width: 100%;
    justify-self: end;
    display: flex;
    flex-direction: column;
    text-align: center;
    /* padding-left: 100px; */
}
div.quote-two h3{
    color: var(--blue-theme-color);
    font-weight: 600;
    font-size: 30px;
    font-style: normal;
    letter-spacing: -2.1px;
}
div.quote-two p{
    max-width: 100%;
    color: var(--hash-color);
    align-self: flex-end;
    font-weight: 400;
}

@media(min-width: 600px) and (max-width: 799px){
    /* div.dots {
        display: block;
        width: 100%;
        background-image: url('../assets/images/Vector.svg');
        background-repeat: repeat;
        background-size: 34px;
        width: 300px;
        height: 75%;
        position: absolute;
        right: 1.5vw;
        top: 55%;
        background-color: transparent;
    } */
    img.food-image {
        display: block;
        position: absolute;
        top: 55%;
        right: 1.5vw;
        height: 300px;
        width: 300px;
    }
    div.search button{ background: var(--red-color) }
}

/* Laptop screen style */
@media(min-width: 800px) {

    .nav-container {
        grid-column: 1/5;
        /* width: 100%; */
        /* height: 100%; */
        /* display: flex; */
        /* flex-direction: column; */
        /* justify-content: flex-start; */
    }


    .shadow_heading{
        /* color: #EBE6E6; */
        /* font-family: Poppins; */
        font-size: 120px;
        /* font-style: normal; */
        font-weight: 600;
        /* line-height: 160%; */
        /* display: flex; */
        /* width: 100%; */
        /* height: 150px; */
        /* flex-direction: column; */
        /* justify-content: center; */
        /* flex-shrink: 0; */
        padding: 30px;
    }
    .red_box{
        display: block;
        grid-column: 5/7;
        width: 100%;
        height: 600px;
        background-color: var(--red-color);
        flex-shrink: 0;
    }
    div.dots {
        display: block;
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
    img.food-image {
        display: block;
        position: absolute;
        top: 20%;
        right: 12%;
        height: 500px;
        width: 500px;
    }
    div.search {
        /* background-color: white; */
        margin-left: 100px;
        /* height: 50px; */
        /* width: 350px; */
        /* display: grid; */
        /* grid-template-columns: repeat(3, 1fr); */
        /* box-shadow: 0px 15px 40px 0px rgba(0, 0, 0, 0.10); */
        /* positioning it using its base position, which is down */
        /* position: relative; */
        /* top: 0px; */
    }
    div.search button{
        background: var(--red-color);
    }
    /* Random Section */
    section.random{
        min-height: 90px;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        grid-template-rows: auto;
        margin-top: 20px;
        row-gap: 20px;
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
        box-shadow: none;
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
        text-align: left;
        margin: 0;
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
        max-width: 51ch;
        color: var(--hash-color);
        text-align: right;
        align-self: flex-end;
        font-weight: 400;
    }
}
/* Recipe Section */

/* Trending Section */

/* Explore Section */

</style>
