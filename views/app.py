"""application endpoints"""
from flask import Flask, render_template
from controllers.middlewares import find_by_ingredients
from uuid import uuid4
import mimetypes


mimetypes.add_type('text/javascript', '.mjs', strict=True)

app = Flask(__name__)


@app.route('/')
def index():
    """home page"""
    return render_template('home.html', cache_id=uuid4())


@app.route('/saved_recipes')
def favourites():
    """saved recipe page"""
    return render_template('recipe_details.html', cache_id=uuid4())


@app.route('/shopping_list')
def get_shopping_list():
    """Users shopping list"""
    return render_template('shopping_list.html', cache_id=uuid4())


@app.route('/create_shopping_list')
def create_shopping_list():
    """Users shopping list"""
    return render_template('shopping_list.html', cache_id=uuid4())


@app.route('/registration')
def sign_up():
    """new user registration"""


@app.route('/login')
def login():
    """verification of registered user"""


@app.route('/user_profile')
def user_profile():
    """show profile page"""


@app.route('/search')
def get_recipes():
    """returns a list of recipes"""


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
