# controller.py

from model import BookModel
from view import BookView

class BookController:
    """
    BookController class manages the interaction between the model and the view.
    """
    def __init__(self):
        """
        Initializes the BookController with a model and a view.
        """
        self.model = BookModel()
        self.view = BookView()

    def add_book(self, title: str, author: str):
        """
        Adds a book to the model.
        """
        self.model.add_book(title, author)
        self.view.display_message(f'Book "{title}" by {author} added.')

    def show_books(self):
        """
        Retrieves books from the model and updates the view.
        """
        books = self.model.get_books()
        self.view.display_books(books)

    def remove_book(self, title: str):
        """
        Deletes a book from the model and updates the view.
        """
        if self.model.delete_book(title):
            self.view.display_message(f'Book "{title}" removed.')
        else:
            self.view.display_message(f'Book "{title}" not found.') 