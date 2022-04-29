from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'desk_schema'


class Peripheral:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.link = data['link']
        self.price = data['price']
        self.theme = data['theme']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.desk_id = session['desk_id']



    @classmethod
    def savePerf(cls,data):
        query = "INSERT INTO peripherals (name, link, price, theme, desk_id) VALUES (%(name)s,%(link)s,%(price)s,%(theme)s,%(desk_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)