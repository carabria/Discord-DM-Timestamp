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
        print("hit time_input")
        print(f"Message: {message}")
        #searches for years/months/weeks/etc inside of message string using regex
        #\d+\s captures any numbers to the left of the timescale separated by a whitespace
        match = re.search(rf"(\d+)\s*{timescale}?", message)
        print(f"Match: {match}")

        if match:
            print ("hit if statement")
            #returns the value of the first grouping in match, e.g. (\d+), the digits
            inputted_time = match.group(1)
        else:
            #user did not input time value to the left of timescale
            raise custom_exceptions.NoTimeValueError
        
        return int(inputted_time)

    #returns x time from now
    def time_from_now(self, message):
        #splits time so it has no miliseconds
        timer = str(time.time()).split(".")
        current_time = int(timer[0])
        print(f"current time before methods: {current_time}")
        try:
            #flag to see if any condition was satisfied
            condition_met = False
            #regex finds year/s, month/s, etc in message and sends into time_input function for calculation
            if re.search(r"year[s]?", message):
                #31536000 seconds in a year
                current_time += (self.time_input(message, "year[s]") * 31536000)
                condition_met = True

            if re.search(r"month[s]?", message):
                #2628288 seconds in a month
                current_time += (self.time_input(message, "month[s]") * 2628288)
                condition_met = True

            if re.search(r"week[s]?", message):
                #604800 seconds in a week
                current_time += (self.time_input(message, "week[s]") * 604800)
                condition_met = True

            if re.search(r"day[s]?", message):
                #86400 seconds in a day
                current_time += (self.time_input(message, "day[s]") * 86400)
                condition_met = True

            if re.search(r"hour[s]?", message):
                #3600 seconds in an hour
                current_time += (self.time_input(message, "hour[s]") * 3600)
                condition_met = True
                

            if re.search(r"minute[s]?", message):
                #60 seconds in a minute
                current_time += (self.time_input(message, "minute[s]") * 60)
                condition_met = True

            if re.search(r"second[s]?", message):
                current_time += self.time_input(message, "second[s]")
                condition_met = True
            
            if not condition_met:
                #user inputted time string wrong
                raise custom_exceptions.NoTimeStringError
            
        except custom_exceptions.NoTimeValueError:
            raise custom_exceptions.NoTimeValueError
        
        return current_time

    #returns x time ago    
    def time_ago(self, message):
        #splits time so it has no miliseconds
        timer = str(time.time()).split(".")
        current_time = int(timer[0])

        try:
            #flag to see if any condition was satisfied
            condition_met = False
            #regex finds year/s, month/s, etc in message and sends into time_input function for calculation
            if re.search(r"year[s]?", message):
                #31536000 seconds in a year
                current_time -= (self.time_input(message, "year[s]") * 31536000)
                condition_met = True

            if re.search(r"month[s]?", message):
                #2628288 seconds in a month
                current_time -= (self.time_input(message, "month[s]") * 2628288)
                condition_met = True

            if re.search(r"week[s]?", message):
                #604800 seconds in a week
                current_time -= (self.time_input(message, "week[s]") * 604800)
                condition_met = True

            if re.search(r"day[s]?", message):
                #86400 seconds in a day
                current_time -= (self.time_input(message, "day[s]") * 86400)
                condition_met = True

            if re.search(r"hour[s]?", message):
                #3600 seconds in an hour
                current_time -= (self.time_input(message, "hour[s]") * 3600)
                condition_met = True

            if re.search(r"minute[s]?", message):
                #60 seconds in a minute
                current_time -= (self.time_input(message, "minute[s]") * 60)
                condition_met = True

            if re.search(r"second[s]?", message):
                current_time -= self.time_input(message, "second[s]")
                condition_met = True
            
            
            if not condition_met:
                #user inputted time string wrong
                raise custom_exceptions.NoTimeStringError
            
        except custom_exceptions.NoTimeValueError:
            raise custom_exceptions.NoTimeValueError
        
        return current_time