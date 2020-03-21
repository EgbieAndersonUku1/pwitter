from flask import abort, session, render_template, Blueprint


from tweets.models import Tweets
from users.models import User
from utils.date import prettify_date
from utils.date import get_time_passed_since
from create_app import db

profile_app = Blueprint("profile_app", __name__, url_prefix="/profile")


@profile_app.route("/profile/<username>")
@profile_app.route("/profile")
def profile(username=None):

    user = None
    following = False

    if username is None:
        user = User.query.filter_by(username=session["username"]).first()
    elif username:
        user = User.query.filter_by(username=username).first()
        my_profile = User.query.filter_by(username=session["username"]).first()

        if my_profile in user.followers.all():
            following = True

    if not user:
        abort(404)

    tweets = Tweets.query.filter(User.id == session["id"], Tweets.live == True).order_by(Tweets.date_created.desc()).all()
    pretty_date = prettify_date(user.joined_date, new_date_format="%A %d %B, %Y")
    followees = user.my_followers.all()

    watching = User.query.filter(User.name != session['username']).order_by(db.func.random()).limit(4).all()
    return render_template("profile/profile.html", user=user, pretty_date=pretty_date, tweets=tweets,
                           time_passed=get_time_passed_since, followees=followees, following=following,
                           watching=watching)