from .base import BaseModel


class Post(BaseModel):

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
