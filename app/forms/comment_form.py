from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length


class Comment(FlaskForm):
    comment = StringField('comment', validators=[InputRequired(), Length(min=6,
                                                 message="Your comment should be\
                                                 as min 6 characters lenght.")])
