from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.book import GoodreadsBook


class TestBook():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.book = client.book('11870085')

    def test_get_book(self):
        assert isinstance(self.book, GoodreadsBook)
        assert self.book.gid == '11870085'
