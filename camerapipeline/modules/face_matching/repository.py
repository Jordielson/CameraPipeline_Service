import os
import tinydb
from tinydb import Query

class FaceMatchingRespository():
    def __init__(self):
        """
        Create an environment variable in your .env file with the name FACE_MATCHING_DB_PATH 
        that specifies the folder of the file to database.
        """
        self.db = tinydb.TinyDB(os.environ["FACE_MATCHING_DB_PATH"])
        self.face_matching_query = Query()
        

    def register(self, data: dict):
        self.db.insert(data)
        return data

    def all(self):
        return self.db.all()

    def get(self, name):
        return self.db.search(self.face_matching_query.name == name)