from .base import BaseModel


class Post(BaseModel):

    def __init__(self, **kwargs):
        self.kind = "Post"
        super().__init__(self.kind, **kwargs)
        self.comment_list = self.data.get("comment_list")

    def add_comment(self, comment_id):
        """ Append a comment id to a comment_list field. """
        if not self.comment_list:
            self.comment_list = self.data["comment_list"] = []
        self.comment_list.append(comment_id)
        self.update()

    def delete_comment(self, comment_id):
        """ Delete a given comment id from commnet list. """
        # self.comment_list.remove(comment_id)
        # self.update()
        pass

    def update(self, entity_id=None, data=None):
        if not entity_id and not data:
            return super().update(self.data.get("id"), self.data)
        return super().update(entity_id, data)
