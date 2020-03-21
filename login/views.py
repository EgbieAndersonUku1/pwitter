from flask import request, session, url_for, render_template, Blueprint
from werkzeug.utils import redirect

from users.models import User
from utils.decorators import is_user_already_logged_in
from login.form import LoginForm
from utils.security.passwd import Password


login_app = Blueprint("login_app", __name__)


@login_app.route("/login", methods=["GET", "POST"])
@is_user_already_logged_in
def login():

    form = LoginForm()
    error = None

    if request.method == "GET":
        error = None
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.lower()).first()

        if user and Password.check_password(form.password.data, user.password):
            session["username"] = form.username.data
            session["id"] = user.id
            return redirect(url_for("profile_app.profile", username=session.username))
        else:
            error = "Incorrect username and password"

    return render_template("index.html", form=form, error=error)
