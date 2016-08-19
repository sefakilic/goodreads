from nose.tools import eq_, ok_

from goodreads import apikey
from goodreads.client import GoodreadsClient


class TestOwnedBook():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.owned_book = client.owned_book('43018920')

    def test_owned_book(self):
        eq_(self.owned_book.gid, '43018920')
