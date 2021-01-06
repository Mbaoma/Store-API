import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type = str,
        required= True,
        help="must not be left blank"
    )
    
    parser.add_argument(
        "password",
        type = str,
        required= True,
        help="must not be left blank"
    )

    def post(self):
        data = UserRegistration.parser.parse_args()

        #check for duplicate usernames
        if UserModel.search_by_username(data["username"]):
            return {
                "message": "Username already exists"
            }, 400
            
        user = UserModel(**data)
        user.save_to_db()

        return {
            "message": "User created sccessfully"
        }, 201