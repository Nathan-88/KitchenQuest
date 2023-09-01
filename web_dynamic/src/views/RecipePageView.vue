<script setup>
import Navbar from '../components/Navbar.vue';

const props = defineProps({
  recipe: String
})
const recipe = JSON.parse(props.recipe)
console.log(recipe)
</script>

<template>
  <Navbar :showsearch="true" />

  <main>
    <div class="recipe-container">
      <div class="recipe_image">
        <img class="image" :src="recipe.image" alt="recipe">
      </div>
      <div class="recipe-summary">
        <h1 class="recipe-title">{{ recipe.title }}</h1>
        <span><b>Nutients: </b></span>
        <span class="span" v-for="nutrient in recipe.nutrition.nutrients" :key="nutrient.name">
          <em>{{ nutrient.name }};  </em>
        </span> <br><br>
        <span><b>Ingredients: </b></span>
        <span class="span" v-for="ingredient in recipe.nutrition.ingredients" :key="ingredient.id">
          <em>{{ ingredient.name }};  </em>
        </span><br><br>
        <span><b>Serving: </b></span><span>{{ recipe.servings }}</span><br><br>
        <span><b>Preparation Time: </b></span><span>{{ recipe.readyInMinutes }}minutes</span><br><br>
        <span><b>Source: </b></span><a :href="recipe.sourceUrl">{{ recipe.sourceName }}</a>
        
      </div>
      <div class="box"></div>
      <div class="savedrecipebox"></div>
    </div>
  </main>
</template>

<style scoped>
div.recipe-container{
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    text-align: center;
    justify-content: center;
    align-items: center;
    padding: 0px 20px;
    margin: 0px 20px;
}

div.recipe_image{
  margin-top: 10px;
  width: 600px;
  float: right;
}

div.recipe_image .image {
    width: 100%;
    height: auto;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
div.recipe-summary{
  /* display: inline-block; */
  width: 600px;
  margin: auto;
  text-align: left;
}
span.span{
  padding-inline: 5px;
}
</style>
