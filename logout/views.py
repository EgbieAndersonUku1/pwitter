from flask import session, url_for, redirect, Blueprint

logout_app = Blueprint("logout_app", __name__, url_prefix="/logout")


@logout_app.route("/logout")
def logout():

    if session.get("username"):
        session.clear()
    return redirect(url_for("user_app.index"))
