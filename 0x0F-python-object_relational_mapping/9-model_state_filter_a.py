#!/usr/bin/python3
"""Task 9 lists all State objects containing the letter a from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query_restult = session.query(State).filter(State.name.like("%a%")).all()
    for state in query_restult:
        print(f"{state.id}: {state.name}")
