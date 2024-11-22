class ServiceResponseException(Exception):
    def __init__(self, message, response=None, status_code=400):
        super().__init__(message)
        self.response = response
        self.status_code = status_code


class NoObjectException(Exception):
    def __init__(self, message, response=None):
        super().__init__(message)
        self.response = response
