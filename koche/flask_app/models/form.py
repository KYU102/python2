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

    # @classmethod
    # def get_all_with_employee(cls) -> list:
    #     query = "SELECT employees.first_name, forms.* FROM forms JOIN employees ON employee.id = forms.employee_id;"
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     # results will be a list of dictionaries
    #     forms = []
    #     for dictionary in results:
    #         # dictionary is a dictionary in the list
    #         forms.append( cls(dictionary) )
    #         # adding an instance of the thought class to the thoughts list
    #     return forms

    @classmethod
    def get_by_all(cls,data):
        query = "SELECT * FROM employees"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_all_forms_for_emp(cls,data) -> list:
        # query = "SELECT * FROM forms JOIN employees ON emplopyees.id = forms.employee_id;"
        query = "SELECT * FROM forms WHERE forms.employee_id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        # results will be a list of dictionaries
        forms = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            forms.append( cls(dictionary) )
            # adding an instance of the thought class to the thoughts list
        return forms
    
    @classmethod
    def get_one_form(cls,data):
        query  = "SELECT * FROM forms WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

