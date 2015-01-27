from request import GoodreadsRequest

class GoodreadsUser():
    def __init__(self, resp_dict):
        self._user_dict = resp_dict['user']

    @property
    def id(self):
        return self._user_dict['id']

    @property
    def name(self):
        return self._user_dict['name']

    @property
    def user_name(self):
        return self._user_dict['user_name']

    @property
    def link(self):
        return self._user_dict['link']

    @property
    def image_url(self):
        return self._user_dict['image_url']

    @property
    def small_image_url(self):
        return self._user_dict['small_image_url']

    @property
    def about(self):
        return self._user_dict['about']

    @property
    def age(self):
        return self._user_dict['age']

    @property
    def gender(self):
        return self._user_dict['gender']

    @property
    def location(self):
        return self._user_dict['location']

    @property
    def website(self):
        return self._user_dict['website']

    @property
    def joined(self):
        return self._user_dict['joined']

    @property
    def last_active(self):
        return self._user_dict['last_active']

    @property
    def interests(self):
        return self._user_dict['interests']


