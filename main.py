from fastapi import FastAPI


app = FastAPI()
app.title = "Book API"
app.version = "0.0.1"


@app.get("/")
def root():
    return {"message": "Hello World"}
