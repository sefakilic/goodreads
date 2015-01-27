from request import GoodreadsRequest

class GoodreadsUser():
    def __init__(self, user_dict):
        for key in user_dict:
            setattr(self, key, user_dict[key])

