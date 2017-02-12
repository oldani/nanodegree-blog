from datetime import datetime
from .base import BaseModel


class Comment(BaseModel):

    def __init__(self, **kwargs):
        # Add created and updated attrs by default.
        self.created = self.updated = datetime.now()
        super().__init__(**kwargs)

    def update(self):
        """ Extends update method to update some fields before saving. """
        self.updated = datetime.now()
        super().update()
