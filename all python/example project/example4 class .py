
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
        return None  # If no book with the title is found



library = Library()


library.add_book(Book("Python 101", "John Doe", 3))
library.add_book(Book("Data Science Handbook", "Jane Smith", 5))


print("Books in the Library:")
library.list_books()


print("\nSearching for 'Python 101':")
book = library.find_book_by_title("Python 101")
if book:
    print(f"Found: {book}")
else:
    print("Book not found.")


print("\nSearching for 'Nonexistent Book':")
book = library.find_book_by_title("Nonexistent Book")
if book:
    print(f"Found: {book}")
else:
    print("Book not found.")
