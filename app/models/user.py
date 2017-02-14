from .base import BaseModel


class User(BaseModel):
    """ User's model. """
    username = None
    email = None

    def get_id(self):
        """ Retrieve an Entity ID attribute, necessary for Flask User. """
        try:
            return self.id
        except AttributeError:
            return None

    def set_active(self, active):
        """ Set an User as activated when email have been confirmend,
            to be use by Flask User. """
        self.is_active = active
        self.update()

    def has_confirmed_email(self):
        """ Use by Flask User to check if an user has validate his email. """
        return self.confirmed_at

    def is_active(self):
        """ Use by Flask User to check if and user account is active."""
        return self.is_active

    @property
    def is_authenticated(self):
        """ User by Flask Login to check if and user is authenticated. """
        return True

    def add_post(self, post_id):
        """ Add a post id to the user posts list or create it if not
            exits. """
        if not hasattr(self, 'posts_list'):
            self.posts_list = []
        self.posts_list.append(post_id)
        self.update()
