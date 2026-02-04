# model.py
class BookModel:
    """
    BookModel class stores books 
    in memory and provides methods to add, retrieve, and delete books.
    """
    def __init__(self):
        """
        Initializes the BookModel with an empty list of books.
        """
        # List of books
        self.books = []
    
    def add_book(self, title:str, author:str) -> None:
        """ Adds a book"""
        self.books.append({"title": title, "author": author})
    
    def get_books(self) -> list[dict]:
        """ Returns the list of books """
        return self.books

    def delete_book(self, title:str) -> bool:
        """ Deletes a book by title """
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                return True
        return False    
