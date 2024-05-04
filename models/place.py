#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)

    @property
    def reviews(self):
        """Getter attribute to retrieve reviews from FileStorage."""
        rev_list = []
        rev_dict = storage.all(Review)
        for rev in rev_dict.values():
            if rev.place_id == self.id:
                rev_list.append(rev)
        return rev_list

    @property
    def amenities(self):
        """Getter attribute for amenities"""
        amenities_list = []
        for amenity_id in self.amenity_ids:
            amenity = storage.get('Amenity', amenity_id)

        if amenity:
            amenities_list.append(amenity)
        return amenities_list

    @amenities.setter
    def amenities(self, amenity):
        """setter attribute for amenities"""
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
