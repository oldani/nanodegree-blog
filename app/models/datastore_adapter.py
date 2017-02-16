from flask_user import DBAdapter


class DataStoreAdapter(DBAdapter):
    """ An Wrapper to be use by Flask User to interact with
        the database in this case, the DataStore """

    def __init__(self, db, objMOdel):
        super().__init__(db, objMOdel)

    def get_object(self, ObjectClass, pk):
        """ Retrieve an single Entity specified by a pk or id. """
        return ObjectClass.get(pk)

    def find_all_objects(self, ObjectClass, **kwargs):
        """ Retrieve all Entity matching  all the filters in kwargs. """
        # TODO:
        # The filters should be case sensitive
        for field, value in kwargs.items():
            ObjectClass.add_query_filter(field, "=", value)
        return ObjectClass.fetch()

    def find_first_object(self, ObjectClass, **kwargs):
        """ Retrieve the first Entity matching the filters in
        kwargs or None. """
        # TODO:
        # The filters should be case sensitive
        for field, value in kwargs.items():
            ObjectClass.add_query_filter(field, "=", value)
        entity = ObjectClass.fetch(limit=1)
        return entity[0]

    def ifind_first_object(self, ObjectClass, **kwargs):
        """ Retrieve the first Entity matching the filters in
         kwargs or None. """
        # TODO:
        # The filters should be case insensitive
        for field, value in kwargs.items():
            ObjectClass.add_query_filter(field, "=", value)
        entity = ObjectClass.fetch(limit=1)
        return entity[0]

    def add_object(self, ObjectClass, **kwargs):
        """ Create an Entity with the fields specified in kwargs. """
        entity = ObjectClass(**kwargs)
        entity.put()
        return entity

    def update_object(self, entity, **kwargs):
        """ Update an Entity with the fields specified in kwargs. """
        entity.update(**kwargs)
        return entity

    def delete_object(self, entity):
        """ Delete and Entity. """
        return entity.delete(entity.id)

    def commit(self):
        """ Should commit a session connection to the DataStore. """
        pass
