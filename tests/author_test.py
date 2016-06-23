from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.author import GoodreadsAuthor


class TestAuthor():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.author = client.author('64941')

    def test_get_author(self):
        assert isinstance(self.author, GoodreadsAuthor)
        assert self.author.gid == '64941'

    def test_author_name(self):
        assert self.author.name == 'Donald Ervin Knuth'
