from ..extensions import db


class BaseModel:
    """ Base class with basics methods for all the models. """

    def __init__(self, kind, **kwargs):
        self.kind = kind
        self.db = db
        self.query = self.db.client.query(kind=self.kind)
        self.data = kwargs

    def get(self, id):
        return self.db.get(self.kind, id)

    def put(self, data=None, entity_id=None):
        """ If data and id are pass means a update. """
        if data and entity_id:
            return self.db.put(self.kind, data, entity_id)
        self.id, _ = self.db.put(self.kind, self.data)

    update = put

    def fetch(self):
        """ Execute lazy query and convert obj to a list. """
        return list(self.query.fetch())

    def delete(self, entity_id):
        return self.db.delete(self.kind, entity_id)
