from .base import BaseModel


class Comment(BaseModel):
    """ Comments Model. """

    def __init__(self, **kwargs):
        self.kind = "Comment"
        super().__init__(self.kind, **kwargs)
