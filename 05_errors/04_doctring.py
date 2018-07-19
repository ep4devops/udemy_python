"""
Module / File Definition 
"""
    # Multi Line String
    # Directly underneath class or method --> Docstring
class MyError(Exception):
    '''
    Exception raised when a specific error code is needed
    '''
    def __init__(self, message, code):
        super().__init__(f'<Error: {self.__class__} Message: {message} Code: {code}')
        self.code = code

#raise MyError('Message', 99)
print(MyError.__doc__)

# Tools for documentation