from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'recipes_schema'

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under30 = data['under30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def saveRecipe(cls,data):
        query = "INSERT INTO recipes (name, under30, description, instructions, date_made, user_id) VALUES (%(name)s, %(under30)s, %(description)s, %(instructions)s, %(date_made)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_one_recipe(cls,data):
        query  = "SELECT * FROM recipes WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s WHERE id = %(id)s;"

        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)


    @staticmethod
    def recipe_is_valid(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters.")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters.")
        if recipe['date_made'] == False:
            is_valid = False
            flash("Date made required")
        return is_valid