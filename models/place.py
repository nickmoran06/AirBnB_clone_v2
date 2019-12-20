#!/usr/bin/python3
"""
This is the place class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from models.review import Review
import os

place_amenity = Table("place_amenity", Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False),
                      )


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    data = os.getenv('HBNB_TYPE_STOGAGE')
    if data == 'db':
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)

    @property
    def reviews(self):
        """
        Getter attribute to return list of Review instances
        """
        Mylist = []
        Ins_Review = models.storage.all(Review)
        for ins in Ins_Review:
            if ins.place_id == self.id:
                Mylist.append(ins)

        return (Mylist)

    @property
    def amenities(self):
        """
        Getter attribute to return list of Amenity instance
        """
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
        """
        Getter attribute to return list of Amenity instance
        """
        if type(obj) is Amenity and obj.id not in self.amenity_ids:
            self.amenity_ids.append(Amenity.id)
