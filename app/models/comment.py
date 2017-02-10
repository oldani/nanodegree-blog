from datetime import datetime
from .base import BaseModel


class Comment(BaseModel):
    """ Comments Model. """

    def __init__(self, **kwargs):
        self.kind = "Comment"
        super().__init__(self.kind, **kwargs)

    def put(self):
        """ Extends put method to add some extra fields before saving. """
        self.data['created'] = datetime.now()
        self.data['updated'] = datetime.now()
        super().put()

    def update(self):
        """ Extends update method to update some fields before saving. """
        if self.data.get('updated'):
            self.data['updated'] = datetime.now()
        super.update(self.data.get("id"), self.data)
