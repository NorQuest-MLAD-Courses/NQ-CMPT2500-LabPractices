class Movie:
    """
     Represents a movie with its details.
    """

    def __init__(self, title:str, genre:str, year:int):
        """
        Initialize the Movie object with a title, genre, and year.
        Arguments:
        title: Title of the movie
        genre: Genre of the movie
        year: Year the movie was released.
        """
        self.title = title
        self.genre = genre
        self.year = year

    def display_movie(self) -> str:
        """
        Display the movie's details.
        :return: A formatted string representing the movie details.
        """
        return f"Title: {self.title}, genre: {self.genre}, year: {self.year}"

class MovieManager:
    """
    Manages a collection of movies.
    """
    
    def __init__(self):
        """
        Initialize with an empty list of movies.
        """
        self.movies = []
    
    def add_movie(self, title:str, genre: str, year:int) -> None:
        """
        Add a new movie.
        Arguments:
        movie: Movie to be added.
        """
        movie = Movie(title, genre, year)
        self.movies.append(movie)
        print("Movie added.")
    
    def view_movies(self) -> None:
        """
        Display all movies.
        """
        for index, movie in enumerate(self.movies):
            print(f"{index}:" + movie.display_movie())
    
    def delete_movie(self, index: int) -> None:
        """
        Remove a movie by its index.
        Arguments:
        index: The index of the movie to be removed.
        """
        try: # Handle user supplying invalid index
            self.movies.pop(index)
            print(f"Movie index {index} removed.")
        except IndexError:
            print("Invalid index.")

def main():
    manager = MovieManager()

    while True:
        print("\n--- Movie Management System ---")
        print("1. Add a Movie")
        print("2. View Movies")
        print("3. Delete a Movie")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            year = input("Enter release year: ")
            manager.add_movie(title, genre, year)
        elif choice == "2":
            manager.view_movies()
        elif choice == "3":
            manager.view_movies()
            index = int(input("Enter the number of the movie to delete: "))
            manager.delete_movie(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()