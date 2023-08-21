#!/usr/bin/python3
"""
    a Python file similar to model_state.py
    named model_city.py that contains the class
    definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
        inherits from Base (imported from model_state)
        links to the MySQL table cities
        class attribute id
        class attribute name
        class attribute state_id
    """
    __tablename__ = "cities"
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False,)
