<script setup>
const props = defineProps({
    imageSrc: String,
    recipeTitle: String,
    summary: String
})

let summary = props.summary?.replace(/<\/?[^>]+(>|$)/g, "")
</script>

<template>
    <section class="recipe-item">
        <div class="film"></div>
        <img :src="props.imageSrc" alt="#">
        <div class="recipe-summary">
            <h3>{{ props.recipeTitle }}</h3>
            <!-- <div class="likes"></div> -->
            <p class="summary"><b>Summary:</b> {{ summary }}</p>
        </div>
    </section>
</template>

<style scoped>
section.recipe-item{
    position: relative;
    /* background-color: white; */
    width: 100%;
    /* height: 200px; */
    display: grid;
    grid-template-rows: 220px;
    grid-template-columns: 1fr 1fr;
    justify-content: center;
    align-items: center;
    /* padding: 20px; */
}
section.recipe-item img{
    width: 170px;
    height: 170px;
    margin: auto;
    border-radius: 15px;
    object-fit: cover;
}
section.recipe-item h3{
    font-size: 14px;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: 2;
    display: -webkit-box;
    -webkit-box-orient: vertical;
}
div.recipe-summary{
    /* background-color: aqua; */
    max-width: 200px;
    height: 170px;
    margin: auto;
    display: grid;
    row-gap: 10px;
    grid-template-rows: 40px 120px;
    grid-template-columns: 1fr;
    /* flex-direction: column;
    justify-content: space-around; */
}
.summary{
    height: 100%;
    overflow: hidden;
    font-size: 11.5px;
    /* add custom ellipsis to overflowing text */
    text-overflow: ellipsis;
    -webkit-line-clamp: 7;
    display: -webkit-box;
    -webkit-box-orient: vertical;
}
div.film{
    position: absolute;
    height: 100%;
    width: 100%;
    display: none;
}
section.recipe-item:hover div.film{
    display: block;
    cursor: pointer;
    background-color: rgba(100, 94, 94, 0.5);
}
@media(min-width: 800px){
    section.recipe-item{
        position: relative;
        /* background-color: white; */
        width: 100%;
        height: 250px;
        display: grid;
        grid-template-rows: 250px;
        grid-template-columns: 1fr 1fr;
        /* padding: 20px; */
    }
    section.recipe-item img{
        width: 90%;
        height: 90%;
        margin: auto;
        border-radius: 15px;
        object-fit: cover;
    }
    section.recipe-item h3{
        font-size: 18px;
        overflow: hidden;
        text-overflow: ellipsis;
        -webkit-line-clamp: 2;
        display: -webkit-box;
        -webkit-box-orient: vertical;
    }
    div.recipe-summary{
        max-width: 100%;
        height: 90%;
        margin: auto;
        display: grid;
        row-gap: 10px;
        grid-template-rows: 50px 145px;
        grid-template-columns: 1fr;
        /* flex-direction: column;
        justify-content: space-around; */
    }
    .summary{
        height: 100%;
        overflow: hidden;
        font-size: 12px;
        /* add custom ellipsis to overflowing text */
        text-overflow: ellipsis;
        -webkit-line-clamp: 8;
        display: -webkit-box;
        -webkit-box-orient: vertical;
    }
    div.film{
        position: absolute;
        height: 100%;
        width: 100%;
        display: none;
    }
    section.recipe-item:hover div.film{
        display: block;
        cursor: pointer;
        background-color: rgba(100, 94, 94, 0.5);
    }
}
</style>