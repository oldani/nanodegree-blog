from flask_classy import FlaskView


class Main(FlaskView):
    """ Main page view. """
    route_base = "/"

    def index(self):
        return "HEEEEYYYYY"
