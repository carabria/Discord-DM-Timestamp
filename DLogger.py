import logging
from settings import LOGGING_CONFIG

class DLogger:
    def _init_(self, logger_name):
        logging.config.dictConfig(LOGGING_CONFIG)
        self.logger = logging.get_logger(logger_name)
    
    def log(self):
        return self.logger