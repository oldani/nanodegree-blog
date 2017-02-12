from flask import Flask
from flask.json import JSONEncoder
from flask_user import UserManager
from . import views
from .extensions import db, mail, toolbar
from .models import DataStoreAdapter, UserModel, BaseModel


def create_app(config):
    """ Create a Flask App base on a config obejct. """

    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_views(app)

    return app


def register_extensions(app):
    """ Register all extensions with the app. """
    db.init_app(app)
    mail.init_app(app)
    toolbar.init_app(app)

    # Cannot put it in extension files
    # due to will create a circular import.
    db_adapter = DataStoreAdapter(db, UserModel)
    user_manager = UserManager(db_adapter, app)
    app.json_encoder = CustomJsonEncoder


def register_views(app):
    """ Register all views class. """
    views.Main.register(app)
    views.Post.register(app)
    views.Comment.register(app)


class CustomJsonEncoder(JSONEncoder):
    """ Extend JSON Enconder, for encoding entity models."""

    def default(self, obj):
        try:
            if isinstance(obj, BaseModel):
                return obj.__dict__
        except AttributeError:
            pass
        return super().default(obj)
