"""Flask app"""
from flask import Flask
from controllers.users_handler import users_handler
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')
SESSION_COOKIE_PATH = '/'
app.register_blueprint(users_handler, url_prefix='/api/v1/user')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
