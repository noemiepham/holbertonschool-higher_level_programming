#!/usr/bin/python3
"""Write a python file that contains the class definition
 of a State and an instance Base = declarative_base():"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represent a city for a MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
   id (sqlalchemy.Integer): The state's id.
   name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
