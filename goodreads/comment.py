"""Class for Goodreads comments"""


class GoodreadsComment:
    """Goodreads comment class"""
    def __init__(self, comment_dict):
        self._comment_dict = comment_dict

    @property
    def gid(self):
        """Goodreads id of the comment"""
        return self._comment_dict['id']

    @property
    def body(self):
        """Body of the comment"""
        return self._comment_dict['body']

    @property
    def user(self):
        """User that made the comment"""
        return self._comment_dict['user']

    @property
    def created_at(self):
        """Comment created at"""
        return self._comment_dict['created_at']

    @property
    def updated_at(self):
        """Comment updated at"""
        return self._comment_dict['updated_at']
