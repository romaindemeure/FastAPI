# This file database.py it's used for create a connection on our database

# We need all these imports to make it work
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create database
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# create_engine for use database with database url and connect arguments
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Local class which is going to be an instance of a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This Base it's used for create each model of database
Base = declarative_base()
