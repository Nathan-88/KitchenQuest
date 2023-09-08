<script setup>
import { getRecipe } from '@/utilities';
</script>

<template>
  <section class="recipes">
      <h2>Diet Recipes</h2>
      <section class="recipe-display">
        <div class="random-recipe-image"><!-- div for an image, check css --></div>
        <div class="recipe-container">
          <img class="recipe-image" src="@/assets/images/vegetarian-diet.webp" alt="recipe name">
          <div class="recipe-content-container">
            <div class="recipe-description">
              <h3>Vegetarian</h3>
              <p>No ingredients may contain meat or meat by-products, such as bones or gelatin.</p>
            </div>
            <button @click="(event) => getRecipe(event.target.dataset.diet)" type="submit" data-diet="vegetarian diet">Go</button>
          </div>
        </div>
        <div class="recipe-container">
          <img class="recipe-image" src="@/assets/images/ketogenic-diet.jpg" alt="recipe name">
          <div class="recipe-content-container">
            <div class="recipe-description">
              <h3>Ketogenic</h3>
              <p>The keto diet is based more on the ratio of fat, protein, and carbs in the diet rather than specific ingredients</p>
            </div>
            <button @click="(event) => getRecipe(event.target.dataset.diet)" type="submit" data-diet="ketogenic diet">Go</button>
          </div>
        </div>
        <div class="recipe-container">
          <img class="recipe-image" src="@/assets/images/gluten-free-diet.jpg" alt="recipe name">
          <div class="recipe-content-container">
            <div class="recipe-description">
              <h3>Gluten Free</h3>
              <p>Eliminating gluten means avoiding wheat, barley, rye, and other gluten-containing grains and foods made from them (or that may have been cross contaminated)</p>
            </div>
            <button @click="(event) => getRecipe(event.target.dataset.diet)" type="submit" data-diet="Gluten Free diet">Go</button>
          </div>
        </div>
      </section>
    </section>
</template>

<style scoped>
section.recipes {
    display: grid;
    grid-template-rows: 50px 2.5fr;
    grid-template-columns: minmax(40px, 1fr);
    margin: 50px 0;
    margin-bottom: 0px;
}
section.recipes h2{
    grid-row: 1/2;
    justify-self: center;
    height: 10px;
    width: 100%;
    text-align: right;
    color: #261A5A;
    /*margin-bottom: 10px;*/
}
section.recipe-display{
    grid-row: 2/3;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    justify-items: center;
    row-gap: 30px;
    width: 100%;
    min-height: 320px;
}
section.recipes .random-recipe-image{
    width: 100%;
    height: 100%;
    flex-shrink: 0;
    background: url('@/assets/images/food-random-image.png');
    background-color: var(--background-color);
    background-size: contain;
    background-repeat: no-repeat;
    /* background-position: center; */
    display: inline-block;
    /* margin-top: 2px; */
    position: relative;
    top: -20px;
}
@media(max-width: 599px){
  /* 
     This would have preference over the one above until 600px
     The preference is because the bottom style for the same property
     has more preference over the top style, top to bottom approach 
  */
  section.recipes .random-recipe-image{
      width: 100vw;
      height: 338px;
      position: relative;
      background-position: 35px;
  }
}
div.recipe-container{
    /* grid-column: 2/3; */
    display: grid;
    grid-template-rows: 290px 1fr;
    justify-items: center;
    width: 100%;
}
img.recipe-image{
    height: 70%;
    width: 290px;
    margin-top: 10px;
    object-fit: cover;
}
div.recipe-container .recipe-content-container{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    width: 290px;
    margin-top: -78px;
}
div.recipe-container div.recipe-description {
    grid-column: 1/4;
    display: grid;
    grid-template-rows: 20px 50px;
    grid-template-columns: 1fr;
    background-color: white;
    height: 52px;
}
div.recipe-description h3{
    padding-inline: 10px;
    font-size: 12px;
}
div.recipe-description p{
    padding-inline: 10px;
    font-size: 10px;
    height: 30px;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: 2;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    /* background-color: aqua; */
}
div.recipe-container button{
    height: 52px;
    width: 100%;
    background-color: var(--red-color);
    color: white;
    font-style: normal;
    border-style: none;
    cursor: pointer;
}
@media(min-width: 800px){
  section.recipes .random-recipe-image{
    width: 300px;
    height: 338px;
    flex-shrink: 0;
    background: url('@/assets/images/image-1d 1.png');
    background-color: var(--background-color);
    background-size: contain;
    background-repeat: no-repeat;
    display: inline-block;
    margin-top: 2px;
    position: static;
  }
}
</style>