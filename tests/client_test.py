"""Client test functions"""

from nose.tools import eq_, ok_, nottest, with_setup
from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.book import GoodreadsBook


class TestClient():
    @classmethod
    def setup_class(cls):
        cls.client = GoodreadsClient(apikey.key, apikey.secret)
        cls.client.authenticate(apikey.oauth_access_token,
                                apikey.oauth_access_token_secret)

    def test_client_setup(self):
        eq_(self.client.client_key, apikey.key)
        eq_(self.client.client_secret, apikey.secret)

    def x_user_authentication(self):
        myself = self.client.auth_user()
        print myself

    def test_user_info(self):
        user = self.client.user(1)
        eq_(user.user_name, 'otis')

    def test_author_by_id(self):
        author_id = '8566992'
        author = self.client.author(author_id)
        eq_(author.gid, author_id)

    def test_author_by_name(self):
        author_name = 'Richard Dawkins'
        author = self.client.find_author(author_name)
        eq_(author.name, author_name)

    def test_book_by_id(self):
        book_id = '11870085'
        book = self.client.book(book_id)
        eq_(book.gid, book_id)

    def test_search_books(self):
        books = self.client.search_books("The selfish gene")
        assert len(books) > 0
        ok_(all(isinstance(book, GoodreadsBook) for book in books))
