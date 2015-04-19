"""Client test functions"""

from nose.tools import eq_, ok_, nottest
from goodreads.client import GoodreadsClient
from goodreads.event import GoodreadsEvent
from goodreads.review import GoodreadsReview
from goodreads.book import GoodreadsBook
from goodreads import apikey

@nottest
def make_client():
    """Create a client object"""
    key, secret = apikey.key, apikey.secret
    client = GoodreadsClient(key, secret)
    client.authenticate(apikey.oauth_access_token,
                        apikey.oauth_access_token_secret)
    return client

def client_test():
    """Test client object"""
    key = apikey.key
    client = make_client()
    eq_(client.query_dict['key'], key)

    # Call methods
    client.query_dict

    client.auth_user()
    
    myself = client.user()               # authorized user itself
    
    user = client.user(1)              # another user
    user.user_name

    author = client.author('8566992')
    author.name

    author = client.find_author("Richard Dawkins")
    author.name

    book = client.book('11870085')
    book.title

    books = client.search_books("The selfish gene")
    ok_(all(isinstance(book, GoodreadsBook) for book in books))

    grp = client.group('8095')
    grp.title

    client.find_groups("book")

    client.book_review_stats(["0441172717", "2C0141439602"])

    # list comments
    #comments = client.list_comments("user", "36918660")

    # list events nearby
    events = client.list_events("21250")
    ok_(all(isinstance(event, GoodreadsEvent) for event in events))
    print events[0].title

    # list recent reviews
    reviews = client.recent_reviews()
    ok_(all(isinstance(review, GoodreadsReview) for review in reviews))
    print reviews[0]

    # get a review
    review = client.review("1212820989")
    print review.body
