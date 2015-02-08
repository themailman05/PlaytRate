from flask import render_template, flash, redirect, jsonify, request
from app import app, db, models
from .forms import SearchAreaForLocations
from apis import yellow_api
from apis import yelp_api
import json
from apis import dbchatter, analyzer
from pprint import pprint


decoder = json.JSONDecoder

@app.route('/')
@app.route('/index')
def index():
    form = SearchAreaForLocations()
    if dbchatter.getNumRows() > 4:
        return render_template('index.html',
                               title='Home',
                               recent=dbchatter.getRandomEntries(5),
                               form=form)

    else:
        return render_template('index.html',
                               title='Home',
                               form=form)


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
    searchresults= yelp_api.shortsearch(request.form['searchquery'],request.form['location'])
    return render_template('results.html',
                           searchresults=searchresults,
                           location=request.form['location'])

@app.route('/analyze', methods=['GET'])
def analyze():
    name = request.args['name']
    businessinfo = yelp_api.getBusinessDetail(name)
    location = {'lat':businessinfo['location']['coordinate']['latitude'],'long':businessinfo['location']['coordinate']['longitude']}
    readablename = businessinfo['name']
    print "READABLE NAME" +readablename
    if dbchatter.BallExists(name,location):    #do not analyze if in database
        return render_template('analysis.html',
                               name=readablename,
                               twitterball=dbchatter.getTwitterBall(name, location))
    else:
        result = analyzer.analyze(readablename,location)
        if result == "ERROR":
            flash('Not enough tweets for '+ readablename + ', try a new location.')
            return redirect('/search')
        else:
            twiball = dbchatter.getTwitterBall(name,location)
            return render_template('analysis.html',
                                   name=readablename,
                                   twitterball=twiball)


