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
        self.desk_id = data['desk_id']
        if 'title' in data:
            self.title = data['title']


    @classmethod
    def savePerf(cls,data):
        query = "INSERT INTO peripherals (name, link, price, theme) VALUES (%(name)s,%(link)s,%(price)s,%(theme)s);"
        return connectToMySQL(DATABASE).query_db(query,data)