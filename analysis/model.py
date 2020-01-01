from . import mongo


class MongoDb:
    _table_name = 'trademon'

    def get_all(self):
        return list(mongo.db[self._table_name].find())

    def insert(self, data):
        mongo.db[self._table_name].insert(data)
