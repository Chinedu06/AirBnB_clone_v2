#!/usr/bin/python3
"""
Module that defines the FileStorage class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing)
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, obj in obj_dict.items():
                    self.__objects[key] = eval(obj['__class__'])(**obj)
        except FileNotFoundError:
            pass

    def close(self):
        """
        Call reload() method for deserializing the JSON file to objects
        """
        self.reload()
