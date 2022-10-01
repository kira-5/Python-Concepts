import logging
from logging.handlers import TimedRotatingFileHandler

"""
    If your application will be running for a long time, you can use a TimedRotatingFileHandler. This will create a rotating log based on how much time has passed. Possible time conditions for the when parameter are: - second (s) - minute (m) - hour (h) - day (d) - w0-w6 (weekday, 0=Monday) - midnight
"""


def customLogger(module_name: str = None):
    if module_name:
        # create logger
        logger = logging.getLogger(module_name)

        # set logging level
        logger.setLevel(logging.DEBUG)

        # create time rotating file handler and set level to debug
        # This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
        handler = TimedRotatingFileHandler(
            'logs/my_log.log', when='m', interval=1, backupCount=10)
        handler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter(
            "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")

        # add formatter to rotating file handler
        handler.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(handler)

        return logger
