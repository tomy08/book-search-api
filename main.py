from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from models.books import Book, UserBookRating


app = FastAPI()
app.title = "Book API"
app.version = "0.0.1"

books_db = []
ratings_db = []


@app.get("/books", response_model=List[Book])
async def search_books(title: Optional[str] = None, author: Optional[str] = None, year: Optional[str] = None):
    filtered_books = books_db
    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book.Book_Title.lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book.Book_Author.lower()]
    if year:
        filtered_books = [book for book in filtered_books if year == book.Year_Of_Publication]
    return filtered_books

@app.get("/books/{ISBN}", response_model=Book)
async def get_book_by_isbn(ISBN: str):
    for book in books_db:
        if book.ISBN == ISBN:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
async def create_book(book: Book):
    books_db.append(book)
    return book

@app.put("/books/{ISBN}", response_model=Book)
async def update_book(ISBN: str, book: Book):
    for i, book in enumerate(books_db):
        if book.ISBN == ISBN:
            books_db[i] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{ISBN}")
async def delete_book(ISBN: str):
    for i, book in enumerate(books_db):
        if book.ISBN == ISBN:
            del books_db[i]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

