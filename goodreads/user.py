import book
import request
import group
import owned_book
import review

class GoodreadsUser():
    def __init__(self, user_dict, client):
        self._user_dict = user_dict
        self._client = client   # for later queries

    def __repr__(self):
        return self.user_name

    @property
    def gid(self):
        """Goodreads ID for the user"""
        return self._user_dict['id']

    @property
    def user_name(self):
        """Goodreads handle of the user"""
        return self._user_dict['user_name']

    @property
    def name(self):
        """Name of the user"""
        return self._user_dict['name']

    @property
    def link(self):
        """URL for user profile"""
        return self._user_dict['link']

    @property
    def image_url(self):
        """URL of user image"""
        return self._user_dict['image_url']

    @property
    def small_image_url(self):
        """URL of user image (small)"""
        return self._user_dict['small_image_url']

    def list_groups(self, page=1):
        """List groups for the user. If there are more than 30 groups, get them
        page by page."""
        resp = self._client.request("group/list/%s.xml" % self.gid, {'page':page})
        return resp['groups']['list']['group']

    def owned_books(self, page=1):
        """Return the list of books owned by the user"""
        resp = self._client.session.get("owned_books/user/%s.xml" % self.gid,
                                        {'page': page, 'format': 'xml'})
        return [owned_book.GoodreadsOwnedBook(d)
                for d in resp['owned_books']['owned_book']]

    def read_status(self):
        """Get the user's read status"""
        resp = self._client.request("read_statuses/%s" % self.gid, {})
        return resp['read_status']

    def reviews(self, page=1):
        """Get all books and reviews on user's shelves"""
        resp = self._client.session.get("/review/list.xml",
                                        {'v': 2, 'id': self.gid, 'page': page})
        return [review.GoodreadsReview(r) for r in resp['reviews']['review']]

    def shelves(self, page=1):
        """Get the user's shelves. This method gets shelves only for users with
        public profile"""
        resp = self._client.request("shelf/list.xml",
                                    {'user_id': self.gid, 'page': page})
        return resp['shelves']['user_shelf']

