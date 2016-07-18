from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.author import GoodreadsAuthor
from goodreads.book import GoodreadsBook


class TestAuthor():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.author = client.author('64941')

    def test_get_author(self):
        assert isinstance(self.author, GoodreadsAuthor)
        assert self.author.gid == '64941'
        assert repr(self.author) == 'Donald Ervin Knuth'

    def test_author_name(self):
        assert self.author.name == 'Donald Ervin Knuth'

    def test_author_about(self):
        self.author.about.startswith('Donald Ervin Knuth, born January 10th 1938,')

    def test_author_books(self):
        books = self.author.books
        assert all(isinstance(book, GoodreadsBook) for book in books)
        assert (books[-1].title == 'Literate Programming')

    def test_born_at(self):
        self.author.born_at == '1938/01/10'

    def test_gender(self):
        self.author.gender == 'male'

    def test_hometown(self):
        self.author.hometown == 'Milwaukee'

    def test_link(self):
        self.author.link == 'http://www.goodreads.com/author/show/64941.Donald_Ervin_Knuth'

    def test_image_url(self):
        self.author.image_url == 'http://d.gr-assets.com/authors/1236845611p5/64941.jpg'

    def test_small_image_url(self):
        self.author.small_image_url == 'http://d.gr-assets.com/authors/1236845611p2/64941.jpg'

    def test_works_count(self):
        self.author.works_count == '56'
