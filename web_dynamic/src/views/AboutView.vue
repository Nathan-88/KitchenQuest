<script setup>
import Navbar from '@/components/Navbar.vue';
</script>
<template>
  <!-- Ignore the div, it's for animation -->
  <div>
    <Navbar :showsearch="true" />
  
    <main>
      <div class="hero">
        <h2>About KitchenQuest</h2>
        <p>Your Culinary Companion</p>
      </div>
      <div class="container">
        <section>
            <h2>Introduction</h2>
            <p>At KitchenQuest, our journey began with a shared frustration that many of us have faced in our own kitchens. You know that feeling when you open your pantry and fridge to find a collection of ingredients, but the inspiration to create a meal seems elusive? We've been there too.
            It was in those moments of culinary uncertainty that we decided to create an application to bridge the gap between ingredients and delicious meals. We wanted to make the cooking process easier and more enjoyable for everyone. That's how KitchenQuest was born.</p>
            <p>
            Imagine this: you open our app, and it's like having a personal chef right in your pocket. You can simply input the ingredients you have on hand, and KitchenQuest will suggest mouthwatering recipes that you can prepare with what you already have. No more staring at your pantry in confusion!</p>
            <p>
            But we didn't stop there. We also understand the importance of dietary preferences. Whether you're a vegetarian, following a Ketogenic diet, or need gluten-free options, we've got you covered. With KitchenQuest, you can search for recipes based on your preferences, and we'll provide you with a tailored list of delicious options.
            Our mission is deeply personal to us. We know the daily dilemma of deciding what to prepare for meals, especially when your ingredients seem random and disconnected. Our goal is simple: to help you effortlessly create memorable meals. With KitchenQuest, you'll not only discover new recipes but also make the most of the ingredients you have, and savor the joy of cooking.</p>
        </section>
        
        <section>
            <h2>Our Mission</h2>
            <p>At KitchenQuest, we empathize with the daily struggle of figuring out what to cook, especially when your ingredients appear haphazard and unrelated. Our purpose is straightforward: to facilitate the creation of unforgettable meals with ease. Through KitchenQuest, you'll explore fresh recipes, optimize your available ingredients, and relish the pleasures of cooking. Our aim is to equip you with a tool that transforms your kitchen into a domain of boundless culinary potential, no matter the contents of your refrigerator.</p>
        </section>
        
        <!-- Add more sections for each feature as needed -->
        
        <section class="features">
            <h2>Explore Our Features</h2>
            <div class="feature-item">
                <ul>
                  <li>
                  <p><span><b>Ingredient Magic: </b></span>Don't know what to cook with the ingredients in your pantry? KitchenQuest's Ingredient Magic is here to help. Simply enter the items you have, and we'll conjure up a list of recipes you can whip up right away.</p>
                  </li>
                  <li>
                  <p><span><b>Personalized Suggestions:</b></span>Your taste buds are unique, and we get that. KitchenQuest learns your preferences and suggests recipes tailored just for you. Vegan, gluten-free, meat-eater – we've got you covered.</p>
                  </li>
                  <li>
                  <p><span><b>Cook Like a Pro:</b></span>Step-by-step instructions, pro tips, and beautiful imagery make cooking a breeze. Whether you're making a family dinner or trying your hand at gourmet cuisine, you'll feel like a master chef.</p>
                  </li>
                  <li>
                  <p><span><b>Build Your Shopping List:</b></span>Need to stock up on ingredients? KitchenQuest allows you to add missing items from your chosen recipe directly to your shopping list. No more forgotten items at the grocery store.</p>
                  </li>
                  <li>
                  <p><span><b> Share and Connect:</b></span>Food brings people together. Share your culinary creations with friends and family through KitchenQuest, and discover what they're cooking too. Connect, inspire, and swap recipes with fellow food enthusiasts.</p>
                  </li>
                </ul>
            </div>
        </section>

        <section>
            <h2>Our Promise</h2>
            <p>KitchenQuest is more than just an app; it's your trusted companion in the kitchen. We promise to continuously improve and expand our offerings, ensuring that your cooking experience is always exciting and hassle-free.</p>
        </section>
        
        <section>
            <h2>Contact Us</h2>
            <p>Got questions, suggestions, or just want to say hi? We'd love to hear from you! Reach out to our friendly support team at <a href="#">contact@email.com</a>.</p>
        </section>
    </div>
    </main>
  </div>
</template>

<style scoped>
.hero{
  text-align: center;
  margin: 0, auto;
  background-size: cover;
  max-width: 100%;
  height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  background-color: rgba(0, 0, 0,0.5);
}
.hero h2{
  font-size: 50px;
  font-weight: 600;
  font-family: var(--primary-font);
}
.hero p{
  font-size: 24px;
}
.hero::before{
  content: "";
  position: absolute;
  background-image: url('@/assets/images/Rectangle30.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  left: 0px;
  right: 0px;
  bottom: 0px;
  top: 0px;
  z-index: -1;
}
.container {
    max-width:100%;
    margin: 0 auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

p{
    font-size: 16px;
    line-height: 1.5;
    color: var(--hash-color);
    /* background-color: ; */
    padding: 10px;
}

h2 {
    font-size: 24px;
    font-weight: 600;
    background-color: #FD043C;
    color: #fff;
    border-radius: 3px;
    width: fit-content;
    padding: 2px 10px;
}

span{
  color: #000;
}

.hero h2, .hero p{
  color: #fff;
  background: none;
  width: 100%;
  font-weight: 800;
  line-height: 1.8em;
}

/* Customize Styles */

.feature-item {
    padding: 20px 0;
}

.feature-item ul{
  color: #000;
  padding-left: revert;
}
</style>