__author__ = 'liam'

from app import db, models

def getTwitterBall(name, location=dict()):
    res = models.TwitterBall.query.filter_by(name=name).first()
    return res