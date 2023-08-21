#!/usr/bin/python3
"""
    a script that prints the State object
    with the name passed as argument
    from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    """
        script takes 4 arguments:
        mysql username,
        mysql password,
        database name and the name of the state
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()

    state_name = argv[4]
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print('{}'.format(state.id))
    else:
        print("Not found")
    session.close()
