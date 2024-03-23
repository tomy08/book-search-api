from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from models.books import Book, BookUpdate, UserBookRating
from utils.token_manager import validate_api_key

book_router = APIRouter()

books_db = [
    Book(ISBN="978-0-671-71245-7", Book_Title="The Catcher in the Rye", Book_Author="J.D. Salinger", Year_Of_Publication=1951, Publisher="Little, Brown", Image_URL_S="http://images.amazon.com/images/P/0671712457.01.THUMBZZZ.jpg", Image_URL_M="http://images.amazon.com/images/P/0671712457.01.MZZZZZZZ.jpg", Image_URL_L="http://images.amazon.com/images/P/0671712457.01.LZZZZZZZ.jpg"),
]
ratings_db = [
    UserBookRating(User_ID=1, ISBN="978-0-671-71245-7", Book_Rating=4),
    UserBookRating(User_ID=2, ISBN="978-0-671-71245-7", Book_Rating=5),
    UserBookRating(User_ID=3, ISBN="978-0-671-71245-7", Book_Rating=3),
    UserBookRating(User_ID=4, ISBN="978-0-671-71245-7", Book_Rating=2),
    UserBookRating(User_ID=5, ISBN="978-0-671-71245-7", Book_Rating=1),
]


@book_router.get("/books", response_model=List[Book],tags=["books"])
async def search_books(title: Optional[str] = None, author: Optional[str] = None, year: Optional[str] = None):
    filtered_books = books_db
    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book.Book_Title.lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book.Book_Author.lower()]
    if year:
        filtered_books = [book for book in filtered_books if year == book.Year_Of_Publication]
    if not filtered_books:
        raise HTTPException(status_code=404, detail="No books found")
    return filtered_books


@book_router.get("/books/{ISBN}", response_model=Book,tags=["books"])
async def get_book_by_isbn(ISBN: str):
    for book in books_db:
        if book.ISBN == ISBN:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.post("/books", response_model=Book,tags=["books"])
async def create_book(book: Book, api_key: str = Depends(validate_api_key)):
    books_db.append(book)
    return book

@book_router.put("/books/{ISBN}", response_model=Book, tags=["books"])
async def update_book(ISBN: str, book_data: BookUpdate, api_key: str = Depends(validate_api_key)):
    for book_db in books_db:
        if book_db.ISBN == ISBN:
            for key, value in book_data.model_dump(exclude_unset=True).items():
                if value:
                    setattr(book_db, key, value)
        
            return book_db
    
    raise HTTPException(status_code=404, detail="Book not found")

@book_router.delete("/books/{ISBN}",tags=["books"])
async def delete_book(ISBN: str, api_key: str = Depends(validate_api_key)):
    for i, book in enumerate(books_db):
        if book.ISBN == ISBN:
            del books_db[i]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")


@book_router.get("/books/{ISBN}/ratings", response_model=List[UserBookRating],tags=["books"])
async def get_book_ratings(ISBN: str):
    return [rating for rating in ratings_db if rating.ISBN == ISBN]

@book_router.post("/books/{ISBN}/ratings", response_model=UserBookRating,tags=["books"])
async def rate_book(ISBN: str, rating: UserBookRating, api_key: str = Depends(validate_api_key)):
    ratings_db.append(rating)
    return rating
