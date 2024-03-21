from fastapi import FastAPI, HTTPException, Query
from routers.books import book_router


app = FastAPI()
app.title = "Book API"
app.version = "0.0.1"

app.include_router(book_router)


