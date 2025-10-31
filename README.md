1. author.py
📘 Презентациядағы нұсқа
class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

💎 Жетілдірілген нұсқа
class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __repr__(self):
        return f"Author(name={self.name!r}, nationality={self.nationality!r})"

🔍 Айырмашылығы
Презентациядағы	Жетілдірілген
Тек ат пен елін сақтайды	__repr__ әдісі қосылды – объект экранда әдемі шығады
Шығару функциясы жоқ	print() кезінде автор туралы толық мәлімет көруге болады
🧩 2. book.py
📘 Презентациядағы нұсқа
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

💎 Жетілдірілген нұсқа
from author import Author

class Book:
    def __init__(self, title, author: Author):
        self.title = title
        self.author = author  # агрегация – дайын Author объектісі беріледі

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author.name!r})"

🔍 Айырмашылығы
Презентациядағы	Жетілдірілген
Author класы импортталмаған	from author import Author қосылды
Автор жай айнымалы	Типизация арқылы Author деп нақты көрсетілді
Нәтижені көрсету әдісі жоқ	__repr__ арқылы кітап атауы мен автор аты көрсетіледі
Түсініктеме жоқ	Комментарий арқылы агрегация түсіндірілді
🧩 3. library.py
📘 Презентациядағы нұсқа
from author import Author
from book import Book

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book_by_info(self, title, author_name, author_nationality):
        author = Author(author_name, author_nationality)
        book = Book(title, author)
        self.books.append(book)

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for b in self.books:
            print(f"{b.title} by {b.author.name}")

💎 Жетілдірілген нұсқа
from author import Author
from book import Book

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book_by_info(self, title, author_name, author_nationality):
        author = Author(author_name, author_nationality)  # композиция
        new_book = Book(title, author)
        self.books.append(new_book)

    def add_book(self, book: Book):  # агрегация
        self.books.append(book)

    def show_books(self):
        print(f"Books in {self.name}:")
        for b in self.books:
            print(f"- {b.title} by {b.author.name}")

    # Қосымша әдістер:
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

🔍 Айырмашылығы
Презентациядағы нұсқа	Жетілдірілген нұсқа
Тек кітап қосу мен көрсету бар	Қосымша әдістер: find_books_by_author, remove_book, count_books
Ішкі байланыстар түсіндірілмеген	Комментарийлер арқылы композиция мен агрегация түсіндірілді
Бағдарламаны тікелей іске қосу мүмкін емес	if __name__ == "__main__": қосылып, тікелей орындалады
Шығару қарапайым	Кітаптар мен авторлар ретімен, анық форматта көрсетіледі
Тапсырманың тек негізгі бөлігі бар	Менің нұсқамда негізгі + қосымша тапсырма бар
📊 Қорытынды
Файл	Презентациядағы	Жетілдірілген
author.py	Тек деректер сақтайды	Объектті әдемі басып шығару әдісі бар
book.py	Қарапайым класс	Импорт, типизация, түсіндірме және __repr__ қосылды
library.py	Негізгі әдістер	Қосымша әдістер, комментарийлер, нақты жұмыс үлгісі қосылды
💬 Қысқаша қорытынды

🔹 Презентациядағы код — теориялық мысал, тек негізгі ұғымды (композиция, агрегация) көрсетуге арналған.
🔹 Менің нұсқам — жұмыс істейтін толық нұсқа, яғни:

VS Code ішінде бірден іске қосылады,

Барлық тапсырмаларды орындайды (кітап қосу, іздеу, жою, санау),

Лабораторияны қорғауға дайын толық мысал.
