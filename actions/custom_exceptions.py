class InputError(Exception):
    #raised when user inputs command parameters improperly
     def __init__(self, message="You didn't input a value for the time!"):
        self.message = message
        super().__init__(self.message)
    
     def __str__(self):
        return self.message
