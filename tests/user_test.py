"""Test functions for User"""

from nose.tools import ok_
from tests import client_test
from goodreads.user import GoodreadsUser

def user_test():
    """Test for getting the user"""
    client = client_test.make_client_with_auth()
    user = client.auth_user()
    ok_(isinstance(user, GoodreadsUser))
    ok_(user.gid)
