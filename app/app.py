from flask import Flask
from .extensions import db
from . import views


def create_app(config):
    """ Create a Flask App base on a config obejct. """

    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_views(app)

    # @app.route("/")
    # def index():
    #     return "Hello World!"

    return app


def register_extensions(app):
    """ Register all extensions with the app. """
    db.init_app(app)


def register_views(app):
    """ Register all views class. """
    views.Main.register(app)
