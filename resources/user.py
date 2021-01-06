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
            
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        table_values = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(
            table_values, (data["username"], data["password"])
        )

        connection.commit()
        connection.close()

        return {
            "message": "User created sccessfully"
        }, 201