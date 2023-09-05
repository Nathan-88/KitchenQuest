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

// module.exports = { getRecipe, moreDetails }
