import logging
from helpers.logger import customLogger
from helpers import logger


def do_something():
    # create logger
    logger = customLogger(__name__)
    for _ in range(1000):
        logger.debug('debug message')
