import time

class Actions:
    def current_time():
        timer = str(time.time()).split(".")
        return int(timer[0])