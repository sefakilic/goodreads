from nose.tools import *
from goodreads.client import GoodreadsClient
from goodreads.user import GoodreadsUser
from goodreads.author import GoodreadsAuthor
from goodreads.book import GoodreadsBook

def client_key_secret():
    key = "sy1BoFti8To9YO2uUc2NQ"
    secret = "NwQZdMRrhdgYTdg81dZrPfrTeBIGqnBcqR6nbIPCMg"
    return key, secret

def oauth_token_secret():
    token = '9nuSGNZ1tw57RECezUlig'
    secret = u'5kNJBxe4cvgjx5GUn8aPktqlEHAl24wM33idVHwI7cI'
    return token, secret

def make_client():
    key, secret = client_key_secret()
    gc = GoodreadsClient(key, secret)
    return gc

def make_client_with_auth():
    gc = make_client()
    token, secret = oauth_token_secret()
    gc.authenticate(token, secret)
    return gc

def client_test():
    key, _ = client_key_secret()
    gc = make_client()
    eq_(gc.query_dict['key'], key)

def auth_test():
    gc = make_client_with_auth()

def user_test():
    gc = make_client_with_auth()
    user = gc.auth_user()
    ok_(isinstance(user, GoodreadsUser))
    ok_(user.id)

def author_test():
    gc = make_client()
    author = gc.author(18541)
    ok_(isinstance(author, GoodreadsAuthor))
    ok_(author.id)

def book_test():
    gc = make_client()
    book = gc.book(50)
    ok_(isinstance(book, GoodreadsBook))
    ok_(book.id)
