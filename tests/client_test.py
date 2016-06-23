"""Client test functions"""

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
        assert self.client.client_key == apikey.key
        assert self.client.client_secret == apikey.secret

    def test_auth_user(self):
        user = self.client.auth_user()
        assert user.user_name == 'sefakilic'

    def test_user_info(self):
        user = self.client.user(1)
        assert user.user_name == 'otis'

    def test_author_by_id(self):
        author_id = '8566992'
        author = self.client.author(author_id)
        assert author.gid == author_id

    def test_author_by_name(self):
        author_name = 'Richard Dawkins'
        author = self.client.find_author(author_name)
        assert author.name == author_name

    def test_book_by_id(self):
        book_id = '11870085'
        book = self.client.book(book_id)
        assert book.gid == book_id

    def test_search_books(self):
        books = self.client.search_books("The selfish gene")
        assert len(books) > 0
        assert all(isinstance(book, GoodreadsBook) for book in books)

    def test_group_by_id(self):
        group_id = '1'
        group = self.client.group(group_id)
        assert group.gid == group_id
