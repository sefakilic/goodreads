import requests
import xmltodict

class GoodreadsRequestException(Exception):
    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return self.error_msg + '(%s)' % url

class GoodreadsRequest():
    def __init__(self, client, path, query_dict):
        """Initialize request object."""
        self.params = dict(query_dict.items() + client.query_dict.items())
        self.host = client.base_url
        self.path = path

    def request(self):
        resp = requests.get(self.host+self.path, params=self.params)
        if resp.status_code != 200:
            raise GoodreadsRequestException(resp.reason, self.path)

        data_dict = xmltodict.parse(resp.content)
        return data_dict['GoodreadsResponse']
