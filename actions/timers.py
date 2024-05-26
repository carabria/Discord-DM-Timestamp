import time
import re
from actions import custom_exceptions

class Actions:
    def __init__(self):
        pass

    #returns the current time
    def current_time(self):
        #splits time so it has no miliseconds
        timer = str(time.time()).split(".")
        return int(timer[0])
    
    #checks to see if -t, -T, etc is contained in the message, then returns a string for the proper format
    def formatter(self, message):
        #the regex here searches for the parameter, accepting it if there is trailing and leading whitespace, but not if there is a leading character.
        if re.search(r'(^|\s)-t(?=\s|$)', message):
            #displays as 9:01 AM
            return ":t"
        
        elif re.search(r'(^|\s)-T(?=\s|$)', message):
            #displays as 9:01:00 AM
            return ":T"
        
        elif re.search(r'(^|\s)-d(?=\s|$)', message):
            #displays as 11/28/2018
            return ":d"
        
        elif re.search(r'(^|\s)-D(?=\s|$)', message):
            #displays as November 28, 2018
            return ":D"
        
        elif re.search(r'(^|\s)-f(?=\s|$)', message):
            #displays as November 28, 2018, 9:01 AM
            return ":f"
        
        elif re.search (r'(^|\s)-F(?=\s|$)', message):
            #displays as Wednesday, November 28, 2018, 9:01 AM
            return ":F"
        
        elif re.search(r'(^|\s)-R(?=\s|$)', message):
            #displays as 6 years ago
            return ":R"
        
        else:
            #Displays as November 28, 2018, 9:01 AM
            return ""
        
    #used for time_from_now and time_ago functions further down
    def time_input(self, message, timescale):
        #searches for years/months/weeks/etc inside of message string using regex
        #\d+\s captures any numbers to the left of the timescale separated by a whitespace
        print(f"Message: {message}")
        print(f"Timescale: {timescale}")
        match = re.search(rf"(\d+)\s*{timescale}", message, re.IGNORECASE)
        print(f"Match: {match}")
        if match:
            #returns the value of the first grouping in match, e.g. (\d+), the digits
            inputted_time = match.group(1)
            print(f"Inputted time: {inputted_time}")
        else:
            #user did not input time value to the left of timescale
            raise custom_exceptions.NoTimeValueError
        
        return int(inputted_time)

    #returns x time ago/from now. opeartor is 1 if in the future, -1 if in the past
    def time_calc(self, message, operator):
        #splits time so it has no miliseconds
        timer = str(time.time()).split(".")
        current_time = int(timer[0])

        #flag to be raised when a pattern is found. if not raise, exception happens at end of method
        pattern_found = False

        try:
            #dictionary regex for every possible time combination. [s]? allows for the time to be plural optionally.
            #the value represents the seconds in each timescale. e.g. there are 60 seconds in a minute.
            time_patterns = {
                "year[s]?": 31536000,
                #extra check to ensure y is not preceded by a letter
                "(?<![a-zA-Z\d])y[s]?": 31536000,

                "month[s]?": 2628288,
                "mon[s]?": 2628288,

                "week[s]?": 604800,
                #extra check to ensure w is not the end of the string
                "w[s]?(?!$)": 604800,

                "day[s]?": 86400,
                #extra check to ensure d is not preceded by -
                "(?<!-)d[s]?": 86400,

                "hour[s]?": 3600,
                #extra check to ensure h is not preceded by a letter
                "(?<![a-zA-Z\d])h[s]?": 3600,

                "minute[s]?": 60,
                #extra check to ensure m is not preceded by a letter
                "(?<![a-zA-Z\d])m[s]?": 60,
                
                "second[s]?": 1,
                #only checks s if it is preceded by either a digit or a whitespace
                "(?<=\d|\s)s[s]?": 1
            }
            
            for pattern, seconds in time_patterns.items():
                #if the pattern (e.g. year[s]? is found in the message)
                if re.search(pattern, message, re.IGNORECASE):
                    current_time += (operator * self.time_input(message, pattern) * seconds)
                    pattern_found = True
            
            if not pattern_found:
                raise custom_exceptions.NoTimeStringError
        
        except custom_exceptions.NoTimeValueError:
            raise custom_exceptions.NoTimeValueError
        
        return current_time