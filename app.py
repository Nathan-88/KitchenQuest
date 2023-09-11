"""Flask app"""
from flask import Flask, request
from models.users import Users
import json

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return 'hello'


@app.route('/api/v1/user', methods=['POST'], strict_slashes=False)
def user():
    """save user details"""
    
    password = request.form.get('password')
    print(password)
    username = request.form.get('username')
    print(username)
    # data = request.form
    # print(data)

    new_user = Users(username=username, password=password)
    new_user.save()
    return str(new_user.id), 200


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
