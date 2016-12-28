from flask import Flask


def create_app(config):
    """ Create a Flask App base on a config obejct. """

    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)

    return app


def register_extensions(app):
    """ Register all extensions with the app. """

    pass
