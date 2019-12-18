#!/usr/bin/python3

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

classes = {"City": City, "State": State}


class DBStorage():
    """Class DBstorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Constructor of DBstorage
        """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = db.create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password,
            host, database, pool_pre_ping=True))

        conection = self.__engine.connect()
        metadata = db.MetaData()
        if env == "test":
            db.drop_all(tables)

    def all(self, cls=None):
        """Dictionary to show objects of the classes
        """
        MyDict = {}
        for i in classes:
            if cls in classes or cls in classes[i] or cls is None:
                objects = self.__session.query(classes[i]).all()
                for obj in objects:
                    key = obj.__class__.__name__ + "." + obj.id
                    MyDict[key] = obj
        return(MyDict)

    def new(self, obj):
        """Add the object to the session
        """
        self.__session.add(obj)

    def save(self):
        """Save changes in the session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__engine = Session
