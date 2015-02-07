__author__ = 'liam'
from app import db

class SearchResult(db.Model):
    query = db.Column(db.String(80), primary_key=True)
    results = db.Column(db.BLOB())

    def __repr__(self):
        return '<SearchResult %r>' (self.query)

class TwitterBall(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    tweets = db.Column(db.String(3000))
    ranking = db.Column(db.String(20))
    rankscore = db.Column(db.Float())
    ranktype = db.Column(db.Boolean())

    def __repr__(self):
        return '<TwitterBall for {0}>'.format(self.name)


class PlaceRanking(db.Model):
    name = db.Column(db.String(120), primary_key=True)
    location = db.Column(db.String(200),index=True)
    computedrating = db.Column(db.Float(12))
    yelprating = db.Column(db.Float(12))
    quips = db.Column(db.String(280),index=True)

    def __repr__(self):
        return '<PlaceRanking %r>' (self.name)