from flask import render_template
from flask import jsonify
from flask import request
from app import app

@app.route('/')
@app.route('/index')
@app.route('/search')
@app.route("/getip", methods=["GET"])



def index():
    return render_template('index.html',
                           title='Home',
                           recent = [{'name':'Mah Pizza',
                                      'location':'Harrisonburg',
                                      'rating':3.5,
                                      'numratings':1000}])

def get_my_ip():
    return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200

def search():
    return "You have reached the search page."
