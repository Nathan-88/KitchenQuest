<script setup>
import Navbar from '@/components/Navbar.vue';
import { useRecipeStore } from '@/stores';

const store = useRecipeStore()
const getAllNames = (dataArr) => {
  const names = []
  for (let data of dataArr){
    names.push(data.name)
  }
  return names
}
const recipe = store.recipeDetails
console.log(recipe.analyzedInstructions[0].steps)
for (let step of recipe.analyzedInstructions[0].steps) {
  console.log(`step ${step.number}: ${step.step}`)
  const ingredients = getAllNames(step.ingredients)
  const allIngredients = ingredients.join(', ')
  console.log('\t\tIngredients:', allIngredients)
  const equipments = getAllNames(step?.equipment)
  if (equipments.length > 0) console.log('\t\tEquipments:', equipments.join(', '))
  if (step?.length) console.log(`\t\ttime: ${step.length.number} ${step.length.unit}`)
}
</script>

<template>
  <div>
    <Navbar :showsearch="true" />
  
    <main>
      <div class="recipe-container">
        <div class="recipe_image">
          <img class="image" :src="recipe.image" alt="recipe">
        </div>
        <div class="recipe-summary">
          <div class="recipe_title">
            <div class="redbox"></div>
            <h1 class="recipe-title">{{ recipe.title }}</h1>
          </div>
          <div class="nutrients-box">
            <span><b>Nutients: </b></span>
            <span class="span" v-for="nutrient in recipe.nutrition.nutrients" :key="nutrient.name">
            <em>{{ nutrient.name }};  </em>
            </span>
          </div>
  
          <div class="blackborder">
            <div class="white-background"><b>Serving: {{ recipe.servings }}</b></div>
            <div class="white-background"><b>Prep: {{ recipe.readyInMinutes }}minutes</b></div>
            <div class="white-background"><b>Source: <a :href="recipe.sourceUrl">{{ recipe.sourceName }}</a></b></div>
          </div> 
        </div>
        <div class="sharesection">
          <div class=share>
            <img src='@/assets/images/bi_save.svg'>
            <p>Save Recipe</p>
          </div>
          <div class='media-container'>
            <img class="media" src="@/assets/images/whatsapp.svg" alt="Whatsapp"/>
            <img class="media" src="@/assets/images/twitter.svg" alt="twitter"/>
            <img class="media" src="@/assets/images/instagram.svg" alt="instagram"/>
          </div>
  
        </div>
      </div>
      <hr>
      <span id="ingredients"><b>Ingredients: </b></span>
      <span class="span" v-for="ingredient in recipe.nutrition.ingredients" :key="ingredient.id">
        <em>{{ ingredient.name }};  </em>
      </span><br><br>

      <!-- Inline styling here, so take note and remove it -->
      <div id="instructions"><b>Instructions: </b></div>
      <div class="step" v-for="instruction in recipe.analyzedInstructions[0].steps" :key="instruction.id" style="margin: 15px 0;">
        <div style="display: flex; gap: 10px;">
          <span><b>Step {{ instruction.number }}:</b></span>
          <span style="width: 80%;">{{ instruction.step }}</span>
        </div>
        <div id="ingredient" style="margin-inline-start: 60px;" v-if="instruction.ingredients.length > 0">
          <b id="ingredient">Ingredients: </b>
          <span><em>{{ getAllNames(instruction.ingredients).join(', ') }}</em></span>
        </div>
        <div style="margin-inline-start: 60px;" v-if="instruction.equipment.length > 0">
          <b id="ingredient">Equipment{{ instruction.equipment.length > 1 ? 's' : '' }}: </b>
          <span><em>{{ getAllNames(instruction.equipment).join(', ') }}</em></span>
        </div>
        <div style="margin-inline-start: 60px;" v-if="instruction.length">
          <b>Time: </b>
          <span><em>{{ instruction.length.number }} minute{{ instruction.length.number > 1 ? 's' : '' }}</em></span>
        </div>
      </div>

    </main>
  </div>
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
  width: 100%;
  max-width: 100%;
  overflow: hidden;
  position: relative;
  border-radius: 15px;
  background-color: #261A5A;
}

div.recipe_image .image {
    width: 30%;
    height: auto;
    display: center;
    max-width: 100%;
    background-position: center;
    background-repeat: repeat;
    border-radius: 15px;
    /*object-fit: cover;*/
    margin-bottom: 10px;
    margin-top: 15px;
}
div.recipe-summary{
  /* display: inline-block; */
  width: 100%;
  margin:10px;

  text-align: center;
}
div.recipe-summary .recipe_title{
  display: flex;
  justify-content:flex-start;
  align-items: center;
  color: #261A5A;
}
div.recipe-summary .recipe_title .redbox{
  background: var(--red-color);
  width: 10px;
  height: 40px;
  flex-shrink: 0;
  margin-right: 10px;
}
div.recipe-summary .nutrients-box{
  width: 100%;
}

span.span{
  padding-inline: 3px;
}
div.recipe-summary .blackborder{
  border: 2px;
  border-style: ridge;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 15px;
  max-width: 100%;
  margin: auto;
  margin-top: 10px;
  border-radius: 5px;
}
div.recipe-summary .blackborder .white-background{
  background: #FFFFFFB2;
  padding: 15px;
  word-spacing:1em;
}

div.sharesection{
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin-top: 20px;
  margin-bottom: 20px;
  padding-top: 10px ;
}

div.sharesection .share{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 15px;
  border-radius: 5px;
  margin-right:20px;
  background: var(--red-color);
}

div.sharesection .share img{
  max-width: 2.5rem;
  height: auto;
  margin-right: 1.5rem;
}
div.sharesection .share p{
  color: white;
  font-size: 1.5rem;
  font-weight: 500;
}

div.sharesection .media-container{
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin-left: 20px;
}

div.sharesection .media-container .media{
  width: 2.5rem;
  height: 2.5rem;
  margin-right: 1.5rem;
}

div.sharesection .media-container .media:hover{
  cursor: pointer;
}
div.sharesection .media-container .media:active{
  transform: scale(0.9);
}
div.sharesection .media-container .media:focus{
  outline: none;
}
span#ingredients {
  font-size: 25px;
  color: #FFF;
  background-color: #FD043C;
  border-radius: 15px;
  padding-left: 10px;
  margin-left: 10px;
  text-align: 5px;
  width: 185px;
  display: inline-block;
  margin-top: 20px;
}
span.span {
  font-size: 20px;
}
div#instructions {
  font-size: 25px;
  color: #FFF;
  background-color: #FD043C;
  border-radius: 15px;
  padding-left: 10px;
  margin-left: 10px;
  /*display: inline-block;*/
  width: 185px;
}
div.step div{
  margin-left: 100px;
  font-size: 18px;
}
div b#ingredient {
  margin-left: 150px;
  font-size: 18px;
}
</style>
