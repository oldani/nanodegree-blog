from flask_user import DBAdapter


class DataStoreAdapter(DBAdapter):
    """ An Wrapper to be use by Flask User to interact with
        the database in this case, the DataStore """

    def __init__(self, db, objMOdel):
        super().__init__(db, objMOdel)

    def get_object(self, ObjectClass, pk):
        """ Retrieve an single Entity specified by a pk or id. """
        entity = ObjectClass().get(pk)
        entity = ObjectClass(**entity)
        return entity

    def find_all_objects(self, ObjectClass, **kwargs):
        """ Retrieve all Entity matching  all the filters in kwargs. """
        # TODO:
        # The filters should be case sensitive
        return ObjectClass().fetch()

    def find_first_object(self, ObjectClass, **kwargs):
        """ Retrieve the first Entity matching the filters in kwargs or None. """
        # TODO:
        # The filters should be case sensitive
        entity = ObjectClass()
        for key, value in kwargs.items():
            entity.query.add_filter(key, "=", value)
        entity = entity.fetch(limit=1)
        # Just return the Entity is the list is not empty and the
        # first element is not None or Falsy else return None
        entity = ObjectClass(**entity[0]) if entity and entity[0] else None
        return entity

    def ifind_first_object(self, ObjectClass, **kwargs):
        """ Retrieve the first Entity matching the filters in kwargs or None. """
        # TODO:
        # The filters should be case insensitive
        entity = ObjectClass()
        for key, value in kwargs.items():
            entity.query.add_filter(key, "=", value)
        entity = entity.fetch(limit=1)
        # Just return the Entity is the list is not empty and the
        # first element is not None or Falsy else return None
        entity = ObjectClass(**entity[0]) if entity and entity[0] else None
        return entity

    def add_object(self, ObjectClass, **kwargs):
        """ Create an Entity with the fields specified in kwargs. """
        entity = ObjectClass(**kwargs)
        entity.put()
        return entity

    def update_object(self, entity, **kwargs):
        """ Update an Entity with the fields specified in kwargs. """
        entity.update(entity.get_id(), kwargs)
        return entity

    def delete_object(self, entity):
        """ Delete and Entity. """
        entity.delete(entity.id)
        return entity

    def commit(self):
        """ Should commit a create, update, all delete to the DataStore. """
        pass
