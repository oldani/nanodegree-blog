from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, TextAreaField


class PostForm(FlaskForm):
    """ Form for posts. """
    title = StringField('title', validators=[InputRequired()])
    body = TextAreaField('body', validators=[InputRequired()])
