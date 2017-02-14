from .base import BaseModel
from flask_user import current_user


class Post(BaseModel):

    def __init__(self, **kwargs):
        # Add a comment list field
        self.comment_list = []
        super().__init__(**kwargs)

    def add_comment(self, comment_id):
        """ Append a comment id to a comment_list field or
        create it if it is the firt one. """
        if not hasattr(self, 'comment_list'):
            self.comment_list = []
        self.comment_list.append(comment_id)
        self.update()

    def delete_comment(self, comment_id):
        """ Delete a given comment id from commnet list. """
        self.comment_list.remove(int(comment_id))
        self.update()

    @classmethod
    def delete(cls, entity_id):
        post = cls.get(entity_id)
        if post:
            if post.comment_list:
                cls.delete_multi(post.comment_list, kind='Comment')
            super().delete(entity_id)
            current_user.posts_list.remove(int(entity_id))
            current_user.put()
            return True
        return
