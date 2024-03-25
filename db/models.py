import uuid

from sqlalchemy import ForeignKey,Column, Integer, String,MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

class Book(Base):
    __tablename__ = 'books'
    ISBN = Column(String, primary_key=True)
    Book_Title = Column(String)
    Book_Author = Column(String)
    Year_Of_Publication = Column(Integer)
    Publisher = Column(String)
    Image_URL_S = Column(String)
    Image_URL_M = Column(String)
    Image_URL_L = Column(String)

class UserBookRating(Base):
    __tablename__ = 'user_book_ratings'
    id = Column(Integer, primary_key=True)
    User_ID = Column(Integer)
    ISBN = Column(String, ForeignKey('books.ISBN'))
    Book_Rating = Column(Integer)



