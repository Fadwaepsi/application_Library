#Book : Représente un livre avec un titre et un auteur.
#Library : Gère une collection de livres et permet d'ajouter, de retirer et de rechercher des livres.


# Code à tester
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"