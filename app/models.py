__author__ = 'liam'
from app import db

class SearchResult(db.Model):
    query = db.Column(db.String(80), primary_key=True)
    results = db.Column(db.BLOB())

    def __repr__(self):
        return '<SearchResult %r>' (self.query)

class PlaceRanking(db.Model):
    name = db.Column(db.String(120), primary_key=True)
    location = db.Column(db.String(200),index=True)
    computedrating = db.Column(db.Float(12))
    yelprating = db.Column(db.Float(12))
    quips = db.Column(db.String(280),index=True)

    def __repr__(self):
        return '<PlaceRanking %r>' (self.name)