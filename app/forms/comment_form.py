from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length


class CommentForm(FlaskForm):
    post_id = IntegerField('post_id', validators=[InputRequired()])
    comment = StringField('comment', validators=[InputRequired(), Length(min=6,
                                                 message="Your comment should be\
                                                 as min 6 characters lenght.")])
