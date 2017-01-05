from decouple import config


class Base():
    """ Base configurations goes here. """
    DEBUG = False
    SECRET_KEY = config("SECRET_KEY")
    PROJECT_ID = config("PROJECT_ID")
    WTF_CSRF_SECRET_KEY = config("WTF_CSRF_SECRET_KEY")


class Development(Base):
    """ Here goes configuations values for development. """
    DEBUG = True


class Production(Base):
    """ Production configuration values. """
    pass
