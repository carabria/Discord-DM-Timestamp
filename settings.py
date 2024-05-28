import os
from dotenv import load_dotenv
from logging.config import dictConfig

load_dotenv(".bot_token.env")
TOKEN = os.getenv("TOKEN")

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard": {
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers": {
        "console_debug": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "console_warning": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/discord.log",
            "formatter": "verbose"
        }
    },
    "loggers": {
        "bot": {
            "handlers": ["console_debug", "console_warning", "file"],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            "handlers": ["console_warning", "file"],
            "level": "INFO",
            "propagate": False
        }
    }
}

dictConfig(LOGGING_CONFIG)