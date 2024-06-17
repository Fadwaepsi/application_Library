import pytest
from ..library.book import Book
from ..library.library import Library

def test_library_integration():
    # Création de la bibliothèque
    library = Library()

    # Création des livres
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    # Ajout des livres à la bibliothèque
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Vérification que les livres ont été ajoutés
    assert len(library.books) == 3
    assert library.find_book_by_title("The Great Gatsby") == book1
    assert library.find_book_by_title("1984") == book2
    assert library.find_book_by_title("To Kill a Mockingbird") == book3

    # Suppression d'un livre
    library.remove_book(book2)
    assert len(library.books) == 2
    assert library.find_book_by_title("1984") is None

    # Liste des livres
    books_list = library.list_books()
    assert books_list == ["The Great Gatsby by F. Scott Fitzgerald", "To Kill a Mockingbird by Harper Lee"]

#pytest.raises est une fonctionnalité de pytest qui permet de vérifier 
# qu'une exception spécifique est levée dans un bloc de code.
def test_remove_nonexistent_book():
    library = Library()
    book = Book("1984", "George Orwell")
    with pytest.raises(ValueError, match="Book not found in the library"):
        library.remove_book(book)

def test_find_nonexistent_book():
    library = Library()
    book = library.find_book_by_title("Nonexistent Book")
    assert book is None
