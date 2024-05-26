import time
import re

class Actions:
    def current_time():
        timer = str(time.time()).split(".")
        return int(timer[0])
    
    def time_from_now(message):
        message_list = message.split(" ")
        timer = str(time.time()).split(".")
        current_time = int(timer[0])

        inputted_time = 0
        #the number inputted into the command
        for c in message_list[1]:
            if c.isdigit():
                inputted_time += int(c)
            else:
                break

        #the measurement of time in the command e.g. days/months etc
        if re.match(r"hour[s]?", message_list[2]):
            #3600 seconds in an hour
            return current_time + (inputted_time * 3600)