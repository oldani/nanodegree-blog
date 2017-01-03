""" Here goes all the extensions and configs options. """
from google.cloud import datastore


class Db:
    """ Class for common datastore functions. """

    def __init__(self):
        pass

    def init_app(self, app):
        self.client = datastore.Client(app.config["PROJECT_ID"])

    def from_datastore(self, entity):
        """ Translate Datastore results from:
                    [Entity{key: (kind, id), prop: val, ...}]
            To:     {id: id, prop: val, ...} """

        if not entity:
            return None
        if isinstance(entity, list):
            entity = entity.pop()

        entity['id'] = entity.key.id
        return entity

    def get(self, kind, id):
        """ Returns a single entity form Datastore. """
        db = self.client
        key = db.key(kind, int(id))
        return self.from_datastore(db.get(key))

    def put(self, kind, data, id=None):
        """ Create an Entity or update """
        db = self.client
        key = db.key(kind, int(id)) if id else db.key(kind)
        entity = datastore.Entity(key=key)
        entity.update(data)
        db.put(entity)
        return self.from_datastore(entity)

    # Updates and insert are almost the same
    update = put

    def delete(self, id, kind):
        """ Delete an Entity from Datastore. """
        db = self.client
        key = db.key(kind, int(id))
        db.delete(key)

db = Db()
