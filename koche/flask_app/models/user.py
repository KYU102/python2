from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.magazine import Magazine

import re	# the regex module
# create a regular expression object that we'll use later  
USER_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = 'magazine_schema'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.magazines = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_all(cls,data):
        query = "SELECT * FROM users"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def is_valid(user):
        is_valid = True
        if len(user['first_name']) < 3:
            is_valid = False
            flash("First name must be at least 3 characters.")
        if len(user['last_name']) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters.")
        if not USER_REGEX.match(user['email']): 
            flash("Invalid user address!")
            is_valid = False
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.")
        if user['password'] != user['confirm']:
            is_valid = False
            flash("Passwords do not match!")
        return is_valid

    @staticmethod
    def user_is_valid(user):
        is_valid = True
        if len(user['first_name']) < 3:
            is_valid = False
            flash("First name must be at least 3 characters.")
        if len(user['last_name']) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters.")
        if not USER_REGEX.match(user['email']): 
            flash("Invalid user address!")
            is_valid = False
        return is_valid

    @classmethod
    def getUsers(cls, data):
        query = "SELECT * FROM users LEFT JOIN magazines ON magazines.user_id = users.id WHERE users.id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        dojo = cls(result[0])
        for magazine in result:
            magazine_data = {
                'id': magazine['magazines.id'],
                'title': magazine['title'],
                'description': magazine['description'],
                'created_at': magazine['magazines.created_at'],
                'updated_at': magazine['magazines.updated_at'],
                'user_id': magazine['user_id'],
                'first_name' : magazine['first_name']
                }
            dojo.magazines.append(Magazine(magazine_data))
            
        return dojo

            # ! READ/RETRIEVE ALL
    @classmethod
    def get_all_with_user(cls) -> list:
        query = "SELECT users.first_name, magazines.* FROM magazines JOIN users ON users.id = magazines.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        # results will be a list of dictionaries
        magazines = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            magazines.append( cls(dictionary) )
            # adding an instance of the thought class to the thoughts list
        return magazines

