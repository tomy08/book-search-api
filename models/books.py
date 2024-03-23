from pydantic import BaseModel, AnyHttpUrl
from typing import Optional

class Book(BaseModel):
    ISBN: str
    Book_Title: str
    Book_Author: str
    Year_Of_Publication: int
    Publisher: str
    Image_URL_S: AnyHttpUrl
    Image_URL_M: AnyHttpUrl
    Image_URL_L: AnyHttpUrl

class BookUpdate(BaseModel):
    ISBN: Optional[str] = None
    Book_Title: Optional[str] = None
    Book_Author: Optional[str] = None
    Year_Of_Publication: Optional[int] = None
    Publisher: Optional[str] = None
    Image_URL_S: Optional[AnyHttpUrl] = None
    Image_URL_M: Optional[AnyHttpUrl] = None
    Image_URL_L: Optional[AnyHttpUrl] = None

class UserBookRating(BaseModel):
    User_ID: int
    ISBN: str
    Book_Rating: int
