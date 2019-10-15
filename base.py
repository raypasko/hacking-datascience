# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Hmm... the database `sqlalchemy` does not exist
engine = create_engine('postgresql://postgres:docker@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)

Base = declarative_base()

