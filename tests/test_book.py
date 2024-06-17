import pytest
from ..library.book import Book 
# Importer la classe Book

# Pour vérifier que les attributs title et author sont correctement initialisés
# vérifie le nom de l'auteur F. Scott et le titre du roman The Great Gatsby
def test_initialization():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    assert book.title == "The Great Gatsby"
    assert book.author == "F. Scott Fitzgerald"

# vérifie que la méthode __str__ retourne la chaîne de caractères formatée correctement.
def test_str_method():
    book = Book("1984", "George Orwell")
    assert str(book) == "1984 by George Orwell"