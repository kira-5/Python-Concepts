import logging
from helpers.logger import customLogger
import time


def do_something():
    # create logger
    logger = customLogger(__name__)
    for _ in range(5):
        logger.debug('debug message')
        # time.sleep(5)
