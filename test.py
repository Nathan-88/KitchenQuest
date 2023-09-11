"""Test the database setup"""
import requests

user_details = {
    'username': 'Wonderful',
    'password': 'Testpassword'
}

response = requests.post('http://localhost:5000/api/v1/user', data=user_details)
# response = requests.get('http://localhost:5000')
print(response.text)
