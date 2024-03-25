# FastAPI Book API

This is an API developed with FastAPI to manage a collection of books. It allows performing CRUD (Create, Read, Update, Delete) operations on the books.

## Installation

1. Clone this repository:

```sh
git clone https://github.com/tomy08/book-search-api
```

2. Navigate to the project directory:

```sh
cd book-search-api
```

3. Create a virtual environment:

```sh
python3 -m venv env
```

4. Activate the virtual environment:

- For Windows:

```sh
source ./env/Scripts/activate
```

- For Unix/Mac:

```sh
source ./env/bin/activate
```

5. Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

1. Run the application:

```sh
uvicorn main:app --reload
```

2. Access the interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

## Endpoints

- `GET /books/`: Get all books or filter by title, author, or year.
- `GET /books/{ISBN}/`: Get a book by its ISBN.
- `POST /books/`: Create a new book.
- `PUT /books/{ISBN}/`: Update an existing book.
- `DELETE /books/{ISBN}/`: Delete a book by its ISBN.
- `GET /books/{ISBN}/ratings/`: Get all ratings for a book by its ISBN.
- `POST /books/{ISBN}/ratings/`: Add a new rating for a book by its ISBN.
- `POST /login/`: Log in and get an authentication token.
