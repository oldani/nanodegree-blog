from datetime import datetime
from flask_user import current_user
from .base import BaseModel
from ..helpers import user_own_post


class Post(BaseModel):

    def __init__(self, **kwargs):
        # Add a comment list field and datetime fields
        # by default
        self.created = self.updated = datetime.now()
        self.comment_list = []
        super().__init__(**kwargs)

    def add_comment(self, comment_id):
        """ Append a comment id to a comment_list field. """
        self.comment_list.append(comment_id)
        self.update()

    def delete_comment(self, comment_id):
        """ Delete a given comment id from commnet list. """
        self.comment_list.remove(int(comment_id))
        self.update()

    def update(self, **kwargs):
        """ Update the updated field, before calling parent method. """
        self.updated = datetime.now()
        super().update(**kwargs)

    @classmethod
    def delete(cls, entity_id):
        """ Given a post id, delete it and all the corelated data. """
        # Needs to retrieve the post to have
        # acces to the comments related with it.
        post = cls.get(entity_id)
        if post and user_own_post(entity_id):
            if post.comment_list:
                cls.delete_multi(post.comment_list, kind='Comment')
            super().delete(entity_id)
            # Remove the post id from the list off post of a user
            current_user.posts_list.remove(int(entity_id))
            current_user.put()
            return True
        return

    def has_liked(self, user_id):
        """ Check if a given user has already like a post. """
        if hasattr(self, "users_liked") and user_id in self.users_liked:
            return True
        return

    def add_like(self, user_id):
        """ Add a like to a post. """
        if not hasattr(self, "likes"):
            self.likes = 0
            self.users_liked = []
        self.likes += 1
        self.users_liked.append(user_id)
        super().update()
