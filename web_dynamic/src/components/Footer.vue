<script setup>
import { RouterLink } from 'vue-router';
import { getRecipe } from '../utilities';
</script>
<template>
  <footer>
    <section class="footer-container">
        <div class="social-info">
            <img class="logo" src="@/assets/images/Logo.svg" alt="Kitchen Quest">
            <p>Welcome to KitchenQuest - Your Culinary Companion</p>
            <div class="media-container">
                <img class="media" src="@/assets/images/whatsapp.svg" alt="Whatsapp">
                <img class="media" src="@/assets/images/twitter.svg" alt="twitter">
                <img class="media" src="@/assets/images/instagram.svg" alt="instagram">
                <img class="media" src="@/assets/images/pinterest.svg" alt="pinterest">
            </div>
            <p class="copyright">2023 Kitchen Q All Rights Reserved</p>
        </div>
        <div>
            <h3>Navigation</h3>
            <div class="extras">
                <p><router-link to="/">Home</router-link></p>
                <p><router-link to="/about">About</router-link></p>
                <p><router-link to="" @click="getRecipe('trending')">Trending</router-link></p>
                <p><router-link to="" @click="getRecipe('european cuisine')">Explore</router-link></p>
            </div>
        </div>
        <div>
            <h3>User Navigation</h3>
            <div class="extras">
                <p data-userRoles="Sign up">Sign Up</p>
                <p data-userRoles="Login">Login</p>
                <p data-userRoles="Favourites"><router-link to="/saved_recipes">Favourites</router-link></p>
            </div>
        </div>
        <div>
            <h3>More Explore Options</h3>
            <div @click="(event) => getRecipe(event.target.dataset.cuisine)" class="extras">
                <p data-cuisine="european cuisine">European Cuisine</p>
                <p data-cuisine="african cuisine">African Cuisine</p>
                <p data-cuisine="indian cuisine">Indian Cuisine</p>
                <p data-cuisine="italian cuisine">Italian Cuisine</p>
            </div>
            <div @click="(event) => getRecipe(event.target.dataset.diet)" class="extras">
                <!-- <h3>More Diets</h3> -->
                <p data-diet="glutenfree">GlutenFree</p>
                <p data-diet="vegetarian">Vegetarian</p>
                <p data-diet="ketogenic">Ketogenic</p>
            </div>
        </div>
    </section>
  </footer>
</template>

<style scoped>
footer{
    max-width: 100vw;
    min-height: 400px;
    background-color: #E4E9E9;
    color: var(--hash-color);
}
footer h3{
    color: #3F3F3F;
    margin-bottom: 30px;
}
section.footer-container{
    max-width: 90%;
    display: grid;
    /* flex-flow: row wrap-reverse;
    justify-content: space-between; */
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 50px;
    margin-inline: auto;
    padding-top: 30px;
    padding-bottom: 30px;
}
section.footer-container p{
    margin: 5px;
    cursor: pointer;
}
div.social-info{
    min-width: 200px;
    height: 100%;
    display: grid;
    grid-template-rows: repeat(4, 1fr);
    grid-template-columns: 1fr;
    gap: 20px;
}
div.social-info img.logo{
    width: 150px;
    height: 50px;
}

div.social-info p:nth-child(2){
    font-size: 12px;
    width: 35ch;
}
div.media-container{
    height: 50px;
    width: 100%;
}
div.social-info img.media{
    width: 30px;
    height: 30px;
}
p.copyright{
    margin-top: 40px;
}
div.extras{
    height: fit-content;
    min-width: 200px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
}
div.extras a{
    text-decoration: none;
    color: inherit;
}

</style>