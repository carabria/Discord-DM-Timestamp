import time
import re
from actions import custom_exceptions

class Actions:
    #returns the current time
    def current_time():
        #splits time so it has no miliseconds
        timer = str(time.time()).split(".")
        return int(timer[0])
    
    #checks to see if -t, -T, etc is contained in the message, then returns a string for the proper format
    def formatter(message):
        if re.search(r'-[t]', message):
            #displays as 9:01 AM
            return ":t"
        elif re.search(r'-[T]', message):
            #displays as 9:01:00 AM
            return ":T"
        elif re.search(r'-[d]', message):
            #displays as 11/28/2018
            return ":d"
        elif re.search(r'-[D]', message):
            #displays as November 28, 2018
            return ":D"
        elif re.search(r'-[f]', message):
            #displays as November 28, 2018, 9:01 AM
            return ":f"
        elif re.search (r'-[F]', message):
            #displays as Wednesday, November 28, 2018, 9:01 AM
            return ":F"
        elif re.search(r'-[R]', message):
            #displays as 6 years ago
            return ":R"
        else:
            #Displays as November 28, 2018, 9:01 AM
            return ""
        
    #returns x time from now
    def time_from_now(message):
        #splits message so each individual part of the command can be called
        message_list = message.split(" ")
        #splits time so it has no miliseconds
        timer = str(time.time()).split(".")
        current_time = int(timer[0])
        inputted_time = ""

        #the number inputted into the command
        for c in message_list[1]:
            if c.isdigit():
                #keep as string to easily convert values like 10 later
                inputted_time += c
            else:
                break
        try:
            inputted_time = int(inputted_time)
        except ValueError:
            #user inputted number wrong
            raise custom_exceptions.NoTimeValueError

        #message_list[2] is the measurement of time in the command e.g. days/months etc
        if re.match(r"second[s]?", message_list[2]):
            return current_time + inputted_time
        
        elif re.match(r"minute[s]?", message_list[2]):
            #60 seconds in a minute
            return current_time + (inputted_time * 60)
        
        elif re.match(r"hour[s]?", message_list[2]):
            #3600 seconds in an hour
            return current_time + (inputted_time * 3600)
        
        elif re.match(r"day[s]?", message_list[2]):
            #86400 seconds in a day
            return current_time + (inputted_time * 86400)
        
        elif re.match(r"week[s]?", message_list[2]):
            #604800 seconds in a week
            return current_time + (inputted_time * 604800)
        
        elif re.match(r"month[s]?", message_list[2]):
            #2628288 seconds in a month
            return current_time + (inputted_time * 2628288)
        
        elif re.match(r"year[s]?", message_list[2]):
            #31536000 seconds in a year
            return current_time + (inputted_time * 31536000)
        
        else:
            #user inputted time string wrong
            raise custom_exceptions.NoTimeStringError

    #returns x time ago    
    def time_ago(message):
        #splits message so each individual part of the command can be called
        message_list = message.split(" ")
        #splits time so it has no miliseconds
        timer = str(time.time()).split(".")
        current_time = int(timer[0])
        inputted_time = ""

        #the number inputted into the command
        for c in message_list[1]:
            if c.isdigit():
                #keep as string to easily convert values like 10 later
                inputted_time += c
            else:
                break
        try:
            inputted_time = int(inputted_time)
        except ValueError:
            #user inputted number wrong
            raise custom_exceptions.NoTimeValueError

        #message_list[2] is the measurement of time in the command e.g. days/months etc
        if re.match(r"second[s]?", message_list[2]):
            return current_time - inputted_time
        
        elif re.match(r"minute[s]?", message_list[2]):
            #60 seconds in a minute
            return current_time - (inputted_time * 60)
        
        elif re.match(r"hour[s]?", message_list[2]):
            #3600 seconds in an hour
            return current_time - (inputted_time * 3600)
        
        elif re.match(r"day[s]?", message_list[2]):
            #86400 seconds in a day
            return current_time - (inputted_time * 86400)
        
        elif re.match(r"week[s]?", message_list[2]):
            #604800 seconds in a week
            return current_time - (inputted_time * 604800)
        
        elif re.match(r"month[s]?", message_list[2]):
            #2628288 seconds in a month
            return current_time - (inputted_time * 2628288)
        
        elif re.match(r"year[s]?", message_list[2]):
            #31536000 seconds in a year
            return current_time - (inputted_time * 31536000)
        
        else:
            #user inputted time string wrong
            raise custom_exceptions.NoTimeStringError