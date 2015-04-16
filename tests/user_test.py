"""Test functions for User"""

from nose.tools import ok_, nottest, eq_
from tests import client_test
from goodreads.user import GoodreadsUser
from goodreads.group import GoodreadsGroup

@nottest
def user_test_unit(user_id):
    """Test for getting the user"""
    client = client_test.make_client()
    user = client.user(user_id)
    ok_(isinstance(user, GoodreadsUser))
    eq_(user.gid, user_id)
    ok_(user.user_name)
    # Call other methods
    user.name
    user.link
    user.image_url
    user.small_image_url
    user.list_groups()
    user.owned_books()
    user.read_status()
    user.reviews()
    user.shelves()
    


def user_test():
    user_test_unit('1')
