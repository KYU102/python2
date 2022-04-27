from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.desk import Desk

import re	# the regex module
# create a regular expression object that we'll use later  
USER_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = 'desk_schema'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.desks = []
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
        if len(user['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters.")
        if not USER_REGEX.match(user['email']): 
            flash("Invalid user address!")
            is_valid = False
        return is_valid

    @classmethod
    def getUsers(cls, data):
        query = "SELECT * FROM users LEFT JOIN desks ON desks.user_id = users.id WHERE users.id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        dojo = cls(result[0])
        for desk in result:
            desk_data = {
                'id': desk['desks.id'],
                'title': desk['title'],
                'description': desk['description'],
                'created_at': desk['desks.created_at'],
                'updated_at': desk['desks.updated_at'],
                'user_id': desk['user_id'],
                'first_name' : desk['first_name']
                }
            dojo.desks.append(Desk(desk_data))
            
        return dojo

            # ! READ/RETRIEVE ALL
    @classmethod
    def get_all_with_user(cls) -> list:
        query = "SELECT users.first_name, desks.* FROM desks JOIN users ON users.id = desks.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        # results will be a list of dictionaries
        desks = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            desks.append( cls(dictionary) )
            # adding an instance of the thought class to the thoughts list
        return desks

