from flask import render_template, flash, redirect, jsonify, request
from app import app, db, models
from .forms import SearchForm
from apis import yellow_api
from apis import yelp_api
import json


decoder = json.JSONDecoder

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home',
                           recent = [{'name':'Mah Pizza',
                                      'location':'Harrisonburg',
                                      'rating':3.5,
                                      'numratings':1000}])


@app.route("/getip", methods=["GET"])
def getip():
    return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Search requested for query="%s", location="%s"' %
             (form.searchquery.data, form.location.data))

        return redirect('/results')
    return render_template('search.html',
                           title='Search',
                           form=form)

@app.route('/results', methods=['GET','POST'])
def results():
    searchresults= yelp_api.query_api(request.form['searchquery'],request.form['location'])
    return render_template('results.html',
                           searchresults=searchresults)

@app.route('/analyze/', methods=['GET'])
def analyze():

