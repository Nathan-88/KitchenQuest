<script setup>
import Navbar from '../components/Navbar.vue'
</script>

<template>
  <!-- Hero Section -->
  <header>
    <section class="nav-container">
      <nav id="navbar-container">
        <Navbar />
      </nav>
      <h1 class="shadow_heading">request</h1>
      <div class="hero-text-container">
        <p class="hero-text">Discover Recipes for</p>
        <p class="hero-text">Delicious Foods around</p>
        <p class="hero-text">the World</p>
      </div>
      <div class="search">
        <input type="text" name="recipe_search" id="recipe-search" placeholder="Search for Recipes">
        <button type="submit">Go</button>
      </div>
    </section>
    <section class="red_box"></section>
    <div class="dots"></div>
    <img src="/static/images/Rectangle 2.png" alt="food" class="food-image">
  </header>
  <main>
    <!-- Random Section -->
    <section class="random">
      <div class="quote">
        <span class="red-bar"></span>
        <p>The internet famous always pan just got a huge update</p>
      </div>
      <div class="quote-two">
        <h3>the world</h3>
        <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt vel non quam. Nullam</p>
      </div>
    </section>
    <!-- Recipe Section -->
    <section class="recipes">
      <h2>Recipes</h2>
      <section class="recipe-display">
        <div class="random-recipe-image"><!-- div for an image, check css --></div>
        <div class="recipe-container">
          <img class="recipe-image" src="/static/images/Rectangle 7.png?{{ cache_id }}" alt="recipe name">
          <div class="recipe-content-container">
            <div class="recipe-description">
              <h3>Yoruba Poraro</h3>
              <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt</p>
            </div>
            <button type="submit">Go</button>
          </div>
        </div>
        <div class="recipe-container">
          <img class="recipe-image" src="/static/images/Rectangle 7.png?{{ cache_id }}" alt="recipe name">
          <div class="recipe-content-container">
            <div class="recipe-description">
              <h3>Yoruba Poraro</h3>
              <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt</p>
            </div>
            <button type="submit">Go</button>
          </div>
        </div>
      </section>
    </section>
    <!-- Trending Section -->
    <section class="trending">
        <h2>Trending</h2>
        <section class="trending-list">
            <div class="trending-recipe">
                <img src="/static/images/image-4.png?{{ cache_id }}" alt="recipe name">
                <div class="recipe-content">
                    <h3>Yoruba Poraro</h3>
                    <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt</p>
                </div>
            </div>
            <div class="trending-recipe">
                <img src="/static/images/image-4.png?{{ cache_id }}" alt="recipe name">
                <div class="recipe-content">
                    <h3>Yoruba Poraro</h3>
                    <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt</p>
                </div>
            </div>
            <div class="trending-recipe">
                <img src="/static/images/image-4.png?{{ cache_id }}" alt="recipe name">
                <div class="recipe-content">
                    <h3>Yoruba Poraro</h3>
                    <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt</p>
                </div>
            </div>
            <div class="trending-recipe">
                <img src="/static/images/image-4.png?{{ cache_id }}" alt="recipe name">
                <div class="recipe-content">
                    <h3>Yoruba Poraro</h3>
                    <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt</p>
                </div>
            </div>
        </section>
    </section>
    <!-- Explore Section -->
    <section class="explore">
        <h2>Explore</h2>
        <div class="explore-list">
            <img src="/static/images/Rectangle 25.png?{{ cache_id }}" alt="cuisine name">
            <img src="/static/images/Rectangle 25.png?{{ cache_id }}" alt="cuisine name">
            <img src="/static/images/Rectangle 25.png?{{ cache_id }}" alt="cuisine name">
        </div>
    </section>
  </main>
</template>
