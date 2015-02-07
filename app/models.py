__author__ = 'liam'
from app import db

class SearchResult(db.Model):
    query = db.Column(db.String(80), primary_key=True)
    results = db.Column(db.BLOB())

    def __repr__(self):
        return '<SearchResult %r>' (self.query)