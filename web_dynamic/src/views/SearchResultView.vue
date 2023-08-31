<script setup>
import axios from 'axios'
import RecipeItem from '../components/RecipeItem.vue';
import Navbar from '../components/Navbar.vue';
import router from '../router/index'
import { ref, onMounted, watch } from 'vue';

const props = defineProps({
    ingredient: String
});
const recipes = ref(null)
const fetchRecipe = (ingredient) => {
    axios({
        url: 'https://api.spoonacular.com/recipes/complexSearch',
        params: {
            apiKey: import.meta.env.VITE_SPOONACULAR_API_KEY,
            includeIngredients: ingredient,
            instructionsRequired: true,
            sort: 'random',
            addRecipeInformation: true,
            addRecipeNutrition: true,
            sortDirection: 'asc',
            number: 10
        }
    }).then((response) =>  {
        recipes.value = response.data['results']
        console.log('state:', recipes.value)
    })
    .catch((error) => console.error(error))
}
onMounted(() => fetchRecipe(props.ingredient))
watch(() => props.ingredient, (ingredient) => fetchRecipe(ingredient))

// show more details about a recipe
// listen for a click event to trigger the route
const moreDetails = (recipeObj) => {
    const recipeJson = JSON.stringify(recipeObj)
    console.log(recipeObj);
    router.push({name: "RecipePage", params: {recipe: recipeJson}})
}
</script>

<template>
    <Navbar :showsearch="true"/>
    <main>
        <h1>Results for {{ props.ingredient }}</h1>
        <section class="container">
            <RecipeItem v-for="recipe in recipes"
                        :recipeTitle="recipe.title"
                        :imageSrc="recipe.image"
                        :summary="recipe.summary"
                        :key="recipe.title"
                        @click="() => moreDetails(recipe)"
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