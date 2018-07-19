class MyError(TypeError):
    #Multi Line String
    # Directly underneath class or method --> Docstring
    '''
    
    '''
    def __init__(self, message, code):
        super().__init__(f'<Error: {self.__class__} Message: {message} Code: {code}')
        self.code = code

raise MyError('Message', 99)