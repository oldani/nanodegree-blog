from .base import BaseModel


class User(BaseModel):
    """ User's model. """
    username = None
    email = None
    password = None

    def __init__(self, **kwargs):
        self.kind = "User"
        super().__init__(self.kind, **kwargs)
        self.username = self.data.get("username")
        self.email = self.data.get("email")
        self.password = self.data.get("password")
        self.posts_list = self.data.get("posts_list")

    def get_id(self):
        """ Retrieve an Entity ID attribute if set or from data dict. """
        try:
            return self.id
        except AttributeError:
            return self.data.get("id")

    def set_active(self, active):
        """ Set an User as activated when confirm email,
            to be use by Flask User. """
        self.data["is_active"] = active
        if self.confirmed_at:
            # Flask User set and comfirmed_at atttribute when email
            # is confirmed, if done add to data dict
            self.data["confirmed_at"] = self.confirmed_at
        self.update()

    def has_confirmed_email(self):
        """ Use by Flask User to check if an user has validate his email. """
        return self.data.get("confirmed_at")

    def is_active(self):
        """ Use by Flask User to check if and user account is active."""
        return self.data.get("is_active")

    @property
    def is_authenticated(self):
        """ User by Flask Login to check if and user is authenticated. """
        return True

    def add_post(self, post_id):
        """ Add a post id to the user posts list or create it if not
            exits as a one to many relationship. """
        if not self.posts_list:
            self.posts_list = self.data["posts_list"] = []
        self.posts_list.append(post_id)
        self.update()

    def update(self):
        """ Extends update method from BaseModel. """
        super().update(self.get_id(), self.data)
