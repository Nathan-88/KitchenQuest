<template>
  <section class="trending">
        <h2>Trending</h2>
        <section class="trending-list">
            <div class="trending-recipe">
                <img src="../assets/images/image-4.png" alt="recipe name">
                <div class="recipe-content">
                    <h3>Yoruba Poraro</h3>
                    <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt</p>
                </div>
            </div>
            <div class="trending-recipe">
                <img src="../assets/images/image-4.png" alt="recipe name">
                <div class="recipe-content">
                    <h3>Yoruba Poraro</h3>
                    <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt</p>
                </div>
            </div>
            <div class="trending-recipe">
                <img src="../assets/images/image-4.png" alt="recipe name">
                <div class="recipe-content">
                    <h3>Yoruba Poraro</h3>
                    <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt</p>
                </div>
            </div>
            <div class="trending-recipe">
                <img src="../assets/images/image-4.png" alt="recipe name">
                <div class="recipe-content">
                    <h3>Yoruba Poraro</h3>
                    <p>Nulla in lorem vitae mi ornare porttitor. Fusce nec nisi non ligula fermentum tincidunt</p>
                </div>
            </div>
        </section>
    </section>
</template>

<style scoped>
section.trending{
    width: 100%;
    min-height: 380px;
    display: grid;
    grid-template-rows: 70px 1fr;
    grid-template-columns: 1fr;
    row-gap: 30px;
}
section.trending-list{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    grid-template-rows: auto;
    row-gap: 50px;
    width: 100%;
    min-height: 350px;
    margin-bottom: 30px;
}
section.trending .trending-recipe{
    width: 70%;
    height: 240px;
    border-radius: 100px 0px 100px 0px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    position: relative;
    margin-top: 50px;
    margin-inline: auto;
}
.trending-recipe:nth-child(odd){
    background-color: white;
}
div.recipe-content{
    margin-top: 70px;
}
div.trending-recipe img{
    width: 200px;
    height: 200px;
    position: absolute;
    top: -80px;
}
div.trending-recipe h3{
    font-size: 15px;
    font-weight: 700;
}
div.trending-recipe p{
    font-size: 12px;
    width: 80%;
    margin: auto;
}
</style>