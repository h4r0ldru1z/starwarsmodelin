import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    
class FavoritePlanets(Base):
    __tablename__ = 'favoriteplanets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey("planets.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    galaxy = Column(String, nullable=False)
    empire_ally = Column(String, nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    race = Column(String, nullable=False)
    language = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    
class FavoriteCharacter(Base):
    __tablename__ = 'favoritecharacter'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')