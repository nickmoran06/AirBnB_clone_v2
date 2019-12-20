#!/usr/bin/python3
"""
This is the state class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref='state')

    @property
    def cities(self):
        """
        Getter cities
        """
        dic = models.storage.all(City)
        Mylist = []
        for key, val in dic.items():
            if val.state_id == self.id:
                Mylist.append(val)
        return(Mylist)
