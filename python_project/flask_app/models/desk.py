from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'desk_schema'

class Desk:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.user_id = data['user_id']
        if 'first_name' in data:
            self.first_name = data['first_name']


    @classmethod
    def saveDesk(cls,data):
        query = "INSERT INTO desks (title, description, user_id) VALUES (%(title)s,%(description)s,%(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_desks(cls):
        query = "SELECT * FROM desks;"
        results = connectToMySQL(DATABASE).query_db(query)
        desks = []
        for desk in results:
            desks.append( cls(desk) )
        return desks

    @classmethod
    def get_one_desk_with_user(cls,data):
        query  = "SELECT * FROM desks WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_one_desk(cls,data):
        query  = "SELECT * FROM desks WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE desks SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s,under30=%(under30)s WHERE id = %(id)s;"

    #     return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM desks WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)


    @staticmethod
    def desk_is_valid(desk):
        is_valid = True
        if len(desk['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters.")
        if len(desk['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters.")
        return is_valid


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

