"""Class definition for owned books"""

from . import book

class GoodreadsOwnedBook:
    def __init__(self, owned_book_dict):
        self._owned_book_dict = owned_book_dict

    @property
    def gid(self):
        """Goodreads id of the owned book"""
        return self._owned_book_dict['id']['#text']

    @property
    def book(self):
        """Book owned"""
        return book.GoodreadsBook(self._owned_book_dict['book'])

    @property
    def review(self):
        """Review for the owned book"""
        return self._owned_book_dict['review']

    @property
    def current_owner(self):
        """Return current owner's id"""
        return self._owned_book_dict['current_owner_id']['#text']

    @property
    def original_purchase_date(self):
        """Date of purchase"""
        return self._owned_book_dict['original_purchase_date']

    @property
    def original_purchase_location(self):
        """Purchase location"""
        return self._owned_book_dict['original_purchase_location']

    def condition(self):
        """Condition of the book"""
        return self._owned_book_dict['condition']

    def link(self):
        """Linked for the owned book"""
        return self._owned_book_dict['link']
