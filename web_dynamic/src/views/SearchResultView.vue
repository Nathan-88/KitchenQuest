<script setup>
import RecipeItem from '@/components/RecipeItem.vue';
import Navbar from '@/components/Navbar.vue';
import { moreDetails } from '@/utilities';
import { ref } from 'vue';
import { storeToRefs } from 'pinia'
import { useRecipeStore } from '@/stores';

const props = defineProps({
    recipe: String
});

let store = useRecipeStore()
const loading = ref(true)
const { recipes } = storeToRefs(store)
if (recipes.value !== null) loading.value = false

store.$subscribe((mutation, state) => {
    localStorage.setItem('recipes', JSON.stringify(state.recipes))
    localStorage.setItem('recipeDetails', JSON.stringify(state.recipeDetails))
})
</script>

<template>
    <div>
        <Navbar :showsearch="true"/>
        <main>
            <h1>Results for {{ props.recipe }}</h1>
            <section class="container">
                <!-- Conditional rendering, this one or the other -->
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
    width: 95%;
    margin: auto;
    height: 250px;
    background-color: lightgrey;
    border-radius: 20px;
    animation: 0.5s infinite alternate loading;
}
@keyframes loading {
    from{
        width: 99.5%;
        height: 249px;
        background-color: rgb(241, 233, 233);
    }
    to{
        width: 100%;
        background-color: rgb(224, 218, 218);
        height: 250px;
    }
}
</style>