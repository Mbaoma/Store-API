import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegistration
from resources.items import ItemsInShop, ItemsList
from resources.store import StoreList, Store
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'hard-to-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(ItemsInShop, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegistration, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if  __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
