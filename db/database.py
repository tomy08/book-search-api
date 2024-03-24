from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import path

from db.models import UserBookRating, Book

sqlite_file_name = "../database.sqlite"
base_dir = path.dirname(path.realpath(__file__))

database_url = f"sqlite:///{path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url,echo=True)
SessionLocal = sessionmaker(engine)

Base = declarative_base()

def create_database():
    Base.metadata.create_all(bind=engine)
