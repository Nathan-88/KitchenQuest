"""Middlewares to process a request before the final response"""
import requests




def find_by_ingredients(ingredients):
    base_url = 'https://api.spoonacular.com/recipes/findByIngredients'
    params = {
        'apiKey': SPOONACULAR_API_KEY,
        'ingredients': ','.join(ingredients),
        'number': 10  # Number of recipes to retrieve
    }

    try:
        response = requests.get(base_url, params=params)
        recipes = response.json()
        return recipes
    except ConnectionError:
        print('Connection Down, Check your Internet Connection')