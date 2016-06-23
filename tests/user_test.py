from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.user import GoodreadsUser


class TestBook():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.user = client.user('1')

    def test_get_book(self):
        assert isinstance(self.user, GoodreadsUser)
        assert self.user.gid == '1'
