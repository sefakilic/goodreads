"""Test functions for GoodreadsBook"""

from nose.tools import ok_
from tests import client_test
from goodreads.book import GoodreadsBook

def book_test():
    """Test for getting a book"""
    client = client_test.make_client()
    book = client.book(50)
    ok_(isinstance(book, GoodreadsBook))
    ok_(book.id)
