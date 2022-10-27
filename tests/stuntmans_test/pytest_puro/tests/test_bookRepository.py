#from sys import path
#path.insert(1, '/home/home/luaa/projects/python/tests/stuntman_test/pytest_puro')

from src.book import Book
from BookRepositoryMock import BookRepositoryMock

import pytest


@pytest.fixture
def bookRepository():
    return BookRepositoryMock()

def test_add_book(bookRepository):
    bookRepository.add_book('111', 'python for beginners', 50.0)

def test_get_book(bookRepository):
    book = bookRepository.get_book('None')
    assert book.title == 'test'
    
def test_get_book_id(bookRepository):
    bookRepository.add_book('111', 'python for beginners', 50.0)
    book = bookRepository.get_book('111')

#def test_get_book_id_not_found(bookRepository):
#    with pytest.raises(Exception):  #ExceptionBooknotfound
#        bookRepository.add_book('111', 'python for beginners', 50.0)
#        bookRepository.get_book('111')

def test_get_books(bookRepository):
    assert len(bookRepository.get_books()) == 1

def test_get_count(bookRepository):
    assert bookRepository.get_count() == (0, 0)
