"""Class implementation for Goodreads reviews"""

class GoodreadsReview():
    def __init__(self, review_dict):
        self._review_dict = review_dict

    def gid(self):
        """Goodreads id for the review"""
        return self._review_dict['id']

    def book(self):
        """Book that the review belongs to"""
        return self._review_dict['book']

    def rating(self):
        """Rating of the book"""
        return self._review_dict['rating']

    def shelves(self):
        """Shelves for the book"""
        return [shelf['@name']
                for shelf in self._review_dict['shelves']['shelf']]

    def recommended_for(self):
        """Book recommended for"""
        return self._review_dict['recommended_for']

    def recommended_by(self):
        """Book recommended by"""
        return self._review_dict['recommended_by']

    def started_at(self):
        """Book started at"""
        return self._review_dict['started_at']

    def read_at(self):
        """Book read at"""
        return self._review_dict['read_at']

    def body(self):
        """Body for the review"""
        return self._review_dict['body']

    def comments_count(self):
        """Number of comments to this review"""
        return self._review_dict['comments_count']

    def url(self):
        """URL for this comment"""
        return self._review_dict['url']

    def owned(self):
        """Is the book owned by this user?"""
        return self._review_dict['owned']

