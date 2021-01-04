from flask import Flask, request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

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
        item = self.find_item_by_name(name)
        if item:
            return item
        else:
            return {
                'message': "Item not found"
            }, 404

    @classmethod
    def find_item_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        create_input = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(create_input, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {
                'Item':
                {"name": row[0],
                "price": row[1]
                }
            }

    def post(self, name):
        if self.find_item_by_name(name):
            return {'message': "item '{}' already exists".format(name)}, 400

        data = ItemsInShop.parser.parse_args()
        item = {'name': name, 'price': data['price']}

        try:
            self.insert_item(item)
        except:
            return {
                "message": "An error occured while inserting item"
            }, 500

        return item, 201
    
    @classmethod
    def insert_item(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES(?,?)"
        cursor.execute(query, (item["name"], item["price"]))

        connection.commit()
        connection.close()
    
    def delete(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        return {'message': 'Item deleted!'}
    
    def put(self, name):
        data = ItemsInShop.parser.parse_args()

        item = self.find_item_by_name(name)
        updated_item = {'name': name, 'price': data['price']}

        if item is None:
            self.insert_item(updated_item)
        else:
            item.update(updated_item)

        return updated_item, 201
    
    @classmethod
    def update(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()

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