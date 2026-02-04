# view.py

class BookView:
    """
    BookView class handles the display of books to the user.
    """

    def display_books(self, books:list[dict]) -> None:
        """ Displays the list of books """
        if not books:
            print("No books available.")
            return
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}")
        
    def display_message(self, message:str) -> None:
        """ Displays a message to the user """
        print(message)