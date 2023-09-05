import router from '../router'

export const getRecipe = (recipe) => {
  console.log('clicked:', recipe)
  router.push({name: 'search', params: {recipe: recipe}})
}

export const moreDetails = (recipeObj) => {
  const recipeJson = JSON.stringify(recipeObj)
  console.log(recipeObj);
  router.push({name: "RecipePage", params: {recipe: recipeJson}})
}

export const defaultParams = {
  apiKey: import.meta.env.VITE_SPOONACULAR_API_KEY,
  instructionsRequired: true,
  sort: 'random',
  addRecipeInformation: true,
  addRecipeNutrition: true,
  sortDirection: 'asc',
  number: 10
}

// module.exports = { getRecipe, moreDetails }
