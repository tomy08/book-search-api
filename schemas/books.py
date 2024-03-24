from pydantic import BaseModel, AnyHttpUrl
from typing import Optional

class Book(BaseModel):
    ISBN: str
    Book_Title: str
    Book_Author: str
    Year_Of_Publication: int
    Publisher: str
    Image_URL_S: str
    Image_URL_M: str
    Image_URL_L: str


class UserBookRating(BaseModel):
    User_ID: int
    ISBN: str
    Book_Rating: int
