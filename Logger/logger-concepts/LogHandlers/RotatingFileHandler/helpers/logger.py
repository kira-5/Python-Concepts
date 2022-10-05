import logging
from logging.handlers import RotatingFileHandler

"""
    When you have a large application that logs many events to a file, and you only need to keep track of the most recent events, then use a RotatingFileHandler that keeps the files small. When the log reaches a certain number of bytes, it gets "rolled over". You can also keep multiple backup log files before overwriting them.
"""


def customLogger(module_name: str = None):
    if module_name:
        # create logger
        logger = logging.getLogger(module_name)

        # set logging level
        logger.setLevel(logging.DEBUG)

        # create rotating file handler and set level to debug
        handler = RotatingFileHandler(
            'logs/my_log.log', maxBytes=2000, backupCount=10)
        handler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter(
            "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")

        # add formatter to rotating file handler
        handler.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(handler)

        return logger
