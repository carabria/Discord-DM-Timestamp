import logging
from settings import LOGGING_CONFIG
from datetime import datetime

class DLogger:
    def __init__(self, logger_name):
        logging.config.dictConfig(LOGGING_CONFIG)
        self.logger = logging.getLogger(logger_name)
    
    def info(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logger.info(f"[{timestamp}] message")

    def error(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logger.error(f"[{timestamp}] message")