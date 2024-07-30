#!/usr/bin/python3
"""Defines the FileStorage engine."""
import json
from models.base_model import BaseModel
from models.state import State

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
                for key, val in objs.items():
                    class_name = key.split('.')[0]
                    self.__objects[key] = eval(class_name)(**val)
        except FileNotFoundError:
            pass

    def close(self):
        """Deserialize JSON file to objects."""
        self.reload()

