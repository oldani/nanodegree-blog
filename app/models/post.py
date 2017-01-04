from .base import BaseModel


class Post(BaseModel):

    def __init__(self, **kwargs):
        self.kind = "Post"
        super().__init__(self.kind, **kwargs)
