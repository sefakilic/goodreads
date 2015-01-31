import webbrowser

from session import GoodreadsSession
from user import GoodreadsUser
from book import GoodreadsBook
from author import GoodreadsAuthor
from request import GoodreadsRequest

class GoodreadsClientException(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg

class GoodreadsClient():
    base_url = "http://www.goodreads.com/"

    def __init__(self, client_key, client_secret):
        """Initialize the client"""
        self.client_key = client_key
        self.client_secret = client_secret

    @property
    def query_dict(self):
        return {'key': self.client_key}

    def authenticate(self, access_token=None, access_token_secret=None):
        self.session = GoodreadsSession(self.client_key, self.client_secret,
                                        access_token, access_token_secret)
        if access_token and access_token_secret:
            self.session.oauth_resume()
        else:
            url = self.session.oauth_init()
            webbrowser.open(url)
            while raw_input("Have you authorized me? (y/n)") != 'y':
                pass
            self.session.oauth_finalize()

    def auth_user(self):
        """Return user who authorized OAuth"""
        if not self.session:
            raise GoodreadsClientException("No authenticated session")
        resp = self.session.get("api/auth_user", {})
        user_id = resp['GoodreadsResponse']['user']['@id']
        return self.user(user_id)

    def request(self, *args, **kwargs):
        """Create a GoodreadsRequest object and make that request"""
        req = GoodreadsRequest(self, *args, **kwargs)
        return req.request()

    def user(self, user_id=None, username=None):
        """Get info about a member by id or username"""
        if not (user_id or username):
            raise GoodreadsClientException("user_id or username required")
        resp = self.request("user/show", {'id': user_id, 'username': username})
        return GoodreadsUser(resp['user'])

    def author(self, author_id):
        """Get info about an author"""
        resp = self.request("author/show", {'id': author_id})
        return GoodreadsAuthor(resp['author'])

    def book(self, book_id=None, isbn=None):
        """Get info about a book"""
        if book_id:
            resp = self.request("book/show", {'id': book_id})
            return GoodreadsBook(resp['book'])
        elif isbn:
            resp = self.request("book/isbn", {'isbn': isbn})
            return GoodreadsBook(resp['book'])
        else:
            raise GoodreadsClientException("book id or isbn required")
                                           
gc = GoodreadsClient("sy1BoFti8To9YO2uUc2NQ",
                     "NwQZdMRrhdgYTdg81dZrPfrTeBIGqnBcqR6nbIPCMg")
gc.authenticate(u'9nuSGNZ1tw57RECezUlig', u'5kNJBxe4cvgjx5GUn8aPktqlEHAl24wM33idVHwI7cI')
