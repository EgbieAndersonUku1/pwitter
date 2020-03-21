from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.widgets import TextArea


class TweetsForm(FlaskForm):
    tweet = StringField("Post tweet", widget=TextArea(), validators=[validators.DataRequired(), validators.Length(max=140)])


class EditTweetForm(FlaskForm):

    tweet = StringField("Edit", widget=TextArea(), validators=[validators.DataRequired(), validators.Length(max=140)])


