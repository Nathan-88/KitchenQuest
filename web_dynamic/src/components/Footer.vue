<template>
  <footer>
    <section class="footer-container">
          <div class="social-info">
              <img class="logo" src="../assets/images/Logo.svg" alt="Kitchen Quest">
              <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula.</p>
              <div class="media-container">
                  <img class="media" src="../assets/images/whatsapp.svg" alt="Whatsapp">
                  <img class="media" src="../assets/images/twitter.svg" alt="twitter">
                  <img class="media" src="../assets/images/instagram.svg" alt="instagram">
                  <img class="media" src="../assets/images/pinterest.svg" alt="pinterest">
              </div>
              <p class="copyright">2023 Kitchen Q All Rights Reserved</p>
          </div>
          <div>
              <h3>Yoruba Poraro</h3>
              <div class="extras">
                  <p>About</p>
                  <p>Recipes</p>
                  <p>Trending</p>
                  <p>Explore</p>
              </div>
          </div>
          <div>
              <h3>Yoruba Poraro</h3>
              <div class="extras">
                  <p>About</p>
                  <p>Recipes</p>
                  <p>Trending</p>
                  <p>Explore</p>
              </div>
          </div>
          <div>
              <h3>Yoruba Poraro</h3>
              <div class="extras">
                  <p>About</p>
                  <p>Recipes</p>
                  <p>Trending</p>
                  <p>Explore</p>
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
    height: 150px;
    min-width: 200px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
}

</style>