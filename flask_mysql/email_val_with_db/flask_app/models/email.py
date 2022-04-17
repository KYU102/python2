from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT into emails (email) VALUES (%(email)s);"
        return connectToMySQL('email_schema').query_db(query,data)

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_schema').query_db(query)
        emails = []
        for row in results:
            emails.append( cls(row) )
        return emails

    @staticmethod
    def is_valid(email):
        is_valid = True
        if len(email['email']) < 3:
            is_valid = False
            flash("Email must be at least 3 characters.")
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid