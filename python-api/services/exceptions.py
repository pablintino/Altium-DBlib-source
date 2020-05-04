# base app exception
class Error(Exception):
    def __init__(self, msg=None):
        self.msg = msg
    pass


class ResourceNotFoundError(Error):
    pass


class ResourceAlreadyExists(Error):
    pass

