from flask import session, url_for, flash, render_template, Blueprint, abort

from login.form import LoginForm
from tweets.forms import TweetsForm, EditTweetForm
from tweets.models import Tweets
from users.models import User, followers
from utils.date import date_now, get_time_passed_since
from utils.decorators import login_required
from utils.security.is_url_safe import if_url_is_safe_redirect
from create_app import db


tweets_app = Blueprint("tweets_app", __name__, url_prefix="/tweets")


@tweets_app.route("/post", methods=["POST"])
@login_required
def post_tweets():

    form = TweetsForm()

    if form.validate():
        tweets = Tweets(user_id=session["id"], tweet=form.tweet.data, date_created=date_now(), live=True)
        db.session.add(tweets)
        db.session.commit()
        flash("You tweet has been posted")

        return if_url_is_safe_redirect(_get_url())
    flash("Could not post tweet something went wrong")


@tweets_app.route("/edit/<id>", methods=["GET", "POST"])
@login_required
def edit_tweet(id):

    form = EditTweetForm()

    tweet_obj = Tweets.query.filter_by(id=id).first()

    if tweet_obj:
        form = EditTweetForm(obj=tweet_obj)

    if form.validate_on_submit() and session["id"] == tweet_obj.user_id:
        tweet_obj.tweet = form.tweet.data
        db.session.add(tweet_obj)
        db.session.commit()
        return if_url_is_safe_redirect(_get_url())

    return render_template("tweet/edit_tweet.html", form=form, id=id)


@tweets_app.route("/delete/<tweet_id>")
@login_required
def delete_tweet(tweet_id):

    tweet = Tweets.query.filter_by(id=tweet_id).first()
    if tweet and session["id"] == tweet.user_id:
        tweet.live = False
        db.session.add(tweet)
        db.session.commit()
    return if_url_is_safe_redirect(_get_url())


@tweets_app.route("/timeline/<username>")
@tweets_app.route("/timeline")
def timeline(username=None):
    tweets_form = TweetsForm()
    user = None
    viewing_my_page = False

    if username:
        user = User.query.filter_by(username=username).first()
    elif username is None and session.get("username"):
        viewing_my_page = True
        user = User.query.filter_by(username=session["username"]).first()

    if not user:
        abort(404)

    if viewing_my_page:
        tweets = Tweets.query.join(followers, (followers.c.followee_id == Tweets.user_id)). \
            filter(followers.c.follower_id == user.id, Tweets.live == True). \
            order_by(Tweets.date_created.desc()).all()

    else:
        tweets = Tweets.query.filter(User.id == user.id, Tweets.live == True).order_by(Tweets.date_created.desc()).all()

    watching = User.query.filter(User.id != user.id).order_by(db.func.random()).limit(4).all()

    return render_template("tweet/tweet_timeline.html", form=LoginForm(), tweets_form=tweets_form, tweets=tweets,
                           time_passed=get_time_passed_since, user=user, watching=watching)

def _get_url():
    return url_for("tweets_app.timeline", username=session["username"])