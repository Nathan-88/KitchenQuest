<script setup>
import Navbar from '@/components/Navbar.vue';
import { useRecipeStore } from '@/stores';

const store = useRecipeStore()

const recipe = store.recipeDetails
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
      <span><b>Ingredients: </b></span>
      <span class="span" v-for="ingredient in recipe.nutrition.ingredients" :key="ingredient.id">
        <em>{{ ingredient.name }};  </em>
      </span>
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
    width: 100%;
    height: auto;
    display: block;
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
</style>
