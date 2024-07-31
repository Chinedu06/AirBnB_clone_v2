#!/usr/bin/python3
"""
Module for DBStorage class
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
# other imports


class DBStorage:
    """DBStorage class manages storage of hbnb models in MySQL database"""

    # existing code

    def close(self):
        """Call remove() methodontheprivatesessionattribute (self.__session)"""
        self.__session.remove()
