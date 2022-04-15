from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

DATABASE = 'checklist'

class Dojo:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
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

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def getNinjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id=%(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo = cls(result[0])
        for ninja in result:
            ninja_data = {
                'id': ninja['ninjas.id'],
                'first_name': ninja['first_name'],
                'last_name': ninja['last_name'],
                'age': ninja['age'],
                'created_at': ninja['ninjas.created_at'],
                'updated_at': ninja['ninjas.updated_at'],
                'dojo_id': ninja['dojo_id']
                }
            dojo.ninjas.append(Ninja(ninja_data))
            
        return dojo