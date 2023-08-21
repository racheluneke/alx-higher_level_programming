#!/usr/bin/python3
"""
    a python file that contains the class
    definition of a State and an instance
    Base = declarative_base():
"""
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        class for states:
        __tablename__ = states
        id = integer auto generated
        name = name of state and cannot be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
