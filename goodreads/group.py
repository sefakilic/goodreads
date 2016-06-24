"""Class for GoodreadsGroup"""

class GoodreadsGroup:
    """Goodreads Group class implementation"""
    def __init__(self, group_dict):
        self._group_dict = group_dict

    def __repr__(self):
        return self.title

    @property
    def gid(self):
        """Goodreads id for the group"""
        return self._group_dict['id']

    @property
    def title(self):
        """Title for the group"""
        return self._group_dict['title']

    @property
    def description(self):
        """Description of the group"""
        return self._group_dict['description']

    @property
    def category(self):
        """Category of the group"""
        return self._group_dict['category']

    @property
    def subcategory(self):
        """Sub-category of the group"""
        return self._group_dict['subcategory']

    @property
    def rules(self):
        """Group rules"""
        return self._group_dict['rules']

    @property
    def image_url(self):
        """Image URL for the group"""
        return self._group_dict['image_url']

    @property
    def last_activity_at(self):
        """Time of the last activity in the group"""
        return self._group_dict['last_activity_at']

    @property
    def access(self):
        """Is the group public or private?"""
        return self._group_dict['access']

    @property
    def users_count(self):
        """Number of users in the group"""
        return self._group_dict['group_users_count']

    @property
    def members(self):
        """Members of the group"""
        return self._group_dict['members']['group_users']
