<script setup>
import Navbar from '../components/Navbar.vue';
</script>
<template>
  <Navbar :showsearch="true" />

  <main>
    <section id="about-top">
      <h1>How To Navigate</h1>
      <div id="about">
        <img src="../assets/images/image7.png" alt="display image"/>
        <article>
          <div>
          <h2>Everything you want in the search box</h2>
          </div>
          <p>
              KitchenQuest aims to solve the challenges of deciding what to cook based on the ingredients 
              available to users. Often, people find themselves with a collection of ingredients but lack the 
              inspiration to create a meal. This application will bridge that gap by suggesting recipes that 
              can be prepared using the ingredients the user already has. It's designed to streamline the cooking 
              process, reduce food waste, and offer creative culinary options even when faced with limited ingredients.
          </p>
        </article>
      </div>
    </section>
  </main>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}


#about-top h1 {
    color: #261A5A;
    font-family: Poppins;
    font-size: 45px;
    font-style: normal;
    font-weight: 700;
    line-height: 60%; /* 128px */
    letter-spacing: -1.4px;
    margin-left: 14px;
    bottom: 0px;
    padding: 10px 10px 0px 50px;  
}

#about-top div {
    width: flex;
    height: 500px;
    margin: 0;
    background: white;
    position: relative;
}

#about-top div img {
    width: 500px;
    height: 436px;
    margin: 30px;
}

div#about div{
    background: #261A5A;
    position: absolute;
    top: 90px;
    margin-bottom: 0px;
    left: 550px;
    margin: 0px;
    /* padding: 10px 10px 10px 10px;
    width: 50px;
    height: 50px; */
    height: 50px;
}
#about-top div h2 {
    color: white;
    font-family: Poppins;
    font-size: 30px;
    font-style: normal;
    font-weight: 400;
    line-height: 100%; /* 128px */
    letter-spacing: -0.4px;
    padding: 10px;
}

div#about p{
    font-family: Poppins;
    font-size: 16px;
    position: absolute;
    top: 150px;
    left: 550px;
    width: 600px;
}
</style>