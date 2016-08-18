import webbrowser
import collections


from .session import GoodreadsSession
from .user import GoodreadsUser
from .book import GoodreadsBook
from .author import GoodreadsAuthor
from .request import GoodreadsRequest
from .comment import GoodreadsComment
from .event import GoodreadsEvent
from .group import GoodreadsGroup
from .owned_book import GoodreadsOwnedBook
from .review import GoodreadsReview


class GoodreadsClientException(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class GoodreadsClient():
    base_url = "https://www.goodreads.com/"

    def __init__(self, client_key, client_secret):
        """Initialize the client"""
        self.client_key = client_key
        self.client_secret = client_secret

    @property
    def query_dict(self):
        return {'key': self.client_key}

    def authenticate(self, access_token=None, access_token_secret=None):
        """Authenticate client to query requiring authorization"""
        self.session = GoodreadsSession(self.client_key, self.client_secret,
                                        access_token, access_token_secret)
        if access_token and access_token_secret:
            self.session.oauth_resume()
        else:
            url = self.session.oauth_init()
            webbrowser.open(url)
            while input("Have you authorized me? (y/n)") != 'y':
                pass
            self.session.oauth_finalize()

    def auth_user(self):
        """Return user who authorized OAuth"""
        if not hasattr(self, 'session'):
            raise GoodreadsClientException("No authenticated session")
        resp = self.request_oauth('api/auth_user', {})
        user_id = resp['user']['@id']
        return self.user(user_id)

    def request(self, *args, **kwargs):
        """Create a GoodreadsRequest object and make that request"""
        req = GoodreadsRequest(self, *args, **kwargs)
        return req.request()

    def request_oauth(self, *args, **kwargs):
        resp = self.session.get(*args, **kwargs)
        return resp

    def user(self, user_id=None, username=None):
        """Get info about a member by id or username.

        If user_id or username not provided, the function returns the
        authorized user.
        """
        if not (user_id or username):
            return self.auth_user()
        resp = self.request("user/show", {'id': user_id, 'username': username})
        return GoodreadsUser(resp['user'], self)

    def author(self, author_id):
        """Get info about an author"""
        resp = self.request("author/show", {'id': author_id})
        return GoodreadsAuthor(resp['author'], self)

    def find_author(self, author_name):
        """Find an author by name"""
        resp = self.request("api/author_url/%s" % author_name, {})
        return self.author(resp['author']['@id']) if 'author' in resp else None

    def book(self, book_id=None, isbn=None):
        """Get info about a book"""
        if book_id:
            resp = self.request("book/show", {'id': book_id})
            return GoodreadsBook(resp['book'], self)
        elif isbn:
            resp = self.request("book/isbn", {'isbn': isbn})
            return GoodreadsBook(resp['book'], self)
        else:
            raise GoodreadsClientException("book id or isbn required")

    def search_books(self, q, page=1, search_field='all'):
        """Get the most popular books for the given query. This will search all
        books in the title/author/ISBN fields and show matches, sorted by
        popularity on Goodreads.
        :param q: query text
        :param page: which page to return (default 1)
        :param search_fields: field to search, one of 'title', 'author' or
        'genre' (default is 'all')
        """
        resp = self.request("search/index.xml",
                            {'q': q, 'page': page, 'search[field]': search_field})
        works = resp['search']['results']['work']
        # If there's only one work returned, put it in a list.
        if type(works) == collections.OrderedDict:
            works = [works]
        return [self.book(work['best_book']['id']['#text']) for work in works]

    def group(self, group_id):
        """Get info about a group"""
        resp = self.request("group/show", {'id': group_id})
        return GoodreadsGroup(resp['group'])

    def owned_book(self, owned_book_id):
        """Get info about an owned book, given its id"""
        resp = self.session.get("owned_books/show/%s" % owned_book_id,
                                {'format': 'xml'})
        return GoodreadsOwnedBook(resp['owned_book']['owned_book'])

    def find_groups(self, query, page=1):
        """Find a group based on the query"""
        resp = self.request("group/search.xml", {'q': query, 'page': page})
        return resp['groups']['list']['group']

    def book_review_stats(self, isbns):
        """Get review statistics for books given a list of ISBNs"""
        resp = self.request("book/review_counts.json",
                            {'isbns': ','.join(isbns)},
                            req_format='json')
        return resp['books']

    def list_comments(self, comment_type, resource_id, page=1):
        """List comments on a subject.

        comment_type should be one of 'author_blog_post', 'blog',
        'book_news_post', 'chapter', 'comment', 'community_answer',
        'event_response', 'fanship', 'friend', 'giveaway', 'giveaway_request',
        'group_user', 'interview', 'librarian_note', 'link_collection', 'list',
        'owned_book', 'photo', 'poll', 'poll_vote', 'queued_item', 'question',
        'question_user_stat', 'quiz', 'quiz_score', 'rating', 'read_status',
        'recommendation', 'recommendation_request', 'review', 'topic', 'user',
        'user_challenge', 'user_following', 'user_list_challenge',
        'user_list_vote', 'user_quote', 'user_status', 'video'.
        """
        resp = self.request("%s/%s/comments" % (comment_type, resource_id),
                            {'format': 'xml'})
        return [GoodreadsComment(comment_dict)
                for comment_dict in resp['comments']['comment']]

    def list_events(self, postal_code):
        """Show events near a location specified with the postal code"""
        resp = self.request("event/index.xml", {'search[postal_code]': postal_code})
        return [GoodreadsEvent(e) for e in resp['events']['event']]

    def recent_reviews(self):
        """Get the recent reviews from all members"""
        resp = self.request("/review/recent_reviews.xml", {})
        return [GoodreadsReview(r) for r in resp['reviews']['review']]

    def review(self, review_id):
        """Get a review"""
        resp = self.request("/review/show.xml", {'id': review_id})
        return GoodreadsReview(resp['review'])
