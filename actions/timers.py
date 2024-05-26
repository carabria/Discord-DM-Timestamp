import time
import re
from actions import custom_exceptions

class Actions:
    def current_time():
        timer = str(time.time()).split(".")
        return int(timer[0])
    
    def time_from_now(message):
        message_list = message.split(" ")
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
            raise custom_exceptions.InputError

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
        
    def time_ago(message):
        message_list = message.split(" ")
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
            raise custom_exceptions.InputError

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