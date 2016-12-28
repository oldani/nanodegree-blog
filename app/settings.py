
class Base():
    """ Base configurations goes here. """
    DEBUG = False


class Development(Base):
    """ Here goes configuations values for development. """
    DEBUG = True


class Production(Base):
    """ Production configuration values. """
    pass
