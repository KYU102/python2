from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'checklist'

class Dojo:
    def __init__(self, data:dict) -> None:
        self.id = data['dojo_id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def saveDojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result