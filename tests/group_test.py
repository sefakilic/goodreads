from nose.tools import eq_, ok_

from goodreads import apikey
from goodreads.client import GoodreadsClient


class TestGroup():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.group = client.group(1)

    def test_group_title(self):
        eq_(self.group.title, 'Goodreads Feedback')
