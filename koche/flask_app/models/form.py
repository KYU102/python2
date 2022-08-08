from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'koche_schema'

class Form:
    def __init__(self,data):
        self.id = data['id']
        self.close_contact = data['close_contact']
        self.exposure_date = data['exposure_date']
        if 'first_name' in data:
            self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.employee_id = data['employee_id']


    @classmethod
    def saveForm(cls,data):
        query = "INSERT INTO forms (close_contact, exposure_date, employee_id) VALUES (%(close_contact)s,%(exposure_date)s, %(employee_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
