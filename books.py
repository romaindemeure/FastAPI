from enum import Enum

from fastapi import FastAPI

app = FastAPI()


BOOKS = {
    "book_1": {"title": "Title One", "author": "Author One"},
    "book_2": {"title": "Title Two", "author": "Author Two"},
    "book_3": {"title": "Title Three", "author": "Author Three"},
    "book_4": {"title": "Title Four", "author": "Author Four"},
    "book_5": {"title": "Title Five", "author": "Author Five"},
}


# get it's for see all books at "/" with optional parameter "skip_book"
@app.get("/")
async def read_all_books(skip_book: str | None = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


# get it's for see one book with the book name at "/{book_name}"
@app.get("/{book_name}")
async def read_books(book_name: str):
    return BOOKS[book_name]


# post it's for create book with book_title and book_author, the book_name id it's automatically create
@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0

    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x

    BOOKS[f'book_{current_book_id + 1}'] = {'title': book_title, 'author': book_author}
    return BOOKS[f'book_{current_book_id + 1}']


# put it's for update book_title and book_author with specific book_name id
@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {'title': book_title, 'author': book_author}
    BOOKS[book_name] = book_information
    return book_information


# delete it's for delete data with the book_name id
@app.delete("/{book_name}")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book_{book_name} deleted.'
