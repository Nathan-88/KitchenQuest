import { defineStore } from "pinia";
import { computed } from "vue";
import { persistState } from "@/utilities";

export const useRecipeStore = defineStore('recipes', () => {
    const recipes = persistState('recipes');
    const recipeDetails = persistState('recipeDetails')
    const trending = persistState('trending')

    const getRecipeResponse = computed(() => recipes.value)

    return { recipes, recipeDetails, trending, getRecipeResponse }
})
