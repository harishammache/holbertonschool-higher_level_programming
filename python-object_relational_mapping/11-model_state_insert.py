#!/usr/bin/python3
""" adds the State object “Louisiana”"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    data = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, data),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
