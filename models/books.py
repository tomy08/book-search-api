from pydantic import BaseModel, AnyHttpUrl

class Book(BaseModel):
    ISBN: str
    Book_Title: str
    Book_Author: str
    Year_Of_Publication: str
    Publisher: str
    Image_URL_S: AnyHttpUrl
    Image_URL_M: AnyHttpUrl
    Image_URL_L: AnyHttpUrl

class UserBookRating(BaseModel):
    User_ID: int
    ISBN: str
    Book_Rating: int
