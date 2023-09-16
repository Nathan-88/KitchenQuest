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
deployed_url = 'https://kitchen-quest-api.onrender.com'
local_url = 'http://127.0.0.1:5000'
new_user_response = requests.post(f'{local_url}/api/v1/user', json=user_details)
print(new_user_response.text)
verify_user_response = requests.post(f'{local_url}/api/v1/user/verification', data=user_details)
print(verify_user_response.text)
save_recipe_response = requests.post(f'{local_url}/api/v1/user/save-recipe', data=save_recipe)
print(save_recipe_response.text)