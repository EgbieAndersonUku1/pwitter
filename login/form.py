from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class LoginForm(FlaskForm):

    username = StringField("Username", validators=[validators.DataRequired(), validators.Length(min=3, max=80)])
    password = PasswordField("Password", validators=[validators.DataRequired()])

