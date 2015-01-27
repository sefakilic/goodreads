
class GoodreadsAuthor:
    def __init__(self, author_dict):
        for key in author_dict:
            setattr(self, key, author_dict[key])

