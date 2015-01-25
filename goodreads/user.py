class GoodreadsUser():
    def __init__(self, resp_dict):
        self._user_dict = resp_dict['GoodreadsResponse']['user']

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
    def private(self):
        return self._user_dict['private']

