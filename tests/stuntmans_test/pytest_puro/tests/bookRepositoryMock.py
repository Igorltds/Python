from datetime import date
from src.book import Book
from src.bookRepository import BookRepository

class BookRepositoryMock(BookRepository):
    def __init__(self):
        self.__count = 0
        self.__book = Book('111', 'pythonfor beginners', 50.0, date.today())
    
    def get_book(self, id:str)->Book:
        self.__count += 1
        return self.__book
    
    def get_count(self):
        return self.__count