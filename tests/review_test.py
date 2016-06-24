from nose.tools import eq_, ok_

from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.review import GoodreadsReview


class TestReview():
    @classmethod
    def setup_class(cls):
        cls.client = GoodreadsClient(apikey.key, apikey.secret)
        cls.client.authenticate(apikey.oauth_access_token,
                                apikey.oauth_access_token_secret)

    def test_recent_reviews(self):
        reviews = self.client.recent_reviews()
        ok_(all(isinstance(r, GoodreadsReview) for r in reviews))

    def test_review(self):
        review = self.client.review('2')
        eq_(review.gid, '2')
        pass
