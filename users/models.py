from create_app import db
from tweets.models import Tweets

followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followee_id', db.Integer, db.ForeignKey('user.id')))


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    image = db.Column(db.String(255))
    joined_date = db.Column(db.String(255))
    tweets = db.relationship("Tweets", backref='user', lazy='dynamic')
    following = db.relationship('User', secondary=followers, primaryjoin=(followers.c.follower_id == id),
                                secondaryjoin=(followers.c.followee_id == id),backref=db.backref('followers', lazy='dynamic'),
                                lazy='dynamic')
    my_followers = db.relationship('User', secondary=followers, primaryjoin=(followers.c.followee_id == id),
                                secondaryjoin=(followers.c.follower_id == id),
                                backref=db.backref('followees', lazy='dynamic'), lazy='dynamic')


