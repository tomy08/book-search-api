from fastapi import FastAPI
from routers.books import book_router
from routers.user import user_router
from db.database import create_database


app = FastAPI()
app.title = "Book API"
app.version = "0.0.1"

create_database()

app.include_router(book_router)
app.include_router(user_router)


