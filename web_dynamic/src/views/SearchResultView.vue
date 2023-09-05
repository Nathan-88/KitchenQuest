<script setup>
import axios from 'axios'
import RecipeItem from '../components/RecipeItem.vue';
import Navbar from '../components/Navbar.vue';
import { defaultParams, moreDetails } from '../utilities';
import router from '../router/index'
import { ref, onMounted, watch } from 'vue';

// The ingredient props name should be changed to something more generic
// because we are about to use it for cuisines too
const props = defineProps({
    recipe: String
});

const recipes = ref(null)
const loading = ref(true)

const fetchRecipe = (ingredient) => {
    // create a default params object
    const params = {...defaultParams}
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
        url: import.meta.env.VITE_SPOONACULAR_BASE_URL,
        params: params
    }).then((response) =>  {
        recipes.value = response.data['results']
        loading.value = false
    })
    .catch((error) => console.error(error))
}
// component lifecycle
onMounted(() => fetchRecipe(props.recipe))
watch(() => props.recipe, (ingredient) => fetchRecipe(ingredient))

</script>

<template>
    <div>
        <Navbar :showsearch="true"/>
        <main>
            <h1>Results for {{ props.recipe }}</h1>
            <section class="container">
                <RecipeItem v-if="!loading" v-for="recipe in recipes"
                            :recipeTitle="recipe.title"
                            :imageSrc="recipe.image"
                            :summary="recipe.summary"
                            :key="recipe.title"
                            @click="() => moreDetails(recipe)"
                />
                <section v-else v-for="n in 10" :key="n" class="loading"></section>
            </section>
        </main>
    </div>
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
section.loading{
    width: 100%;
    height: 250px;
    background-color: lightgrey;
    border-radius: 20px;
}
</style>