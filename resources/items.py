from flask import Flask, request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item_model import ItemModel

class ItemsInShop(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
                            'price',
                            type=float,
                            required=True,
                            help='Must not be left blank'
        )
    data = parser.parse_args

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return item.json()
        else:
            return {
                'message': "Item not found"
            }, 404

    
    def post(self, name):
        if ItemModel.find_item_by_name(name):
            return {'message': "item '{}' already exists".format(name)}, 400

        data = ItemsInShop.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            return {
                "message": "An error occured while inserting item"
            }, 500

        return item.json(), 201
        
    def delete(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted!'}
    
    def put(self, name):
        data = ItemsInShop.parser.parse_args()

        item = ItemModel.find_item_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']
        item.save_to_db()
            
        return item.json(), 201
    

class ItemsList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []

        for i in result:
            items.append({
                'item name': i[0],
                'price': i[1]
            })

        connection.close()
        return {
            'Items': items
        }, 200