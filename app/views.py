from flask import render_template, flash, redirect, jsonify, request
from app import app
from .forms import SearchForm
from apis import yellow_api

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
        searchresults = yellow_api.search('Pizza', 'Montreal')


        return redirect('/results')
    return render_template('search.html',
                           title='Search',
                           form=form)

@app.route('/results', methods=['GET'])
def results():

    print searchresults
    #searchresults = [{'name':'McGoos Pizza','location':'Harrisonburg'}]
    return render_template('results.html',
                           searchresults=searchresults)
