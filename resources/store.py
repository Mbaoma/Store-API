from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_item_by_name(name)
        if store:
            return store.json
        else:
            return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_item_by_name(name):
            return {'message': f'A store with that name, {name} exists'}, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
            return {'message': 'Store created'}, 200
        except:
            return {'message': 'An error occured while creating store'}, 500
        
    def delete(self, name):
        store = StoreModel.find_item_by_name()
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self):
        stores = StoreModel.query.all()
        return {
        'stores': [store.json() for store in stores]
        }