from flask import render_template, flash, redirect, jsonify, request
from app import app, db, models
from .forms import SearchAreaForLocations
from apis import yellow_api
from apis import yelp_api
import json
from apis import dbchatter, analyzer


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
    form = SearchAreaForLocations()
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

@app.route('/analyze', methods=['GET'])
def analyze():
    name = request.args['name']
    readablename = request.args['name'].replace('+',' ')
    print(name)
    location = {'lat':request.args['lat'],'long':request.args['long']}
    print ("SEARCHED LOCATION IS " + str(location) + "NAME IS :" + name)
    if not analyzer.analyze(name, location) == "ERROR":
        twiball = dbchatter.getTwitterBall(name,location)
        return render_template('analysis.html',
                               name=readablename,
                               twitterball=twiball)
    else:
        flash('Not enough tweets for '+ readablename + ', try a new location.')
        return redirect('/search')

