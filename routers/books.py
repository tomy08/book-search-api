from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from schemas.books import Book,  UserBookRating
from db.models import Book as BookModel
from utils.token_manager import validate_api_key
from db.database import SessionLocal
from services import crud


book_router = APIRouter()



@book_router.get("/books", response_model=List[Book], tags=["books"])
async def search_books(title: Optional[str] = None, author: Optional[str] = None, year: Optional[str] = None):
    db = SessionLocal()
    return crud.get_books(db, title, author, year)

@book_router.get("/books/{ISBN}", response_model=Book, tags=["books"])
async def get_book_by_isbn(ISBN: str):
    db = SessionLocal()
    book = crud.get_book_by_isbn(db, ISBN)
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@book_router.post("/books", tags=["books"])
async def add_book(book: Book, api_key: str = Depends(validate_api_key)):
    new_book = BookModel(**book.model_dump())
    db = SessionLocal()           
    return crud.create_book(db, new_book)



@book_router.put("/books/{ISBN}", tags=["books"])
async def update_book(ISBN: str, book: Book, api_key: str = Depends(validate_api_key)):
    new_book = BookModel(**book.model_dump())
    db = SessionLocal()
    return crud.update_book(db, ISBN, new_book)

@book_router.delete("/books/{ISBN}", tags=["books"])
async def delete_book(ISBN: str, api_key: str = Depends(validate_api_key)):
    db = SessionLocal()
    crud.delete_book(db, ISBN)
    return {"message": "Book deleted successfully"}

@book_router.get("/books/{ISBN}/ratings", response_model=List[UserBookRating], tags=["books"])
async def get_book_ratings(ISBN: str):
    db = SessionLocal()
    return crud.get_book_ratings(db, ISBN)

@book_router.post("/books/{ISBN}/ratings", response_model=UserBookRating, tags=["books"])
async def rate_book(ISBN: str, rating: UserBookRating, api_key: str = Depends(validate_api_key)):
    db = SessionLocal()
    return crud.rate_book(db, ISBN, rating)
