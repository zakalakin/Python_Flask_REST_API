from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel


class Items(Resource):
    @jwt_required()
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('qty',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item must be associated with a store!")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": f"Item with name {name} already exists"}, 400

        data = Item.parser.parse_args()  # request.get_json()

        item = ItemModel(name, data["qty"], data["store_id"])

        try:
            print("saving to db...")
            item.save_to_db()
            print("saved to fb..")
        except:
            return {"message": "An error occurred when inserting item"}, 500

        return item.json(), 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()  # request.get_json()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data["qty"], data["store_id"])
        else:
            item.qty = data["qty"]

            item.save_to_db()
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)

        if item is not None:
            item.delete_from_db()

        return {"message": f"'{name}' has been removed from the items table"}
