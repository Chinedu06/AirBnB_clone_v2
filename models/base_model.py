#!/usr/bin/python3
"""BaseModel module"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import datetime

Base = declarative_base()

class BaseModel:
    """A base class for all models with common attributes"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def save(self):
        """Save the object to the database"""
        # Implement the save method (you will likely need to add this to your DBStorage class)
        pass

    def to_dict(self):
        """Convert the object to a dictionary"""
        # Implement the conversion to dictionary (you will likely need to add this to your DBStorage class)
        pass

    def __str__(self):
        """Return a string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

