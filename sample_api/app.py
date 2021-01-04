from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from user import UserRegistration
from items import ItemsInShop, ItemsList
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'hard-to-guess'
api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(ItemsInShop, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegistration, '/register')

if  __name__ == '__main__':
    app.run(port=5000, debug=True)
