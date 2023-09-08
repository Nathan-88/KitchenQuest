<script setup>
import { RouterLink } from 'vue-router';
import { getRecipe } from '@/utilities';
import { ref } from 'vue';


const props = defineProps({
  showsearch: Boolean
})

const searchText = ref("")
const display = ref({
    menu: false,
    search: false
})

const displayItem = show => display.value[show] = !display.value[show]

</script>

<template>
  <nav class="navbar">
      <a href="/"><img class="logo" src="@/assets/images/Logo.svg" alt="kitchen Quest"></a>
      <ul :class="{'active': display.menu}" class="menu-list">
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/about">About</RouterLink></li>
        <li @click="() => getRecipe('trending')">Trending</li>
        <li><RouterLink to="/saved_recipes">Favourites</RouterLink></li>
      </ul>
      <span v-if="props.showsearch" @click="() => displayItem('search')" class="search-mobile">Search</span>
      <div :class="{'active': display.search}" v-if="props.showsearch" class="nav-search">
          <input v-model="searchText" @keypress.enter.prevent="() => getRecipe(searchText)" type="text" name="nav_search" id="nav-search" placeholder="Search for Recipes">
          <button @click="() => { displayItem('search'); getRecipe(searchText) }" type="submit"><img class="icon" src="@/assets/images/search.svg" alt="search"></button>
      </div>
      <img @click="() => displayItem('menu')" src="@/assets/images/Hamburger_icon.png" alt="" class="menu">
  </nav>
</template>

<style scoped>
#navbar{
    width: 100%;
}

.navbar {
    display: flex;
    /* grid-template-columns: repeat(3, 1fr);; */
    justify-content: space-between;
    align-items: center;
    flex-direction: row;
    background-color: var(--background-color);
    max-width: 100%;
    cursor: pointer;
    height: 55px;
}
.navbar img.logo {
    margin-top: 2px; /* added a margin */
    width: 100px;
    height: 50px;
    padding-left: 10px;
}
@media(max-width: 799px){
    .navbar ul {
        list-style: none;
        display: flex;
        flex-direction: column;
        width: 100%;
        justify-content: space-around;
        align-items: center;
        gap: 10px;
        font-family: Poppins;
        font-size: 17px;
        font-style: normal;
        font-weight: 600;
        position: absolute;
        top: 54px;
        right: 0px;
        background-color: var(--background-color);
        z-index: 1;
        padding: 20px 0;
        box-shadow: 0px 8px 4px 0px rgba(0,0,0,0.2);
        visibility: hidden;
    }
}
.navbar a{
    color: var(--grayscale-50);
    text-decoration: none;
}

img.menu{
    width: 50px;
    height: 50px;
}
.active.menu-list{
    visibility: visible;
}
.active.nav-search{
    visibility: visible;
}
.search-mobile{
    margin: auto;
    font-family: Poppins;
    font-size: 24px;
    font-style: normal;
    font-weight: 600;
}
.nav-search{
    height: 40px;
    width: 100%;
    display: flex;
    background: var(--white);
    box-shadow: 0px 5px 8px 0px rgba(0, 0, 0, 0.10);
    /* border-radius: 5px; */
    background-color: white;
    margin-inline: 0;
    position: absolute;
    top: 55px;
    visibility: hidden;
    z-index: 1;
}
.nav-search input{
    border: none;
    outline: none;
    width: 80%;
    height: 100%;
    /* font-size: 1.2rem; */
    /* font-style: normal; */
    /* font-weight: 400; */
    padding: 0 15px;
    border-radius: 5px;
}
.nav-search button{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 20%;
    height: 100%;
    line-height: 40px;
    text-align: center;
    background: var(--red-color);
    /* border-radius: 50px 4px 4px 4px; */
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

@media(min-width: 800px){
    .navbar {
        display: flex;
        /* grid-template-columns: repeat(3, 1fr);; */
        justify-content: space-around;
        align-items: center;
        /* gap: 30px; */
        flex-direction: row;
        margin: 10px 0px 0px 50px;
        max-width: 100%;
        cursor: pointer;
        /* grid-row: 1/2; */
    }
    .navbar img.logo {
        margin-top: 5px; /* added a margin */
        grid-column: 1/2;
        width: 150px;
        height: 50px;
    }
    .navbar ul {
        /* grid-column: 2/5; */
        list-style: none;
        display: flex;
        flex-direction: row;
        max-width: 100%;
        justify-content: space-around;
        align-items: center;
        gap: 50px;
        font-family: Poppins;
        font-size: 24px;
        font-style: normal;
        font-weight: 600;
        position: relative;
        background-color: none;
        /* line-height: 140%; 33.6px */
    }
    .navbar a{
        color: var(--grayscale-50);
        text-decoration: none;
    }
    img.menu{
        display: none;
    }
    span.search-mobile{
        display: none;
    }
    .nav-search{
        height: 35px;
        width: 300px;
        display: flex;
        background: var(--white);
        /*box-shadow: 0px 15px 40px 0px rgba(0, 0, 0, 0.10);*/
        box-shadow: 0px 5px 8px 0px rgba(0, 0, 0, 0.10);
        border-radius: 5px;
        background-color: white;
        position: static;
        visibility: visible;
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
}
</style>
