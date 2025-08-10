# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        """Initialize the Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Readable representation of the Book."""
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize the EBook with title, author, and file size in MB."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Readable representation of the EBook."""
        return f"'{self.title}' by {self.author} [EBook, {self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize the PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Readable representation of the PrintBook."""
        return f"'{self.title}' by {self.author} [PrintBook, {self.page_count} pages]"


class Library:
    def __init__(self):
        """Initialize an empty Library."""
        self.books = []

    def add_book(self, book: Book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)
