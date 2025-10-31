from author import Author
from book import Book


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book_by_info(self, title, author_name, author_nationality):
        author = Author(author_name, author_nationality)
        new_book = Book(title, author)
        self.books.append(new_book)

    def add_book(self, book: Book):
        self.books.append(book)

    def show_books(self):
        print(f"Books in {self.name}:")
        for b in self.books:
            print(f"- {b.title} by {b.author.name}")

    def find_books_by_author(self, name):
        return [b for b in self.books if b.author.name == name]

    def remove_book(self, title):
        for i, b in enumerate(self.books):
            if b.title == title:
                del self.books[i]
                return True
        return False

    def count_books(self):
        return len(self.books)

if __name__ == "__main__":
    author1 = Author("Robert Martin", "USA")
    author2 = Author("Luciano Ramalho", "Brazil")

    book1 = Book("Clean Code", author1)
    book2 = Book("Fluent Python", author2)

    library = Library("ATU Digital Library")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book_by_info("Python 101", "Michael Driscoll", "USA")

    library.show_books()
    print("Found:", library.find_books_by_author("Robert Martin"))
    print("Count:", library.count_books())
    print("Remove Clean Code:", library.remove_book("Clean Code"))
    library.show_books()

