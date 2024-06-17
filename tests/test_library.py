import pytest
from ..library.library import Library
from ..library.book import Book

def test_add_book():
    library = Library()
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(book)
    assert book in library.books


# crée un nouvel objet Book avec le titre et l'auteur. 
# Cet objet représente le livre que nous allons ajouter puis supprimer de la bibliothèque.
# Appelle la méthode 'add_book' de l'instance 'library', ajoutant ainsi l'objet 'book' à la liste des livres de la bibliothèque.
# l'assertion verifie que book n'est plus présent dans la liste library.books. 
# Si book a été correctement supprimé, l'assertion passera sans erreur. 
# Si book est toujours dans la liste, l'assertion échouera et le test échouera également.
def test_remove_book():
    library = Library()
    book = Book("1984", "George Orwell")
    library.add_book(book)
    library.remove_book(book)
    assert book not in library.books

# Pareil comme test-remove-book
def test_remove_book_not_found():
    library = Library()
    book = Book("1984", "George Orwell")
    with pytest.raises(ValueError, match="Book not found in the library"):
        library.remove_book(book)

def test_find_book_by_title():
    library = Library()
    book = Book("To Kill a Mockingbird", "Harper Lee")
    library.add_book(book)
    found_book = library.find_book_by_title("To Kill a Mockingbird")
    assert found_book == book

def test_find_book_by_title_not_found():
    library = Library()
    book = library.find_book_by_title("Nonexistent Book")
    assert book is None

def test_list_books():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)
    books_list = library.list_books()
    assert books_list == ["The Great Gatsby by F. Scott Fitzgerald", "1984 by George Orwell"]