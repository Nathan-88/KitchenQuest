import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useRecipeStore = defineStore('recipes', () => {
    const recipes = ref(null);
    const recipeDetails = ref(null)

    const getRecipeResponse = computed(() => recipes.value)

    return { recipes, recipeDetails, getRecipeResponse }
})
