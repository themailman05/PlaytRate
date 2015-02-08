__author__ = 'liam'

from app import db, models
from sqlalchemy import func
from random import randint

def getTwitterBall(name, location=dict()):
    res = models.TwitterBall.query.filter_by(name=name, lat=location['lat'], long=location['long']).first()
    return res

def getTwitterBallById(id):
    res = models.TwitterBall.query.filter_by(id=id).first()
    return res


def BallExists(yelpid):
    if models.TwitterBall.query.filter_by(yelpid=yelpid).first():
        return True
    else:
        return False

def getNumRows():
    rows = db.session.query(models.TwitterBall).count()
    return rows


def getRandomEntries(numentries):
    entries = db.session.query(models.TwitterBall).count()
    print entries
    results = []
    for ii in range(numentries):
        jj = randint(1,entries)
        results.append(getTwitterBallById(jj))
    return results



def main():
    print BallExists("Martians",{'lat':'30','long':'30'})

if __name__ == "__main__":
    main()