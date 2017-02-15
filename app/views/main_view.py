from flask import render_template
from flask_classy import FlaskView
from ..models import PostModel


class Main(FlaskView):
    """ Main page view. """

    route_base = "/"

    def index(self):
        PostModel.set_query()
        PostModel.query.order = ['-updated', 'title']
        posts = PostModel.fetch()
        return render_template("index.html", posts=posts)
