from flask import Blueprint, render_template, session

from login.form import LoginForm
from users.models import User
from utils.date import prettify_date
from utils.decorators import login_required

user_app = Blueprint('user_app', __name__)


@user_app.route("/")
def index():
    return render_template("index.html", form=LoginForm())



@user_app.route("/users")
@login_required
def users():
    users = User.query.all()
    my_profile = User.query.filter_by(username=session["username"]).first()
    return render_template("users/users.html", users=users, prettify_date=prettify_date, my_profile=my_profile)

