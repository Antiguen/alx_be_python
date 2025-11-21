class Book:
    """Represents a book with a title, author, and availability status."""
    
    def __init__(self, title, author):
        """Initializes a Book object."""
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute for encapsulation
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available if checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available (not checked out)."""
        return not self._is_checked_out
    
    def __str__(self):
        """User-friendly representation for printing."""
        return f"{self.title} by {self.author}"
    
class Library:
    """Manages a collection of Book objects."""
    
    def __init__(self):
        """Initializes the library with an empty list of books."""
        # Private list to store Book objects (composition/encapsulation)
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)
            # print(f"Added: {book.title}") # Optional confirmation
        else:
            print("Error: Only Book objects can be added to the library.")

    def _find_book(self, title):
        """Helper method to find a book by its title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        """Checks out a book by title, if it's available."""
        book = self._find_book(title)
        if book:
            if book.is_available():
                book.check_out()
                return True
            else:
                print(f"'{title}' is already checked out.")
                return False
        else:
            print(f"Error: Book titled '{title}' not found in library.")
            return False

    def return_book(self, title):
        """Returns a book by title, if it was checked out."""
        book = self._find_book(title)
        if book:
            if not book.is_available():
                book.return_book()
                return True
            else:
                # This handles cases where someone tries to return an already available book
                print(f"'{title}' was not checked out.")
                return False
        else:
            print(f"Error: Book titled '{title}' not found in library.")
            return False

    def list_available_books(self):
        """Prints the title and author of all available books."""
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book) # Uses the Book's __str__ method
                available_count += 1
        
        if available_count == 0:
            print("No books are currently available.")

