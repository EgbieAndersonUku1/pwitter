from flask import url_for, session, render_template, abort, Blueprint

from users.models import User
from utils.date import prettify_date
from utils.decorators import login_required
from utils.security.is_url_safe import if_url_is_safe_redirect
from create_app import db


follow_app = Blueprint("follow_app", __name__, url_prefix="/follow")


@follow_app.route("/unfollow/<username>")
@login_required
def unfollow(username):

    user = User.query.filter_by(username=username).first()

    if not user:
        abort(404)

    my_profile = User.query.filter_by(username=session["username"]).first()
    my_followees = my_profile.followees.all()

    if user in my_followees:
        my_followees.remove(user)

        my_profile.followees = my_followees
        db.session.add(my_profile)
        db.session.commit()
    return if_url_is_safe_redirect(_get_url())


@follow_app.route("/my_followers/<username>")
@login_required
def my_followers(username):

    user = User.query.filter_by(username=username).first()

    if not user:
        abort(404)
    return render_template("followers/my_followers.html", user=user, prettify_date=prettify_date,
                           followers=user.my_followers.all())


@follow_app.route("/follow/<username>")
@login_required
def follow_user(username):

    user_to_follow = User.query.filter_by(username=username).first()
    user = User.query.filter_by(username=session['username']).first()

    if not user_to_follow:
        abort(404)
    user.following.append(user_to_follow)
    db.session.add(user)
    db.session.commit()

    return if_url_is_safe_redirect(_get_url())


def _get_url():
    return url_for("user_app.users")