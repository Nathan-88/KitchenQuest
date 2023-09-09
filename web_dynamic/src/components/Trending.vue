<script setup>
import { ref } from 'vue';
import axios from 'axios'
import { moreDetails, getRecipe, defaultParams } from '@/utilities'
import { useRecipeStore } from '@/stores';
import { storeToRefs } from 'pinia';

// Initializing the store and reactive state
const store = useRecipeStore()
const { trending } = storeToRefs(store)

// getting and updating the params
const params = {...defaultParams}
params.number = 5

// Removing tags from summary
const fixSummary = (summary) => {
    let finalSummary = summary.replace(/<\/?[^>]+(>|$)/g, "")
    return finalSummary
}

// Fetching and updating the state based on a condition
if (trending.value === null) {
    axios({
        url: import.meta.env.VITE_SPOONACULAR_BASE_URL,
        params: params,
    }).then((response) => {
        store.trending = response.data['results']
    }).catch((error) => console.error(error))
}

// watching for updates and storing 
store.$subscribe((mutation, state) => {
    sessionStorage.setItem('trending', JSON.stringify(state.trending))
})
</script>

<template>
  <section class="trending">
        <h2 @click="() => getRecipe('trending')">Trending</h2>
        <section class="trending-list">
            <div v-for="recipe in trending" class="trending-recipe" @click="() => moreDetails(recipe)">
                <img :src="recipe.image" :alt="recipe.title">
                <div class="recipe-content">
                    <h3>{{ recipe.title }}</h3>
                    <p>{{ fixSummary(recipe.summary) }}</p>
                </div>
            </div>
        </section>
    </section>
</template>

<style scoped>
section.trending{
    width: 100%;
    min-height: 380px;
    display: grid;
    grid-template-rows: 70px 1fr;
    grid-template-columns: 1fr;
    row-gap: 30px;
    cursor: pointer;
}
section.trending-list{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    grid-template-rows: auto;
    row-gap: 80px;
    width: 100%;
    min-height: 350px;
    margin-bottom: 30px;
}
section.trending .trending-recipe{
    width: 90%;
    height: 250px;
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
@media(max-width: 400px){
    section.trending .trending-recipe{
        width: 65%;
    }
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
    top: -100px;
    border-radius: 50%;
    box-shadow: 10px 15px 20px -10px rgba(0, 0, 0, 0.5);
    object-fit: cover;
}
div.trending-recipe h3{
    font-size: 13px;
    font-weight: 700;
}
div.trending-recipe p{
    font-size: 10px;
    width: 80%;
    margin: auto;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: 4;
    display: -webkit-box;
    -webkit-box-orient: vertical;
}
</style>