class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None  # Return None if no book with the given title is found

# Example Usage
library = Library()
library.add_book(Book("Python 101", "John Doe", 3))
library.add_book(Book("Data Science Handbook", "Jane Smith", 5))

# List all books
print("List of Books in Library:")
library.list_books()

# Finding a book by title
print("\nFinding a book by title:")
book = library.find_book_by_title("Python 101")
if book:
    print(f"Found: {book}")
else:
    print("Book not found.")

# Trying to find a book that doesn't exist
print("\nFinding a non-existent book:")
book = library.find_book_by_title("Non-Existent Book")
if book:
    print(f"Found: {book}")
else:
    print("Book not found.")
