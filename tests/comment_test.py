from nose.tools import eq_, ok_

from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.comment import GoodreadsComment


class TestComment():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.comments = client.list_comments('user', '1')

    def test_list_comments(self):
        ok_(all(isinstance(c, GoodreadsComment) for c in self.comments))
