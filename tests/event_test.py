from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.event import GoodreadsEvent


class TestEvent():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.events = client.list_events('21244')

    def test_list_events(self):
        assert all(isinstance(e, GoodreadsEvent) for e in self.events)
