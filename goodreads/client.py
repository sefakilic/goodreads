import requests
import webbrowser
import xmltodict
from session import GoodreadsSession

class GoodreadsClient():
    base_url = "http://www.goodreads.com/"

    def __init__(self, client_key, client_secret):
        """Initialize the client"""
        self.client_key = client_key
        self.client_secret = client_secret

    def request(self, path, query_dict=None):
        """Goodreads request handler."""
        if query_dict is None:
            query_dict = {}
        query_dict['key'] = self.client_key # add client key to query dict
        return requests.get(self.base_url + path, params=query_dict)

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
        """Get id of user who authorized OAuth"""
        if not self.session:
            raise Exception("No authenticated session")
        return self.request("api/auth_user")

    def author_books(self, author_id, page=1):
        """Get a paginated list of an author's books"""
        resp = self.request("author/list", {'id': author_id, 'page':page})
        return xmltodict.parse(resp.text)

    def author_show(self, author_id):
        """Get info about an author"""
        resp = self.request("author/show", {'id': author_id})
        return xmltodict.parse(resp.text)

    def book_isbn_to_id(self, isbn):
        """Get the Goodreads book ID given an ISBN. Response contains the ID
        without any markup."""
        resp = self.request("book/isbn_to_id", {'isbn': isbn})
        return resp.text

    def book_review_counts(self, isbns):
        """Get review statistics for books given a list of ISBNs."""
        resp = self.request("book/review_counts.json",
                            {'isbns': ','.join(isbns)})
        return resp.json()

    def book_show(self, book_id):
        """Get the reviews for a book given a Goodreads book id"""
        resp = self.request("book/show", {'id': book_id})
        return xmltodict.parse(resp.text)


gc = GoodreadsClient("sy1BoFti8To9YO2uUc2NQ",
                     "NwQZdMRrhdgYTdg81dZrPfrTeBIGqnBcqR6nbIPCMg")
gc.authenticate(u'9nuSGNZ1tw57RECezUlig', u'5kNJBxe4cvgjx5GUn8aPktqlEHAl24wM33idVHwI7cI')
