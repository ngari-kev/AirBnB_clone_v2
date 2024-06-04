#!/usr/bin/python3
'''This is the new storage engine'''
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage():
    '''Defines the DBStorage engine'''
    __engine = None
    __session = None

    def __init__(self):
        '''Defines a new instance'''
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if (env == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query all objects depending on class name'''
        my_dict = {}

        if (cls is None):
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        for a_class in classes:
            objs = self.__session.query(a_class).all()

            for obj in objs:
                cls_name = obj.__class__.__name__
                obj_id = obj.id
                key = "{}.{}".format(cls_name, obj_id)

                my_dict[key] = obj

        return (my_dict)

    def new(self, obj):
        '''adds obj to current db session'''
        self.__session.add(obj)

    def save(self):
        '''commits changes staged in current db session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Deletes obj from db if not none'''
        if (obj):
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        '''Creates all tables in the db and initializes a new session'''
        Base.metadata.create_all(self.__engine)

        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session()

    def close(self):
        """Calls remove() method:
        On the private session attribute (self.__session)
        or close() on the class Session."""
        self.__session.remove()
