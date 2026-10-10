
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"

        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)
        print("-" * 30)


books = {}


def add_book():
    try:
        book_id = int(input("Enter book ID: "))

        if book_id in books:
            print("Book ID already exists!")
            return

        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()

        if not title or not author:
            print("Title and author cannot be empty!")
            return

        book = Book(book_id, title, author)
        books[book_id] = book

        print("Book added successfully!")

    except ValueError:
        print("Please enter a valid numeric book ID.")


def view_books():
    if not books:
        print("No books available.")
        return

    for book in books.values():
        book.display()


def search_book():
    try:
        book_id = int(input("Enter book ID to search: "))

        if book_id in books:
            books[book_id].display()
        else:
            print("Book not found!")

    except ValueError:
        print("Please enter a valid numeric book ID.")


def borrow_book():
    try:
        book_id = int(input("Enter book ID to borrow: "))

        if book_id not in books:
            print("Book not found!")
        elif books[book_id].available:
            books[book_id].available = False
            print("Book borrowed successfully!")
        else:
            print("This book is already borrowed.")

    except ValueError:
        print("Please enter a valid numeric book ID.")


def return_book():
    try:
        book_id = int(input("Enter book ID to return: "))

        if book_id not in books:
            print("Book not found!")
        elif not books[book_id].available:
            books[book_id].available = True
            print("Book returned successfully!")
        else:
            print("This book was not borrowed.")

    except ValueError:
        print("Please enter a valid numeric book ID.")


def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
