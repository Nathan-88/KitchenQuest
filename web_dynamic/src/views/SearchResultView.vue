<script setup>
import axios from 'axios'
import RecipeItem from '../components/RecipeItem.vue';
import Navbar from '../components/Navbar.vue';
import router from '../router/index'
import { ref, onMounted, watch } from 'vue';

// The ingredient props name should be changed to something more generic
// because we are about to use it for cuisines too
const props = defineProps({
    recipe: String
});

const recipes = ref(null)

const fetchRecipe = (ingredient) => {
    // create a default params object
    const params = {
        apiKey: import.meta.env.VITE_SPOONACULAR_API_KEY,
        instructionsRequired: true,
        sort: 'random',
        addRecipeInformation: true,
        addRecipeNutrition: true,
        sortDirection: 'asc',
        number: 10
    }
    // conditionally set the optional params for the api
    if (ingredient.includes('cuisine')) {
        const cuisine = ingredient.replace("cuisine", "")
        params.cuisine = cuisine
    } else if (ingredient.includes('diet')) {
        const diet = ingredient.replace("diet", "")
        params.diet = diet
    } else if (!ingredient.includes('trending')){
        params.includeIngredients = ingredient
    }

    axios({
        url: import.meta.env.VITE_BASE_URL,
        params: params
    }).then((response) =>  {
        recipes.value = response.data['results']
        console.log('state:', recipes.value)
    })
    .catch((error) => console.error(error))
}
// component lifecycle
onMounted(() => fetchRecipe(props.recipe))
watch(() => props.recipe, (ingredient) => fetchRecipe(ingredient))

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
        <h1>Results for {{ props.recipe }}</h1>
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

<style scoped>
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