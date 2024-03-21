from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models.books import Book, UserBookRating

book_router = APIRouter()

books_db = []
ratings_db = []


@book_router.get("/books", response_model=List[Book])
async def search_books(title: Optional[str] = None, author: Optional[str] = None, year: Optional[str] = None):
    filtered_books = books_db
    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book.Book_Title.lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book.Book_Author.lower()]
    if year:
        filtered_books = [book for book in filtered_books if year == book.Year_Of_Publication]
    return filtered_books

@book_router.get("/books/{ISBN}", response_model=Book)
async def get_book_by_isbn(ISBN: str):
    for book in books_db:
        if book.ISBN == ISBN:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.post("/books", response_model=Book)
async def create_book(book: Book):
    books_db.append(book)
    return book

@book_router.put("/books/{ISBN}", response_model=Book)
async def update_book(ISBN: str, book: Book):
    for i, book in enumerate(books_db):
        if book.ISBN == ISBN:
            books_db[i] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.delete("/books/{ISBN}")
async def delete_book(ISBN: str):
    for i, book in enumerate(books_db):
        if book.ISBN == ISBN:
            del books_db[i]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")


@book_router.get("/books/{ISBN}/ratings", response_model=List[UserBookRating])
async def get_book_ratings(ISBN: str):
    return [rating for rating in ratings_db if rating.ISBN == ISBN]

@book_router.post("/books/{ISBN}/ratings", response_model=UserBookRating)
async def rate_book(ISBN: str, rating: UserBookRating):
    ratings_db.append(rating)
    return rating
