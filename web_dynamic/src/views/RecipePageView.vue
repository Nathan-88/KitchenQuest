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
          <div class= "recipe_title">
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
      <hr>

      <div class="ingre-instru-container">
        <div class="ingredients">
          <h2 class="ingre_h2">Ingredients</h2>
          <span class="span" v-for="ingredient in recipe.nutrition.ingredients" :key="ingredient.id">
            <em>{{ ingredient.name }};  </em>
          </span>
        </div>

        <!-- Inline styling here, so take note and remove it -->
        <div class="instruction">
          <h2>Instructions</h2>
          <div class="step" v-for="instruction in recipe.analyzedInstructions[0].steps" :key="instruction.id">
            <div style="display: flex; gap: 10px;">
              <span><b>Step {{ instruction.number }}:</b></span>
              <span style="width: 70%;">{{ instruction.step }}</span>
            </div>
            <div style="margin-inline-start: 60px;" v-if="instruction.ingredients.length > 0">
              <b>Ingredients: </b>
              <span><em>{{ getAllNames(instruction.ingredients).join(', ') }}</em></span>
            </div>
            <div style="margin-inline-start: 60px;" v-if="instruction.equipment.length > 0">
              <b>Equipment{{ instruction.equipment.length > 1 ? 's' : '' }}: </b>
              <span><em>{{ getAllNames(instruction.equipment).join(', ') }}</em></span>
            </div>
            <div style="margin-inline-start: 60px;" v-if="instruction.length">
              <b>Time: </b>
              <span><em>{{ instruction.length.number }} minute{{ instruction.length.number > 1 ? 's' : '' }}</em></span>
            </div>
          </div>
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
}

div.recipe_image .image {
    width: 800px;
    height: 340px;
    /* display: block; */
    max-width: 100%;
    background-position: center;
    background-repeat: repeat;
    border-radius: 15px;
    object-fit: cover;
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
  /* border-style: ridge; */
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
  background: floralwhite;
  padding: 15px;
  word-spacing:1em;
}

div.sharesection{
  display: flex;
  align-items: center;
  justify-content: center;
  max-width: 100%;
  margin-top: 10px;
  margin-bottom: 20px;
  padding-top: 10px ;
}

div.sharesection .share{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 15px;
  border-radius: 5px;
  /* margin-right:20px; */
  background: var(--red-color);
}

div.sharesection .share img{
  max-width: 1.5rem;
  height: auto;
  cursor: pointer;
  margin-right: 1.3rem;
}
div.sharesection .share p{
  color: white;
  font-size: 1.3rem;
  font-weight: 500;
}

div.sharesection .media-container{
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin-left: 1.5rem;
}

div.sharesection .media-container .media{
  width: 2.5rem;
  height: 2.5rem;
  margin-right: 1.5rem;
}

div.sharesection .media-container > img:last-child{
  margin-right: 1.7rem;
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

.ingre-instru-container{
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
  padding: 0px 20px;
  margin: 0px 20px;
}

div.ingredients{
  width: 100%;
  margin: 10px;
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 5px;
  background: floralwhite;
}

div.ingredients h2{
  font-size: 1.5rem;
  margin-bottom: 10px;
}

div.instruction{
  width: 100%;
  margin: 10px;
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 5px;
  background: floralwhite;
}

div.instruction h2{
  font-size: 1.5rem;
  margin-bottom: 10px;
}

div.instruction .step{
  margin-bottom: 10px;
}

div.instruction .step span{
  font-size: 1.2rem;
  font-weight: 500;
  line-height: 1.5;
}

div.instruction .step span em{
  font-size: 1.2rem;
  font-weight: 400;
}

div.instruction .step span b{
  font-size: 1.2rem;
}




@media (max-width: 767px) {
  /* Your styles for mobile view here */
  div.recipe-summary{
    margin: 0px;
  }
  div.recipe-summary .recipe_title{
    align-items: flex-start;
    margin-top: 5px;
  }
  div.recipe-summary .recipe_title h1{
    font-size: 1.5rem;
    margin-bottom: 5px;
    line-height: 1.5rem;

  }
  div.recipe-summary .blackborder{
    margin: 0px;
    margin-top: 10px;
    padding: 0px;
    border-style: none;
  }
  div.recipe-summary .blackborder .white-background{
    margin: 0px;
    border: floralwhite;
  }


  div.sharesection .share{
    padding: 10px;
    margin: 0px;
    margin-bottom: 10px;
  }
  div.sharesection .share p{
  color: white;
  font-size: 1rem;
  font-weight: 500;
  width: 100px;
}
div.sharesection .media-container{
  margin-left: 0.5rem;
}
div.sharesection .media-container .media{
  width: 2rem;
  height: 2rem;
  margin-right: 1rem;
}
div.sharesection .media-container > img:last-child{
  margin-right: 1.2rem;
}
}
</style>
