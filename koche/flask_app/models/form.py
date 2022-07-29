from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'koche_schema'

class Form:
    def __init__(self,data):
        self.id = data['id']
        self.close_contact = data['close_contact']
        self.exposure_date = data['exposure_date']
        self.employee_id = data['employee_id']
        if 'first_name' in data:
            self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def saveForm(cls,data):
        query = "INSERT INTO forms (close_contact, exposure_date,employee_id) VALUES (%(close_contact)s,%(exposure_date)s,%(employee_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    # @classmethod
    # def get_all_forms(cls):
    #     query = "SELECT * FROM forms;"
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     forms = []
    #     for form in results:
    #         forms.append( cls(form) )
    #     return forms

    # @classmethod
    # def get_one_form_with_user(cls,data):
    #     query  = "SELECT * FROM forms WHERE id = %(id)s";
    #     result = connectToMySQL(DATABASE).query_db(query,data)
    #     return cls(result[0])

    # @classmethod
    # def get_one_form(cls,data):
    #     query  = "SELECT * FROM forms WHERE id = %(id)s";
    #     result = connectToMySQL(DATABASE).query_db(query,data)
    #     return cls(result[0])

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE forms SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s,under30=%(under30)s WHERE id = %(id)s;"

    #     return connectToMySQL(DATABASE).query_db(query,data)


    # @classmethod
    # def delete(cls,data):
    #     query = "DELETE FROM forms WHERE id = %(id)s"
    #     return connectToMySQL(DATABASE).query_db(query,data)


    # @staticmethod
    # def form_is_valid(form):
    #     is_valid = True
    #     if len(form['title']) < 3:
    #         is_valid = False
    #         flash("Title must be at least 3 characters.")
    #     if len(form['description']) < 3:
    #         is_valid = False
    #         flash("Description must be at least 3 characters.")
    #     return is_valid


            # ! READ/RETRIEVE ALL
    # @classmethod
    # def get_all_with_user(cls) -> list:
    #     query = "SELECT users.first_name, forms.* FROM forms JOIN users ON users.id = forms.user_id;"
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     # results will be a list of dictionaries
    #     forms = []
    #     for dictionary in results:
    #         # dictionary is a dictionary in the list
    #         forms.append( cls(dictionary) )
    #         # adding an instance of the thought class to the thoughts list
    #     return forms

