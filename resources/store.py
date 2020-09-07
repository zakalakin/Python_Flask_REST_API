from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.store import StoreModel


class Stores(Resource):
    @jwt_required()
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}


class Store(Resource):
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {"message": "Store not found"}, 404

    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": f"A store with name '{name}' already exists"}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "Error occurred while creating the store"}, 500
        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": "Store deleted"}, 200
