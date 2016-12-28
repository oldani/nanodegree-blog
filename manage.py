from decouple import config
from flask_escript import Manager, Shell, Server
from app.app import create_app
from app.settings import Development, Production

# Reads the Env vars if exist
ENVIRONMENT = config("ENVIRONMENT", default="DEV")

if ENVIRONMENT == "DEV":
    app = create_app(Development)
else:
    app = create_app(Production)


manager = Manager(app)


def _make_context():
    """ Create a context for when running the shell. """
    return dict(app=app)


manager.add_command("runserver", Server)
manager.add_command("shell", Shell)

if __name__ == "__main__":
    manager.run()
