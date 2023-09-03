<script setup>
import router from '../router';

const getDiet = (target) => {
  if (target.dataset.diet !== undefined) {
    console.log(`Getting ${target.dataset.diet}`)
    router.push({name: "search", params: {ingredient: target.dataset.diet}})
  }
}
</script>

<template>
  <section class="recipes">
      <h2>Diet Recipes</h2>
      <section @click="(event) => getDiet(event.target)" class="recipe-display">
        <div class="random-recipe-image"><!-- div for an image, check css --></div>
        <div class="recipe-container">
          <img class="recipe-image" src="../assets/images/vegetarian-diet.webp" alt="recipe name">
          <div class="recipe-content-container">
            <div class="recipe-description">
              <h3>Vegetarian</h3>
              <p>No ingredients may contain meat or meat by-products, such as bones or gelatin.</p>
            </div>
            <button type="submit" data-diet="vegetarian diet">Go</button>
          </div>
        </div>
        <div class="recipe-container">
          <img class="recipe-image" src="../assets/images/ketogenic-diet.jpg" alt="recipe name">
          <div class="recipe-content-container">
            <div class="recipe-description">
              <h3>Ketogenic</h3>
              <p>The keto diet is based more on the ratio of fat, protein, and carbs in the diet rather than specific ingredients</p>
            </div>
            <button type="submit" data-diet="ketogenic diet">Go</button>
          </div>
        </div>
        <div class="recipe-container">
          <img class="recipe-image" src="../assets/images/gluten-free-diet.jpg" alt="recipe name">
          <div class="recipe-content-container">
            <div class="recipe-description">
              <h3>Gluten Free</h3>
              <p>Eliminating gluten means avoiding wheat, barley, rye, and other gluten-containing grains and foods made from them (or that may have been cross contaminated)</p>
            </div>
            <button type="submit" data-diet="Gluten Free diet">Go</button>
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
}
section.recipes h2{
    grid-row: 1/2;
    justify-self: center;
    height: 30px;
    width: 100%;
    text-align: right;
}
section.recipe-display{
    grid-row: 2/3;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    justify-items: center;
    row-gap: 30px;
    width: 100%;
    min-height: 350px;
}
section.recipes .random-recipe-image{
    width: 300px;
    height: 338px;
    flex-shrink: 0;
    background: url('../assets/images/image-1d 1.png');
    background-color: var(--background-color);
    background-size: contain;
    background-repeat: no-repeat;
    display: inline-block;
    /* grid-column: 1/2; */
}
div.recipe-container{
    /* grid-column: 2/3; */
    display: grid;
    grid-template-rows: 290px 1fr;
    justify-items: center;
    width: 100%;
}
img.recipe-image{
    height: 100%;
    width: 300px;
}
div.recipe-container .recipe-content-container{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    width: 300px;
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
</style>