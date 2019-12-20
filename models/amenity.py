#!/usr/bin/python3
"""
This is the amenity class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity
#import os


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    #data = os.getenv('HBNB_TYPE_STORAGE')
    #if data == 'db':
    place_amenities = relationship("Place", secondary=place_amenity)
