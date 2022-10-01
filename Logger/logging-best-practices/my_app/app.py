import logging
from helpers.logger import get_logger


def do_something():
    # create logger
    logger = get_logger(__name__)
    for _ in range(5):
        logger.debug('debug message')
        logger.info('Info message')
        logger.warning('Warning message')
        logger.error('Error message')
