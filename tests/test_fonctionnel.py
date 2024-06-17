import pytest 
from ..library.book import Book
from ..library.library import Library

@pytest.fixture
def library_with_books():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    return library

def test_add_book(library_with_books):
    assert len(library_with_books.books) == 3
    new_book = Book("Animal Farm", "George Orwell")
    library_with_books.add_book(new_book)
    assert len(library_with_books.books) == 4
    assert library_with_books.find_book_by_title("Animal Farm") == new_book

def test_remove_book(library_with_books):
    initial_count = len(library_with_books.books)
    book_to_remove = library_with_books.find_book_by_title("1984")
    library_with_books.remove_book(book_to_remove)
    assert len(library_with_books.books) == initial_count - 1
    assert library_with_books.find_book_by_title("1984") is None

def test_find_book_by_title(library_with_books):
    found_book = library_with_books.find_book_by_title("The Great Gatsby")
    assert found_book is not None
    assert found_book.title == "The Great Gatsby"

def test_find_nonexistent_book(library_with_books):
    found_book = library_with_books.find_book_by_title("Nonexistent Book")
    assert found_book is None

def test_list_books(library_with_books):
    books_list = library_with_books.list_books()
    assert len(books_list) == len(library_with_books.books)
    assert "The Great Gatsby by F. Scott Fitzgerald" in books_list
    assert "1984 by George Orwell" in books_list
    assert "To Kill a Mockingbird by Harper Lee" in books_list
