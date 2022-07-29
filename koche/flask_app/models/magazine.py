from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'magazine_schema'

class Magazine:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.user_id = data['user_id']
        if 'first_name' in data:
            self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def saveMagazine(cls,data):
        query = "INSERT INTO magazines (title, description,user_id) VALUES (%(title)s,%(description)s,%(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_magazines(cls):
        query = "SELECT * FROM magazines;"
        results = connectToMySQL(DATABASE).query_db(query)
        magazines = []
        for magazine in results:
            magazines.append( cls(magazine) )
        return magazines

    @classmethod
    def get_one_magazine_with_user(cls,data):
        query  = "SELECT * FROM magazines WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_one_magazine(cls,data):
        query  = "SELECT * FROM magazines WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE magazines SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s,under30=%(under30)s WHERE id = %(id)s;"

    #     return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM magazines WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)


    @staticmethod
    def magazine_is_valid(magazine):
        is_valid = True
        if len(magazine['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters.")
        if len(magazine['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters.")
        return is_valid


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

