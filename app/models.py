__author__ = 'liam'
from app import db
from datetime import datetime

class SearchResult(db.Model):
    query = db.Column(db.String(80), primary_key=True)
    results = db.Column(db.BLOB())

    def __repr__(self):
        return '<SearchResult %r>' (self.query)

class TwitterBall(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=1)
    name = db.Column(db.String(100), index=True)
    lat = db.Column(db.Float(), index=True)
    long = db.Column(db.Float(), index=True)
    locname = db.Column(db.String(30),index=True)
    tweets = db.Column(db.String(3000))
    ranking = db.Column(db.String(20))
    rankscore = db.Column(db.Float())
    ranktype = db.Column(db.Boolean())

    def __repr__(self):
        return '<TwitterBall for {0}>'.format(self.name)


class PlaceRanking(db.Model):
    id = db.Column(db.ForeignKey(TwitterBall.id))
    name = db.Column(db.String(120), primary_key=True)
    computedrating = db.Column(db.Float(12))
    yelprating = db.Column(db.Float(12))
    quips = db.Column(db.String(280),index=True)

    def __repr__(self):
        return '<PlaceRanking %r>' (self.name)