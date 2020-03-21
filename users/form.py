from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, validators, ValidationError, FileField, PasswordField

import re

from users.models import User

_PATTERN_TO_MATCH = "^[a-zA-Z0-9_-]{3,80}$"


class UserRegisterForm(FlaskForm):
    name = StringField("Name", validators=[validators.DataRequired(), validators.Length(min=3, max=80)])
    username = StringField("Username", validators=[validators.DataRequired(), validators.Length(min=3, max=80)])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=8, max=255),
                                                     validators.EqualTo("confirm")
                                                     ])
    confirm = PasswordField("Confirm password")
    image = FileField("image", validators=[validators.DataRequired(), FileAllowed(["jpg", "jpeg", "gif", "png"])])

    def validate_name(form, field):

        if not re.search(_PATTERN_TO_MATCH, field.data):
            raise ValidationError("Invalid username")

    def validate_username(form, field):

        if not re.search(_PATTERN_TO_MATCH, field.data):
            raise ValidationError("Invalid username")
        elif User.query.filter_by(username=field.data.lower()).first():
            raise ValidationError("The username already exists")

