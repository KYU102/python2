from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'thoughts_schema'

class Thought:
    def __init__(self,data):
        self.id = data['id']
        self.thought = data['thought']
        self.users_id = data['users_id']
        self.likes = data['likes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def saveThought(cls,data):
        query = "INSERT INTO thoughts (thought, users_id, likes) VALUES (%(thought)s, 1, %(likes)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_thoughts(cls):
        query = "SELECT * FROM thoughts;"
        results = connectToMySQL(DATABASE).query_db(query)
        thoughts = []
        for thought in results:
            thoughts.append( cls(thought) )
        return thoughts

    @classmethod
    def get_all_thoughts_with_user(cls):
        query = "SELECT user.first_name, thoughts.* FROM thoughts JOIN users ON users.id = thoughts.users_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        thoughts = []
        for thought in results:
            thoughts.append( cls(thought) )
        return thoughts

    @classmethod
    def get_one_thought(cls,data):
        query  = "SELECT * FROM thoughts WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE thoughts SET thought=%(thought)s,likes=%(1)s WHERE id = %(id)s;"

        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM thoughts WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)


    @staticmethod
    def thought_is_valid(thought):
        is_valid = True
        if len(thought['thought']) < 3:
            is_valid = False
            flash("Thought must be at least 3 characters.")
        return is_valid

        @classmethod
    def like(cls,data):
        query = "UPDATE thoughts SET thought=%(thought)s,likes=%(likes)s+1 WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)