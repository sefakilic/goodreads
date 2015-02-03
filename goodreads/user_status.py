import user
import book
import comment

class GoodreadsUserStatus:
    def __init__(self, user_status_dict):
        self._user_status_dict = user_status_dict

    @property
    def gid(self):
        """Goodreads id of the status"""
        return self._user_status_dict['id']

    @property
    def work_gid(self):
        """Goodreads id of the work"""
        return self._user_status_dict['work_id']

    @property
    def header(self):
        """Header of the status"""
        return self._user_status_dict['header']

    @property
    def body(self):
        """Body of the status"""
        return self._user_status_dict['body']

    @property
    def page(self):
        """Page status"""
        return self._user_status_dict['page']

    @property
    def percent(self):
        """Percent completion of the book"""
        return self._user_status_dict['percent']

    @property
    def user(self):
        """User object for the status"""
        return user.GoodreadsUser(self._user_status_dict['user'])

    @property
    def book(self):
        """Book object for the status"""
        return book.GoodreadsBook(self._user_status_dict['book'])

    @property
    def comments(self):
        """Comments for the status"""
        return [comment.GoodreadsComment(comment_dict)
                for comment_dict in self._user_status_dict['comments']]

    @property
    def created_at(self):
        """User status created at"""
        return self._user_status_dict['created_at']

    @property
    def updated_at(self):
        """User status updated at"""
        return self._user_status_dict['updated_at']

    @property
    def likes_count(self):
        """How many likes this status has?"""
        return self._user_status_dict['likes_count']

    @property
    def comments_count(self):
        """How many comments this status has?"""
        return self._user_status_dict['comments_count']

    @property
    def liked(self):
        """Did you like this status"""
        return self._user_status_dict['liked']

