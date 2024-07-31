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

    __engine = None
    __session = None

    # existing code ...

    def close(self):
        """
        Call remove() method on the private
        session attribute (self.__session)
        """
        self.__session.remove()

    def reload(self):
        """Create all tables in the database and start a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(session_factory)
