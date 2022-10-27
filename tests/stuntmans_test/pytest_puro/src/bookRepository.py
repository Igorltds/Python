from src.book import Book
from abc import ABCMeta, abstractmethod

class BookRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_book(self, id:str) -> Book:
        pass
    