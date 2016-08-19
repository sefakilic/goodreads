import collections

from goodreads import apikey
from goodreads.client import GoodreadsClient
from goodreads.book import GoodreadsBook
from goodreads.author import GoodreadsAuthor
from goodreads.shelf import GoodreadsShelf


class TestBook():
    @classmethod
    def setup_class(cls):
        client = GoodreadsClient(apikey.key, apikey.secret)
        client.authenticate(apikey.oauth_access_token,
                            apikey.oauth_access_token_secret)
        cls.book = client.book('11870085')

    def test_get_book(self):
        assert isinstance(self.book, GoodreadsBook)
        assert self.book.gid == '11870085'
        assert repr(self.book) == 'The Fault in Our Stars'

    def test_title(self):
        assert self.book.title == 'The Fault in Our Stars'

    def test_authors(self):
        assert len(self.book.authors) == 1
        assert isinstance(self.book.authors[0], GoodreadsAuthor)

    def test_description(self):
        assert self.book.description.startswith(
            '"I fell in love the way you fall asleep: slowly, then all at once."')

    def test_average_rating(self):
        rating = float(self.book.average_rating)
        assert rating >= 1.0
        assert rating <= 5.0

    def test_rating_dist(self):
        assert self.book.rating_dist.startswith('5:')

    def test_ratings_count(self):
        assert self.book.ratings_count.isdigit()

    def test_text_reviews_count(self):
        assert self.book.text_reviews_count.isdigit()

    def test_num_pages(self):
        assert self.book.num_pages.isdigit()

    def test_popular_shelves(self):
        assert all(isinstance(shelf, GoodreadsShelf)
                   for shelf in self.book.popular_shelves)

    def test_work(self):
        assert type(self.book.work) == collections.OrderedDict
        assert self.book.work['id']['#text'] == '16827462'

    def test_series_works(self):
        assert self.book.series_works is None

    def test_publication_date(self):
        assert self.book.publication_date == ('1', '10', '2012')

    def test_publisher(self):
        assert self.book.publisher == 'Dutton Books'

    def test_language_code(self):
        assert self.book.language_code == 'eng'

    def test_edition_information(self):
        assert self.book.edition_information is None

    def test_image_url(self):
        assert self.book.image_url == 'https://d2arxad8u2l0g7.cloudfront.net/books/1360206420m/11870085.jpg'

    def test_small_image_url(self):
        assert self.book.small_image_url == 'https://d2arxad8u2l0g7.cloudfront.net/books/1360206420s/11870085.jpg'

    def test_is_ebook(self):
        assert self.book.is_ebook == 'false'

    def test_format(self):
        assert self.book.format == 'Hardcover'

    def test_isbn(self):
        assert self.book.isbn == '0525478817'

    def test_isbn13(self):
        assert self.book.isbn13 == '9780525478812'

    def test_link(self):
        assert self.book.link == 'https://www.goodreads.com/book/show/11870085-the-fault-in-our-stars'

    def test_reviews_widget(self):
        assert self.book.reviews_widget.startswith('<style>')
        assert self.book.reviews_widget.endswith('</div>')

    def test_similar_books(self):
        assert all(isinstance(b, GoodreadsBook)
                   for b in self.book.similar_books)
