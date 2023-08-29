from flask import Flask, render_template
from uuid import uuid4

app = Flask(__name__)

@app.route('/')
def index():
    """home page"""
    return render_template('home.html', cache_id=uuid4())


app.run(host='localhost', port=5000)
