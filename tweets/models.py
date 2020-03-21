from create_app import db


class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tweet = db.Column(db.String(140))
    live = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime)