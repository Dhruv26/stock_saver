from . import mongo


class MongoDb:
    _table_name = 'trademon'

    def insert(self, data):
        mongo.db[self._table_name].insert(data)
