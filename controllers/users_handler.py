"""Flask app"""
from flask import Flask, request, session, redirect, url_for, jsonify, Blueprint
from models.users import Users
from argon2 import PasswordHasher
from mongoengine.errors import *
from dotenv import load_dotenv
from os import getenv

load_dotenv()

passwordhasher = PasswordHasher()
SESSION_COOKIE_PATH = '/'
users_handler = Blueprint('users_handler', __name__)


@users_handler.route('/registeration', methods=['POST'], strict_slashes=False)
def register_user():
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
            return jsonify({
                'message': 'success',
                'user_id': str(new_user.id)
            })
        except NotUniqueError:
            return jsonify({'message': 'Username exists'}), 409


@users_handler.route('/login', methods=['POST'], strict_slashes=False)
def login():
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
            print(session)
            return jsonify({'message': 'success'})
        else:
            return jsonify({'message': 'Invalid Password'}), 401
    except DoesNotExist:
        return jsonify({'message': 'User does not exist'}), 401
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return jsonify({
            'message': 'An Error has occured while processing your request'
        }), 500


@users_handler.route('/logout', strict_slashes=False)
def logout():
    """user logout"""
    print(session)
    try:
        session.pop('user')
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return jsonify({
                'message': 'An Error occured while processing your request',
                'error_details': f'{type(error).__name__}'
            }), 500
    
    return jsonify({'message': 'User logged out successfully'})


@users_handler.route('/save-recipe', methods=['POST'], strict_slashes=False)
def save_recipe():
    """save recipe for user"""
    if 'user' in session:
        recipe_title = request.form.get('recipe_title',
                                        request.get_json().get('recipe_title'))
        username = session.get('user')
        try:
            user = Users.objects.get(username=username)
            user.saved_recipes.append(recipe_title)
            user.save()
        except Exception as error:
            print(f'{type(error).__name__}: {type(error).__name__}')
            return jsonify({
                'message': 'An Error occured while processing your request',
                'error_details': f'{error}'
            }), 500
        
        return jsonify({'message': 'success'})
    
    return jsonify({'message': 'User not logged in'}), 401
