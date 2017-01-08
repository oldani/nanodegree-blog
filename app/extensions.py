""" Here goes all the extensions and configs options. """
from google.cloud import datastore
from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension


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

    def get(self, kind, entity_id):
        """ Returns a single entity form Datastore. """

        db = self.client
        key = db.key(kind, int(entity_id))
        return self.from_datastore(db.get(key))

    def put(self, kind, data, entity_id=None):
        """ Create an Entity or update """

        db = self.client
        key = db.key(kind, int(entity_id)) if entity_id else db.key(kind)
        entity = datastore.Entity(key=key)
        entity.update(data)
        db.put(entity)
        return entity.key.id, self.from_datastore(entity)

    # Updates and insert are almost the same
    update = put

    def delete(self, kind, entity_id):
        """ Delete an Entity from Datastore. """

        db = self.client
        key = db.key(kind, int(entity_id))
        db.delete(key)


# GClound DataStore wrapper
db = Db()

# Flask Mail
mail = Mail()

# Flask Debug
toolbar = DebugToolbarExtension()
