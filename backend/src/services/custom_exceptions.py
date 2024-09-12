'''Custom exceptions for CRUD operations'''

class ItemException(Exception):
    '''Exception subclass for CRUD errors'''
    def __init__(self, http_code: int, message: str):
        self.http_code = http_code
        self.message = message
        super().__init__(self.message)


class ItemAlreadyExistsException(ItemException):
    '''Exception for cases when the item does already exist'''
    def __init__(self):
        http_code = 409
        message = "Requested item already exists"
        super().__init__(http_code, message)


class ItemDoesNotExistException(ItemException):
    '''Exception for cases when the item does not exist'''
    def __init__(self):
        http_code = 404
        message = "Requested item does not exist"
        super().__init__(http_code, message)
