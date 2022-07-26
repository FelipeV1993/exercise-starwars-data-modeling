import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False,)
    email = Column(String(250), nullable=False, unique=True)
    name = Column(String(250), )
    last_name = Column(String(250), )


# id init pk
# usser_name string unique
# password string
# email string
# name string NULL 
# last_name string NULL 

class People(Base):
    __tablename__ = 'People'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    People_id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False, unique=True)
    height = Column(Integer, nullable=False,)
    mass = Column(Integer, nullable=False,)
    hair_color = Column(String(250), )
    skin_color = Column(String(250), )
    eye_color = Column(String(250), )
    birth_year = Column(String(250), )
    gender = Column(String(250), )

# People
# -
# People_id PK int
# Name varchar(200) UNIQUE 
# height int
# mass int
# hair_color string NULL 
# skin_color string
# eye_color string
# birth_year string
# gender string NULL 

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    Planet_id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False, unique=True)
    rotation_period = Column(Integer, nullable=False,)
    orbital_period = Column(Integer, nullable=False,)
    diameter = Column(Integer, nullable=False,)
    climate = Column(String(250), )
    gravity = Column(String(250), )
    terrain = Column(String(250), )
    surface_water = Column(Integer, nullable=False,)

# Planets
# -
# Planet_id PK int
# Name varchar(200) UNIQUE
# rotation_period int
# orbital_period int
# diameter int
# climate string
# gravity string
# terrain string
# surface_water init

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    Vehicles_id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False, unique=True)
    model = Column(String(250), )
    manufacturer = Column(String(250), )
    cost_in_credits = Column(Integer, nullable=False,)
    length = Column(Integer, nullable=False,)
    max_atmosphering_speed = Column(Integer, nullable=False,)
    crew = Column(Integer, nullable=False,)
    passengers = Column(Integer, nullable=False,)

# Vehicles
# -
# Vehicles_id PK int FK 
# Name varchar(200) UNIQUE
# model string
# manufacturer string
# cost_in_credits int
# length init
# max_atmosphering_speed init
# crew init
# passengers init



# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.

    user_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    planets_id = Column(Integer, ForeignKey('Planets.Planet_id'))
    vehicles_id = Column(Integer, ForeignKey('Vehicles.Vehicles_id'))
    people_id = Column(Integer, ForeignKey('People.People_id'))

    def to_dict(self):
        return {}

# user_id FK >- User.id pk init
# planets_id FK >- Planets.Planet_id pk init
# vehicles_id FK >- Vehicles.Vehicles_id pk init
# people_id FK >- People.People_id pk init

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')