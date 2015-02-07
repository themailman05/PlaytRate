__author__ = 'liam'

from app import db, models

def getTwitterBall(name, location=dict()):
    result = {'name':name, 'location':location,}
    res =models.TwitterBall.query.get(name)
    print res
    return 'ok'