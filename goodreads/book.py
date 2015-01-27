
class GoodreadsBook:
    def __init__(self, book_dict):
        for key in book_dict:
            setattr(self, key, book_dict[key])
