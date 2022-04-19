from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re	# the regex module
# create a regular expression object that we'll use later  
USER_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = 'users_schema'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

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
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])

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
        if len(user['password']) < 3:
            is_valid = False
            flash("Password must be at least 3 characters.")
        if user['password'] != user['confirm']:
            is_valid = False
            flash("Passwords do not match!","register")
        return is_valid