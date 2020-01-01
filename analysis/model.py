from bson.objectid import ObjectId

from . import mongo


class MongoDb:
    _table_name = 'trademon'

    def get_all(self):
        return list(mongo.db[self._table_name].find())

    def insert(self, data):
        mongo.db[self._table_name].insert(data)

    def update(self, ob_id, data):
        mongo.db[self._table_name].update({'_id': ObjectId(ob_id)}, {'$set': data})

    def delete(self, ob_id):
        mongo.db[self._table_name].remove({"_id": ObjectId(ob_id)})
