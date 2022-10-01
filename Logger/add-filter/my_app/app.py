import logging
from helpers.logger import customLogger
from helpers import logger


def do_something():
    # create logger
    logger = customLogger(__name__)
    logger.propagate = False
    for _ in range(3):
        logger.debug('debug message')
        logger.info('Info message')
