import datetime 
from src.book import Book
from src.bookRepository import BookRepository

class BookRepositoryMock(BookRepository):
    def __init__(self):
        self.__books = {}
        self.__book_count = 0
        self.__books_count = 0
        self.add_book()

    def add_book(self, id="None", title='test', price=0.0, date=datetime.date.today()):
        self.__books[id] = Book(id, title, price, date)

    def get_book(self, id:str) -> Book:
        self.__book_count += 1
        try: return self.__books[id]
        except: raise Exception #ExceptionBookmarknotfound 

    def get_books(self):
        self.__books_count += 1
        return self.__books
            
    def get_count(self):
        return self.__book_count, self.__books_count
