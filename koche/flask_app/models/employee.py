from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.form import Form

import re	# the regex module
# create a regular expression object that we'll use later  
EMPLOYEE_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = 'koche_schema'

class Employee:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.forms = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO employees (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM employees WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching employee
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_all(cls,data):
        query = "SELECT * FROM employees"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE employees SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def is_valid(employee):
        is_valid = True
        if len(employee['first_name']) < 3:
            is_valid = False
            flash("First name must be at least 3 characters.")
        if len(employee['last_name']) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters.")
        if not EMPLOYEE_REGEX.match(employee['email']): 
            flash("Invalid employee address!")
            is_valid = False
        if len(employee['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.")
        if employee['password'] != employee['confirm']:
            is_valid = False
            flash("Passwords do not match!")
        return is_valid

    @staticmethod
    def employee_is_valid(employee):
        is_valid = True
        if len(employee['first_name']) < 3:
            is_valid = False
            flash("First name must be at least 3 characters.")
        if len(employee['last_name']) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters.")
        if not EMPLOYEE_REGEX.match(employee['email']): 
            flash("Invalid employee address!")
            is_valid = False
        return is_valid

    @classmethod
    def getEmployees(cls, data):
        query = "SELECT * FROM employees LEFT JOIN forms ON forms.employee_id = employees.id WHERE employees.id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        dojo = cls(result[0])
        for form in result:
            form_data = {
                'id': form['forms.id'],
                'close_contact': form['close_contact'],
                'exposure_date': form['exposure_date'],
                'created_at': form['forms.created_at'],
                'updated_at': form['forms.updated_at'],
                'employee_id': form['employee_id'],
                'first_name' : form['first_name']
                }
            dojo.forms.append(Form(form_data))
            
        return dojo

    #         # ! READ/RETRIEVE ALL
    @classmethod
    def get_all_with_employee(cls) -> list:
        query = "SELECT employees.first_name, forms.* FROM forms JOIN employees ON employees.id = forms.employee_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        # results will be a list of dictionaries
        forms = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            forms.append( cls(dictionary) )
            # adding an instance of the thought class to the thoughts list
        return forms

