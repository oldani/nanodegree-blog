from ..extensions import db


class Post(object):
    """ Post Model"""
    def __init__(self, **kwargs):
        self.kind = "Post"
        self.db = db
        self.query = self.db.client.query(kind=self.kind)
        self.data = kwargs or None

    def get(self, id):
        return self.db.get(self.kind, id)

    def put(self, data=None, id=None):
        if data:
            return self.db.put(self.kind, data)
        return self.db.put(self.kind, self.data)

    update = put

    def fetch(self):
        return list(self.query.fetch())

    def delete(self, id):
        return self.db.delete(self.kind, id)
