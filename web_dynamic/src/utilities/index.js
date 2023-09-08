import router from '@/router'
import { useRecipeStore } from '@/stores'
import axios from 'axios'
import { ref } from 'vue'



export const defaultParams = {
  apiKey: import.meta.env.VITE_SPOONACULAR_API_KEY,
  instructionsRequired: true,
  sort: 'random',
  addRecipeInformation: true,
  addRecipeNutrition: true,
  sortDirection: 'asc',
  number: 10
}

const fetchRecipe = async (searchValue) => {
  const store = useRecipeStore()
  // create a default params object
  const params = {...defaultParams}
  // conditionally set the optional params for the api
  if (searchValue.includes('cuisine')) {
      const cuisine = searchValue.replace("cuisine", "")
      params.cuisine = cuisine
  } else if (searchValue.includes('diet')) {
      const diet = searchValue.replace("diet", "")
      params.diet = diet
  } else if (!searchValue.includes('trending')){
      params.includeIngredients = searchValue
  }

  return axios({
      url: import.meta.env.VITE_SPOONACULAR_BASE_URL,
      params: params
  }).then((response) =>  {
    // check for empty result, so a different page can be displayed
      if (response.data['results'].length === 0) return null
      store.recipes = response.data['results']
      return true
  })
  .catch((error) => {
    console.error(error)
    return false
  })
}

export const getRecipe = async (query) => {
  console.log('called me')
  const status = await fetchRecipe(query)
  if (status) router.push({name: 'search', params: {recipe: query}})
  if (status === null) router.push({name: 'NoResult'})
  else router.push({name: 'error'})
}

export const moreDetails = (recipeObj) => {
  const store = useRecipeStore()
  store.recipeDetails = recipeObj
  router.push({name: "RecipePage"})
}

export const persistState = (stateName) => {
  const state = localStorage.getItem(stateName)
  if (typeof state === 'string') {
    return ref(JSON.parse(state))
  }
  return ref(null)
}



// module.exports = { getRecipe, moreDetails }
