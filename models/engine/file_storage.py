#!/usr/bin/python3
"""
Serializes instances to JSON file and deserializes JSON file to instances
"""
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and ...
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        k = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[k] = obj

    def save(self):
        """
        serialising FileStroage.__objects
        """
        with open(FileStorage.__file_path, 'w+') as i:
            dicobj = {}
            for k, val in FileStorage.__objects.items():
                dicobj[k] = val.to_dict()
            json.dump(dicobj, i)

    def reload(self):
        """
        deserializes instances from json file
        """
        try:
            with open(FileStorage.__file_path, 'r') as i:
                dictobj = json.loads(i.read())
                from models.base_model import BaseModel
                Classes = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'Place': Place,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Review': Review
                }
                for k, val in dicobj.items():
                    clas = val.get('__class__')
                    if clas in Classes:
                        FileStorage._objects[k] = Classes[clas](**val)

        except FileNotFoundError:
            pass
