#!/usr/bin/python3
"""stores objects created"""
import json, os
from models.base_model import(BaseModel)


class FileStorage(BaseModel):
    """creates class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary object"""
        return self.__objects
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        json.dumps(self.__objects)

    def reload(self):
        """deserializes the JSON file to __objects"""
        Check = os.path.exists(self.__file_path)
        if Check is True:
            self.__objects = json.loads(self.__file_path)




