from ..extensions import db


class BaseModel:
    """ Base class with basics methods for all the models. """
    db = db

    def __init__(self, **kwargs):
        self.kind = self.get_kind(self)
        for field, value in kwargs.items():
            self.__setattr__(field, value)

    @staticmethod
    def get_kind(cls):
        """ Given a class or instance return the class name. """
        if isinstance(cls, BaseModel):
            return cls.__class__.__name__
        return cls.__name__

    @classmethod
    def get(cls, entity_id):
        """ Find a model entity given the id of it. """
        entity_kind = cls.get_kind(cls)
        result = cls.db.get(entity_kind, entity_id)
        if result:
            entity = cls()
            for field_name, value in result.items():
                entity.__setattr__(field_name, value)
            return entity
        return None

    @classmethod
    def get_multi(cls, entities_keys):
        """ Find a given list of entities id. """
        return cls.db.get_multi(cls.get_kind(cls), entities_keys)

    def put(self):
        """ Save a entity to the Datastore. If an id attr does not
        exist means that the entity haven't been created, otherwise
        only make a update. """
        if hasattr(self, 'id'):
            return self.db.update(self.kind, self.__dict__, self.id)
        self.id = self.db.put(self.kind, self.__dict__)
        return self

    def update(self, **kwargs):
        """ If a dict is given set to as obj attrs. """
        if kwargs:
            for field, value in kwargs.items():
                self.__setattr__(field, value)
        return self.put()

    @classmethod
    def set_query(cls):
        """ Set a query class attribute. """
        entity_kind = cls.get_kind(cls)
        cls.query = cls.db.client.query(kind=entity_kind)

    @classmethod
    def add_query_filter(cls, field, operator, value):
        """ Add given filters to a query. """
        if not hasattr(cls, 'query'):
            cls.set_query()
        cls.query.add_filter(field, operator, value)
        return cls

    @classmethod
    def fetch(cls, **kwargs):
        """ Fetch the entitys that match a existing query or a new one.
        Once the query is made del the attr. If entities were
        retrieve return a list a entitys objs. """
        if not hasattr(cls, 'query'):
            cls.set_query()
        entities = map(db.from_datastore, cls.query.fetch(**kwargs))
        entities = list(entities)
        delattr(cls, 'query')
        if entities:
            result = [cls(**entity) for entity in entities]
            return result
        return None

    @classmethod
    def delete(cls, entity_id):
        """ Delete a entity of a given id. """
        return cls.db.delete(cls.get_kind(cls), entity_id)

    @classmethod
    def delete_multi(cls, entities_id, kind=None):
        """ Delete a  list of Entities from a given list of IDs. """
        if kind:
            return cls.db.delete_multi(kind, entities_id)
        return cls.db.delete_multi(cls.get_kind(cls), entities_id)
