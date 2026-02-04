# main.py
from controller import BookController

def main():
    controller = BookController()
    
    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            controller.add_book(title, author)
        elif choice == '2':
            controller.show_books()
        elif choice == '3':
            title = input("Enter book title to delete: ")
            controller.remove_book(title)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()