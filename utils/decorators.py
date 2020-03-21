from functools import wraps
from flask import url_for
from werkzeug.utils import redirect

from flask import session


def login_required(f):
    @wraps(f)
    def login(*args, **kwargs):
        if session.get("username", None) is None:
            return redirect(url_for("user_app.index"))
        return f(*args, **kwargs)
    return login


def is_user_already_logged_in(f):
    @wraps(f)
    def is_user_logged_in(*args, **kwargs):
        if session.get("username", None):
            return redirect(url_for("user_app.index"))
        return f(*args, **kwargs)
    return is_user_logged_in