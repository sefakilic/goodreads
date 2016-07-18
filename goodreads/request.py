import requests
import xmltodict
import json


class GoodreadsRequestException(Exception):
    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return self.url, ':', self.error_msg


class GoodreadsRequest():
    def __init__(self, client, path, query_dict, req_format='xml'):
        """Initialize request object."""
        self.params = query_dict
        self.params.update(client.query_dict)
        self.host = client.base_url
        self.path = path
        self.req_format = req_format

    def request(self):
        resp = requests.get(self.host+self.path, params=self.params)
        if resp.status_code != 200:
            raise GoodreadsRequestException(resp.reason, self.path)
        if self.req_format == 'xml':
            data_dict = xmltodict.parse(resp.content)
            return data_dict['GoodreadsResponse']
        elif self.req_format == 'json':
            return json.loads(resp.content)
        else:
            raise Exception("Invalid format")
