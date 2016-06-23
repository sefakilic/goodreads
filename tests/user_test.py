from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.user import GoodreadsUser
from goodreads.group import GoodreadsGroup
from goodreads.owned_book import GoodreadsOwnedBook
from nose.tools import eq_, ok_


class TestUser():
    @classmethod
    def setup_class(cls):
        cls.client = GoodreadsClient(apikey.key, apikey.secret)
        cls.client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.user = cls.client.user('1')

    def test_get_user(self):
        ok_(isinstance(self.user, GoodreadsUser))
        eq_(self.user.gid, '1')

    def test_user_name(self):
        eq_(self.user.user_name, 'otis')

    def test_name(self):
        eq_(self.user.name, 'Otis Chandler')

    def test_link(self):
        eq_(self.user.link,
            u'http://www.goodreads.com/user/show/1-otis-chandler')

    def test_image_url(self):
        eq_(self.user.image_url,
            u'http://d.gr-assets.com/users/1189644957p3/1.jpg')

    def test_small_image_url(self):
        eq_(self.user.small_image_url,
            u'http://d.gr-assets.com/users/1189644957p2/1.jpg')

    def test_user_in_groups(self):
        groups = self.user.list_groups()
        ok_(all(isinstance(group, GoodreadsGroup) for group in groups))

    def test_user_not_in_any_group(self):
        user = self.client.user('25044452')  # A user with no joined groups
        eq_(user.list_groups(), [])

    def test_user_own_books(self):
        user = self.client.user('6205894')  # A user with owned books
        owned_books = user.owned_books()
        ok_(all(isinstance(book, GoodreadsOwnedBook) for book in owned_books))

    def test_user_not_own_any_books(self):
        owned_books = self.user.owned_books()
        eq_(owned_books, [])
