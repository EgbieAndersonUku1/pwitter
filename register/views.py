from flask import Blueprint, render_template, url_for, redirect

from os.path import join
from werkzeug.utils import secure_filename

from settings import UPLOAD_DIR
from users.models import User
from users.form import UserRegisterForm
from create_app import db
from utils.date import date_now, time_stamp
from utils.security.passwd import Password

register_app = Blueprint('register_app', __name__, url_prefix="/user")


@register_app.route("/", methods=["GET", "POST"])
def register():

    form = UserRegisterForm()

    if form.validate_on_submit():

        img_name = _upload_image_securely(form)

        user = User(name=form.name.data, username=form.username.data.lower(),
                    password=Password.hash_password(form.password.data),
                    image=img_name, joined_date=str(date_now()).split()[0]
                    )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login_app.login'))
    return render_template("register/register.html", form=form)


def _upload_image_securely(form):

    img_name = time_stamp() + secure_filename(form.image.data.filename)
    img_path = join(UPLOAD_DIR, img_name)
    form.image.data.save(img_path)
    return img_name


