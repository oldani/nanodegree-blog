from flask import Flask
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

    pass


def register_views(app):
    """ Register all views class. """
    views.Main.register(app)
