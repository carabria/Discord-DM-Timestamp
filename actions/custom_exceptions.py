class NoTimeValueError(Exception):
    #raised when user inputs command parameters for the time value improperly
     def __init__(self, message="You didn't input a value for the time properly! Prefix your time with a number!"):
        self.message = message
        super().__init__(self.message)
    
     def __str__(self):
        return self.message
     
class NoTimeStringError(Exception):
    #raised when user inputs command parameters for the time string improperly
     def __init__(self, message="You didn't specify how long properly! Use minutes, hours, etc!"):
        self.message = message
        super().__init__(self.message)
    
     def __str__(self):
        return self.message