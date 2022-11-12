#!/usr/bin/python3
"""Write a script that deletes all State objects with a name
 containing the letter a from the database hbtn_0e_6_usa"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.like('%a%')).all()
    for state in state:
        session.delete(state)
    session.commit()
