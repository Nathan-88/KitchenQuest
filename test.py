"""Test the database setup"""
import requests

user_details = {
    'username': 'Test User',
    'password': 'Testpassword'
}
save_recipe = {
    'username': 'Test User',
    'recipe_title': 'Gbegiri Soup'
}

new_user_response = requests.post('https://kitchen-quest-api.onrender.com/api/v1/user', data=user_details)
print(new_user_response.text)
verify_user_response = requests.post('https://kitchen-quest-api.onrender.com/api/v1/user/verification', data=user_details)
print(verify_user_response.text)
save_recipe_response = requests.post('https://kitchen-quest-api.onrender.com/api/v1/user/save-recipe', data=save_recipe)
print(save_recipe_response.text)