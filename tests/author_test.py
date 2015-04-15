"""Test functions for GoodreadsAuthor"""

from nose.tools import ok_, eq_
from tests import client_test
from goodreads.author import GoodreadsAuthor

def author_test():
    """Test for getting an author"""
    client = client_test.make_client()
    author = client.author(1406384)
    ok_(isinstance(author, GoodreadsAuthor))
    ok_(isinstance(book, GoodreadsBook) for book in author.books)
    eq_(author.gid, '1406384')
    ok_(author.about)
    ok_(author.name)
    author.born_at
    author.died_at
    author.fans_count
    author.gender
    author.hometown
    author.link
    author.image_url
    author.small_image_url
    author.influences
    author.user
    author.works_count
