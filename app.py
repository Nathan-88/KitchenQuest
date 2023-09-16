"""Flask app"""
from flask import Flask, request, session, redirect, url_for
from models.users import Users
from argon2 import PasswordHasher
from mongoengine.errors import *
from dotenv import load_dotenv
from os import getenv

load_dotenv()

passwordhasher = PasswordHasher()

app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')

@app.route('/', strict_slashes=False)
def index():
    return 'hello'


@app.route('/api/v1/user', methods=['POST', 'PUT'], strict_slashes=False)
def user():
    """save user details"""
    
    if request.method == 'POST':
        try:
            username = request.form.get('username',
                                        request.get_json().get('username'))
            password = request.form.get('password',
                                        request.get_json().get('password'))
            hashed_password = passwordhasher.hash(password)
            new_user = Users(username=username, password=hashed_password)
            new_user.save()
            return str(new_user.id)
        except NotUniqueError:
            return 'Username exists', 409


@app.route('/api/v1/user/verification', methods=['POST'], strict_slashes=False)
def verify_user():
    """user login authentication"""
    
    username = request.form.get('username',
                                request.get_json().get('username'))
    password = request.form.get('password',
                                request.get_json().get('password'))
    try:
        user = Users.objects.get(username=username)
        password_match = passwordhasher.verify(user.password, password)
        if password_match is True:
            session['user'] = username
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
    if 'user' in session:
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
    
    return redirect(url_for('verify_user'))


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
