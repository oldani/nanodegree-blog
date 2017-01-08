from decouple import config


class Base():
    """ Base configurations goes here. """
    DEBUG = False
    SECRET_KEY = config("SECRET_KEY")

    # Google Cloud Config
    PROJECT_ID = config("PROJECT_ID")

    # Flask WTForm Config
    WTF_CSRF_SECRET_KEY = config("WTF_CSRF_SECRET_KEY")

    # Flask-mail Config
    MAIL_USERNAME = config("MAIL_USERNAME")
    MAIL_PASSWORD = config("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = config("MAIL_DEFAULT_SENDER")
    MAIL_SERVER = config("MAIL_SERVER")
    MAIL_PORT = config("MAIL_PORT", cast=int)
    MAIL_USE_SSL = config("MAIL_USE_SSL", cast=bool)
    MAIL_USE_TLS = config("MAIL_USE_TLS", cast=bool)

    # Flask-User settings
    USER_APP_NAME = config("USER_APP_NAME")


class Development(Base):
    """ Here goes configuations values for development. """
    DEBUG = True


class Production(Base):
    """ Production configuration values. """
    pass
