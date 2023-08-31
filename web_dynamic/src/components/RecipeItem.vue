<script setup>
const props = defineProps({
    imageSrc: String,
    recipeTitle: String,
    missed: Number,
    used: Number
})
</script>

<template>
    <section class="recipe-item">
        <img :src="props.imageSrc" alt="#">
        <div class="recipe-summary">
            <h3>{{ props.recipeTitle }}</h3>
            <!-- <div class="likes"></div> -->
            <p class="summary">Missed Ingredients: {{ props.missed }}</p>
            <p class="summary">Used Ingredients: {{ props.used }}</p>
        </div>
    </section>
</template>

<style scoped>
section.recipe-item{
    background-color: white;
    width: 100%;
    height: 250px;
    display: grid;
    grid-template-rows: 1fr;
    grid-template-columns: 1fr 1fr;
    padding: 20px;
}
section.recipe-item img{
    width: 90%;
    height: 90%;
    margin: auto;
}
div.recipe-summary{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}
</style>