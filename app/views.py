from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/search')

def index():
    user = {'nickname': 'Miguel'}
    return render_template('index.html',
                           title='Home',
                           user=user)


def search():
    return "You have reached the search page."
