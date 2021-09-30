class Error(Exception):
    pass

class LessThan40Error(Exception):

    def __init__(self,  message="Activity should not be less than 40hrs"):
        self.message = message
        super().__init__(self.message)


