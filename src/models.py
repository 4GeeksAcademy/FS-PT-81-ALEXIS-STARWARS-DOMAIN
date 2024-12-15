import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class Users(Base):
        __tablename__ = 'users'
        id= Column(Integer, primary_key=True)
        email = Column(String, nullable=False, unique=True)
        password= Column(String,nullable= False)
        city= Column(String)
        address= Column(String)

class Favorites(Base):
        __tablename__='favorites'
        id=Column(Integer, primary_key=True)
        user_id=Column(Integer, ForeignKey('users.id'))
        user= relationship('users', backref='favorites')

def to_dict(self):
          return{
                'id':self.id,
                'email':self.email,
                'city':self.city,
                'address':self.address
          }
class Characters(Base):
          __tablename__='characters'
          id=Column(Integer, primary_key=True)
          name=Column(String)
          gender=Column(String)
          birthday=Column(Integer)
          description=Column(Integer)
          user_id=Column(Integer, ForeignKey('users.id'))
          user=relationship('users', backref='characters')
          favorites_id=Column(String, ForeignKey('favorites.id'))
          favorites=relationship('favorites', backref='characters')

class Planets(Base):
          __tablename__='planets'
          id=Column(Integer, primary_key=True)
          name=Column(String, nullable=False)
          terraine=Column(String)
          clima=Column(String)
          user_id=Column(Integer, ForeignKey('users.id'))
          user=relationship('users', backref='planets')
          favorites_id=Column(String, ForeignKey('favorites.id'))
          favorites=relationship('favorites', backref='planets')
class Starships(Base):
          __tablename__='starships'
          id=Column(Integer, primary_key=True)
          name=Column(String, nullable=False)
          cosumables=Column(String)
          model=Column(String)
          user_id=Column(Integer, ForeignKey('users.id'))
          user=relationship('users', backref='starships')
          favorites_id=Column(String, ForeignKey('favorites.id'))
          favorites=relationship('favorites', backref='starships')





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
