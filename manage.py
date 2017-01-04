from decouple import config
from flask_script import Manager, Shell, Server
from app import create_app
from app.settings import Development, Production
from app.extensions import db

# Reads the Env vars if exist
ENVIRONMENT = config("ENVIRONMENT", default="DEV")

if ENVIRONMENT == "DEV":
    app = create_app(Development)
else:
    app = create_app(Production)


manager = Manager(app)


def _make_context():
    """ Create a context for when running the shell. """
    return dict(app=app, db=db)


manager.add_command("runserver", Server)
manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == "__main__":
    manager.run()
