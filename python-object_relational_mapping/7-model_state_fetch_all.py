#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    username = argv[0]
    password = argv[1]
    data = argv[2]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, data,
                                   pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
