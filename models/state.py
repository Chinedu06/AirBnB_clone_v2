#!/usr/bin/python3
"""
Module for State class
"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """State class for storing state information"""

    # existing code

    @property
    def cities(self):
        """ReturnsTheListOfCityObjectsFromStorageLinkedToTheCurrentState"""
        if models.storage_type != 'db':
`            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
