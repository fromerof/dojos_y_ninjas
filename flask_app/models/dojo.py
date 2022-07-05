from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,created_at,updated_at) VALUES (%(name)s,NOW(),NOW())"
        return connectToMySQL('esquema_dojos_y_ninja').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db =  connectToMySQL('esquema_dojos_y_ninja').query_db(query)
        dojos =[]
        for d in dojos_from_db:
            dojos.append(cls(d))
        return dojos


    @classmethod
    def getDojo_withNinja(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on ninjas.dojo_id = dojos.id where dojos.id = %(id)s;"
        results = connectToMySQL('esquema_dojos_y_ninja').query_db( query , data )    
        dojo = cls( results[0] )
        for row in results:
            ninja_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age": row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"]
            }
            dojo.ninjas.append( Ninja( ninja_data ) )
        return dojo