#!/usr/bin/python3
"""
    a script that lists all State
    objects from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
        script takes 3 arguments:
        mysql username,
        mysql password and database name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()

    states = session.query(State).order_by(State.id).all()
    [print('{}: {}'.format(state.id, state.name)) for state in states]

    session.close()
