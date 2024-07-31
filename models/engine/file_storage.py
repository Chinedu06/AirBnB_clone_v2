#!/usr/bin/python3
"""
Module for FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
# other imports


class FileStorage:
    """FileStorage class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    # existing code ...

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
