#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''Represents the amenity class'''
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = Table('place_amenity', Base.metadata,
                            Column('amenity_id', String(60),
                                   ForeignKey('amenities.id'),
                                   primary_key=True),
                            Column('place_id', String(60),
                                   ForeignKey('places.id'),
                                   primary_key=True))

    places = relationship("Place", secondary=place_amenities, viewonly=False)
