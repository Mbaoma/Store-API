import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def search_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user =  cls(*row)
        else:
            user =  None 
        
        connection.close()
        return user

    @classmethod
    def search_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id, ))
        row = result.fetchone()
        if row:
            user =  cls(*row)
        else:
            user =  None 
        
        connection.close()
        return user

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
        if User.search_by_username(data["username"]):
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