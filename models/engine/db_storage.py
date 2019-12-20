#!/usr/bin/python3
"""
module to the class DBStorage
"""
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
import os


class DBStorage():
    """
    Class DBstorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor of DBstorage
        """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password,
            host, database), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Dictionary to show objects of the classes
        """
        if cls:
            my_dict = {}
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                my_dict[key] = obj

            return my_dict
        else:
            my_dict = {}
            classes = [City, State, User, Place, Review, Amenity]
            for val in classes:
                query = self.__session.query(val)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    my_dict[key] = obj

            return my_dict

    def new(self, obj):
        """
        Add the object to the session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Save changes in the session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        reloads data
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()
