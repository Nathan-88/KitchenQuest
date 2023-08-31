<script setup>
import axios from 'axios'
import RecipeItem from '../components/RecipeItem.vue';
import Navbar from '../components/Navbar.vue';
import { ref } from 'vue';

const props = defineProps({
    ingredient: String
});
const state = ref({
    recipes: []
})
axios({
    url: 'https://api.spoonacular.com/recipes/findByIngredients',
    params: {
        apiKey: import.meta.env.VITE_SPOONACULAR_API_KEY,
        ingredients: props.ingredient,
        number: 10
    }
}).then((response) =>  state.value.recipes = response.data )
.catch((error) => console.error(error))
</script>

<template>
    <Navbar :showsearch="true"/>
    <main>
        <h1>Results for {{ props.ingredient }}</h1>
        <section class="container">
            <RecipeItem v-for="recipe in state.recipes"
                        :recipeTitle="recipe.title"
                        :imageSrc="recipe.image"
                        :missed="recipe.missedIngredientCount"
                        :used="recipe.usedIngredientCount"
                        :key="recipe.title"
            />
        </section>
    </main>
</template>

<style>
h1{
    padding-inline-start: 20px;
    margin: 30px;
}
main{
    width: 100%;
    padding: 20px;
}
section.container{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
    row-gap: 20px;
    gap: 50px;
}
</style>