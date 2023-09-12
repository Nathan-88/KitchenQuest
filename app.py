"""Flask app"""
from flask import Flask, request
from models.users import Users
from argon2 import PasswordHasher
from mongoengine.errors import *
import json

passwordhasher = PasswordHasher()

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return 'hello'


@app.route('/api/v1/user', methods=['POST', 'PUT'], strict_slashes=False)
def user():
    """save user details"""
    
    if request.method == 'POST':
        try:
            password = request.form.get('password')
            hashed_password = passwordhasher.hash(password)
            print(hashed_password)
            username = request.form.get('username')
            # print(username)

            new_user = Users(username=username, password=hashed_password)
            new_user.save()
            return str(new_user.id)
        except NotUniqueError:
            return 'Username exists', 409


@app.route('/api/v1/user/verification', methods=['POST'], strict_slashes=False)
def verify_user():
    """user login authentication"""
    
    password = request.form.get('password')
    username = request.form.get('username')
    try:
        user = Users.objects.get(username=username)
        password_match = passwordhasher.verify(user.password, password)
        if password_match is True:
            return 'success'
        else:
            return 'Invalid Password', 401
    except DoesNotExist:
        return 'User does not exist', 401
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return 'An Error has occured while processing your request', 500


@app.route('/api/v1/user/save-recipe', methods=['POST'], strict_slashes=False)
def save_recipe():
    """save recipe for user"""
    
    recipe_title = request.form.get('recipe_title')
    username = request.form.get('username')
    try:
        user = Users.objects.get(username=username)
        user.saved_recipes.append(recipe_title)
        user.save()
    except DoesNotExist:
        return 'User not logged in', 401
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return 'An Error has occured while processing your request', 500
    
    return 'success'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
