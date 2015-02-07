__author__ = 'liam'

from app import db, models

def getTwitterBall(name, location=dict()):
    res = models.TwitterBall.query.filter_by(name=name, location=location).first()
    return res

def BallExists(name, location=dict()):
    if models.TwitterBall.query.filter_by(name=name).first():
        return True
    else:
        return False


def main():
    print BallExists("Martians",{'lat':'30','long':'30'})

if __name__ == "__main__":
    main()