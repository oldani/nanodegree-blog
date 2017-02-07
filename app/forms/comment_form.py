from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import InputRequired, Length


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment:', validators=[InputRequired(),
                                                    Length(min=6,
                                                    message="Your comment should be as min\
                                                    6 characters lenght.")])
