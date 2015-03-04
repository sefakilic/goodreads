"""Client test functions"""

from nose.tools import eq_
from goodreads.client import GoodreadsClient
from goodreads import apikey

def make_client():
    """Create a client object"""
    key, secret = apikey.key, apikey.secret
    client = GoodreadsClient(key, secret)
    return client

def make_client_with_auth():
    """Create a client object with oauth"""
    client = make_client()
    client.authenticate(apikey.oauth_access_token,
                        apikey.oauth_access_token_secret)
    return client

def client_test():
    """Test client object"""
    key = apikey.key
    client = make_client()
    eq_(client.query_dict['key'], key)

def auth_test():
    """Authentication test"""
    client = make_client_with_auth()
    return client

