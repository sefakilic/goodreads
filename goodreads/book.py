"""Goodreads book class"""
from . import author
from . import shelf


class GoodreadsBook:
    def __init__(self, book_dict, client):
        self._book_dict = book_dict
        self._client = client

    def __repr__(self):
        return self.title

    @property
    def gid(self):
        """Goodreads id of the book"""
        return self._book_dict['id']

    @property
    def title(self):
        """Title of the book"""
        return self._book_dict['title']

    @property
    def authors(self):
        """Authors of the book"""
        # Goodreads API returns a list if there are more than one authors,
        # otherwise, just the OrderedDict
        if type(self._book_dict['authors']['author']) == list:
            return [author.GoodreadsAuthor(author_dict, self._client)
                    for author_dict in self._book_dict['authors']['author']]
        else:
            return [author.GoodreadsAuthor(self._book_dict['authors']['author'],
                                           self._client)]

    @property
    def description(self):
        """Description of the book"""
        return self._book_dict['description']

    @property
    def average_rating(self):
        """Average rating of the book"""
        return self._book_dict['average_rating']

    @property
    def rating_dist(self):
        """Rating distribution of the book"""
        return self._book_dict['work']['rating_dist']

    @property
    def ratings_count(self):
        """Number of ratings for the book"""
        return self._book_dict['ratings_count']

    @property
    def text_reviews_count(self):
        """Number of text reviews for the book"""
        return self._book_dict['text_reviews_count']

    @property
    def num_pages(self):
        """Number of pages of the book"""
        return self._book_dict['num_pages']

    @property
    def popular_shelves(self):
        """Popular shelves for the book"""
        return [shelf.GoodreadsShelf(shelf_dict)
                for shelf_dict in self._book_dict['popular_shelves']['shelf']]

    @property
    def work(self):
        """Information on the original work"""
        return self._book_dict['work']

    @property
    def series_works(self):
        """Return series of the book"""
        return self._book_dict['series_works']

    @property
    def publication_date(self):
        """Publication month/day/year for the book"""
        return (self._book_dict['publication_month'],
                self._book_dict['publication_day'],
                self._book_dict['publication_year'])

    @property
    def publisher(self):
        """Publisher for the book"""
        return self._book_dict['publisher']

    @property
    def language_code(self):
        """Language code for the book"""
        return self._book_dict['language_code']

    @property
    def edition_information(self):
        """Edition information of the book"""
        return self._book_dict['edition_information']

    @property
    def image_url(self):
        """Image URL of the book"""
        return self._book_dict['image_url']

    @property
    def small_image_url(self):
        """Small image URL of the book"""
        return self._book_dict['small_image_url']

    @property
    def is_ebook(self):
        """Is this book an e-book?"""
        return self._book_dict['is_ebook']

    @property
    def format(self):
        """Book format"""
        return self._book_dict['format']

    @property
    def isbn(self):
        """ISBN of the book"""
        return self._book_dict['isbn']

    @property
    def isbn13(self):
        """ISBN13 of the book"""
        return self._book_dict['isbn13']

    @property
    def link(self):
        """Link for the book"""
        return self._book_dict['link']

    @property
    def reviews_widget(self):
        """Widget for reviews in HTML"""
        return self._book_dict['reviews_widget']

    @property
    def similar_books(self):
        """Return the list of similar books."""
        return [GoodreadsBook(b, self._client)
                for b in self._book_dict['similar_books']['book']]
