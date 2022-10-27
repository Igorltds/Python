from pytest import fixture, raises
from unittest.mock import Mock

from src.book import Book
from datetime import date


class ExceptionBookNotfound(Exception):
    pass


@fixture
def book(id='0000',title='test book', price=0.0, publication_date=date.today()):
    return Book(id, title, price, publication_date)

def test_get_book_id(book):
    bookRepository = Mock() #Mock

    bookRepository.get_book.return_value=book
    bookRepository.get_count.return_value=1

    book_test = bookRepository.get_book()
    assert book_test.id == book.id
 
    assert bookRepository.get_count() == 1


def test_get_book_id_not_found():
    bookRepository = Mock()
    bookRepository.get_book.side_effect=ExceptionBookNotfound
    
    with raises(ExceptionBookNotfound):
        bookRepository.get_book()