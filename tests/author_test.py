"""Test functions for GoodreadsAuthor"""

from nose.tools import ok_
from tests import client_test
from goodreads.author import GoodreadsAuthor

def author_test():
    """Test for getting an author"""
    client = client_test.make_client()
    author = client.author(1406384)
    ok_(isinstance(author, GoodreadsAuthor))
    ok_(isinstance(book, GoodreadsBook) for book in author.books)
