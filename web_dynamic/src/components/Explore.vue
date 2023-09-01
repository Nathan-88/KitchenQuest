<script setup>
import router from '../router';

const getCuisine = (target) => {
  console.log(`Getting ${target.dataset.cuisine}`)
  router.push({name: "search", params: {ingredient: target.dataset.cuisine}})
}
</script>

<template>
  <section class="explore">
        <h2>Explore</h2>
        <div @click="(event) => getCuisine(event.target)" class="explore-list">
            <div class="image" data-cuisine="italian cuisine">
              <p data-cuisine="italian cuisine">Italian Cuisine</p>
            </div>
            <div class="image" data-cuisine="indian cuisine">
              <p data-cuisine="indian cuisine">Indian Cuisine</p>
            </div>
            <div class="image" data-cuisine="chinese cuisine">
              <p data-cuisine="chinese cuisine">Chinese Cuisine</p>
            </div>
        </div>
    </section>
</template>

<style scoped>
section.explore{
    width: 100%;
    min-height: 450px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin-bottom: 30px;
}
section.explore h2{
    width: 50%;
    height: 70px;
    margin-inline: auto;
    /* background-color: green; */
}
section.explore .explore-list{
    min-width: 80%;
    min-height: 300px;
    margin-inline: auto;
    display: flex;
    flex-flow: wrap row;
    justify-content: center;
}
div.image{
    width: 300px;
    height: 300px;
    background-repeat: no-repeat;
    background-size: cover;
    cursor: pointer;
    color: whitesmoke;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 30px;
}
div.image p{
  position: relative;
}
div.image:first-child{
  background-image: url('../assets/images/italian-cuisine.jpg');
}
div.image:nth-child(2){
  background-image: url('../assets/images/indian-cuisine.jpg');
}
div.image:nth-child(3){
  background-image: url('../assets/images/chinese-cuisine.jpg');
}
div.image::before{
  content: "";
  position: absolute;
  background-color: rgba(0, 0, 0, 0.8);
  left: 0px;
  right: 0px;
  bottom: 0px;
  top: 0px
}
div.image:hover{
  background-color: rgba(0, 0, 0, 0.7);
  opacity: 0.9;
}
</style>