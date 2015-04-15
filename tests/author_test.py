"""Test functions for GoodreadsAuthor"""

from nose.tools import ok_, eq_, nottest
from tests import client_test
from goodreads.author import GoodreadsAuthor

@nottest
def author_test_unit(client, author_id):
    """Test for getting an author"""
    author = client.author(author_id)
    ok_(isinstance(author, GoodreadsAuthor))
    ok_(isinstance(book, GoodreadsBook) for book in author.books)
    eq_(author.gid, author_id)
    ok_(author.name)
    author.about
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

def author_test():
    client = client_test.make_client()
    # test author with a single book
    author_test_unit(client, '8566992')
    # author with multiple books
    author_test_unit(client, '1406384')
