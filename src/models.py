import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personjes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personaje = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    color_de_ojos = Column(String(250), nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250)
    population = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
  
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    mail= Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Favoritos(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250)
    planeta_id = Column(String(250), nullable=False)
    persona_id = Column(String(250), nullable=False)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')