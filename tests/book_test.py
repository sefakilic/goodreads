"""Test functions for GoodreadsBook"""

from nose.tools import ok_, eq_, nottest
from tests import client_test
from goodreads.book import GoodreadsBook
from goodreads.author import GoodreadsAuthor

@nottest
def book_test_unit(client, book_id):
    """Test for getting a book"""
    book = client.book(book_id)
    ok_(isinstance(book, GoodreadsBook))
    eq_(book.gid, book_id)
    ok_(book.title)
    book.authors
    book.description
    book.average_rating
    book.rating_dist
    book.ratings_count
    book.text_reviews_count
    book.num_pages
    book.popular_shelves
    book.work
    book.series_works
    book.publication_date
    book.publisher
    book.language_code
    book.edition_information
    book.image_url
    book.small_image_url
    book.is_ebook
    book.format
    book.isbn
    book.isbn13
    book.link
    book.reviews_widget
    book.similar_books

def book_test():
    client = client_test.make_client()
    # book with a single author
    book_test_unit(client, '11870085')
    # book with multiple authors
    #book_test_unit(client, '24780653')
