import logging
from helpers.logger import customLogger
from helpers import logger


def do_something():
    # create logger
    logger = customLogger(__name__)
    user_info = {
        'user_id': 1,
        'user_name': 'kira'
    }
    for _ in range(3):
        logger.debug('debug message', extra=user_info)
        logger.debug('debug1 message')
