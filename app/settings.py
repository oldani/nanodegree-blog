from decouple import config


class Base():
    """ Base configurations goes here. """
    DEBUG = False
    PROJECT_ID = config("PROJECT_ID")


class Development(Base):
    """ Here goes configuations values for development. """
    DEBUG = True


class Production(Base):
    """ Production configuration values. """
    pass
