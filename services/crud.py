from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import  UserBookRating , Book as  BookModel
from schemas.books import Book as BookSchema, UserBookRating as UserBookRatingSchema
from sqlalchemy import or_

# Book table

def get_books(db: Session, title: str = None, author: str = None, year: str = None):
    filters = []

    if title:
        filters.append(BookModel.Book_Title.ilike(f'%{title}%'))
    if author:
        filters.append(BookModel.Book_Author.ilike(f'%{author}%'))
    if year:
        filters.append(BookModel.Year_Of_Publication == year)

    if filters:
        query = db.query(BookModel).filter(or_(*filters))
    else:
        query = db.query(BookModel)
    
    return query.all()

def get_book_by_isbn(db: Session, ISBN: str):
    return db.query(BookModel).filter(BookModel.ISBN == ISBN).first()

def create_book(db: Session, book: BookModel):
    try:
        db.add(book)
        db.commit()
        db.refresh(book)
        return {"message": "Book added successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Book already exists")
    

def update_book(db: Session, ISBN: str, book: BookModel):
    # Intenta encontrar el libro en la base de datos
    existing_book = db.query(BookModel).filter(BookModel.ISBN == ISBN).first()

    # Si el libro no existe, levanta una excepción
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")

    try:
        # Actualiza los atributos del libro existente con los nuevos valores
        existing_book.Book_Title = book.Book_Title
        existing_book.Book_Author = book.Book_Author
        existing_book.Publisher = book.Publisher
        existing_book.Year_Of_Publication = book.Year_Of_Publication

        # Guarda los cambios en la base de datos
        db.commit()
        return {"message": "Book updated successfully"}
    except Exception as e:
        print(e)
        # Si ocurre algún error, realiza un rollback de la transacción y levanta una excepción
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update book")


def delete_book(db: Session, ISBN: str):
    book = db.query(BookModel).filter(BookModel.ISBN == ISBN).first()
    if book:
        db.delete(book)
        db.commit()

# UserBookRating table

def get_book_ratings(db: Session, ISBN: str):
    return db.query(UserBookRating).filter(UserBookRating.ISBN == ISBN).all()

def rate_book(db: Session, ISBN: str, rating: UserBookRatingSchema):
    db.add(rating)
    db.commit()
    db.refresh(rating)
    return rating
