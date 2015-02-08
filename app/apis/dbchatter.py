__author__ = 'liam'

from app import db, models
from sqlalchemy import func
from random import randint

def getTwitterBall(yelpid):
    res = models.TwitterBall.query.filter_by(yelpid=yelpid).first()
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


def getRecentEntries(numresults):
    entries = getNumRows()
    results = set()
    for ii in range(entries,entries-numresults,-1):
        ball = getTwitterBallById(id)
        results.add(ball)
    return results



def main():
    print BallExists("Martians",{'lat':'30','long':'30'})

if __name__ == "__main__":
    main()