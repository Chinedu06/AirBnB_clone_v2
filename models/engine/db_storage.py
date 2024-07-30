#!/usr/bin/python3
"""Defines the DBStorage engine."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
import os

class DBStorage:
    """Database storage engine for MySQL database."""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage."""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, db))

    def all(self, cls=None):
        """Query on the current database session."""
        if cls:
            return self.__session.query(cls).all()
        else:
            # Implement code to return all objects
            pass

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload data from the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current session."""
        self.__session.remove()

