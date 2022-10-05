import logging
import traceback
from helpers.logger import customLogger
from helpers import logger


def do_something(a, b):
    # create logger
    logger = customLogger(__name__)
    try:
        res = a + b
    except TypeError:
        logger.exception("TypeError occurred")
    else:
        return res


"""
    Logging the traceback in your exception logs can be very helpful for troubleshooting issues. You can capture the traceback in logging.error() by setting the excinfo* parameter to True.
"""


def demo():
    logger = customLogger(__name__)
    try:
        a = [1, 2, 3]
        value = a[3]
    except IndexError as e:
        # logger.error(e)
        logger.error(e, exc_info=True)


"""
    If you don't capture the correct Exception, you can also use the traceback.formatexc()* method to log the exception.
"""


def traceback():
    logger = customLogger(__name__)
    try:
        a = [1, 2, 3]
        value = a[3]
    except IndexError as e:
        logger.error(e, traceback.format_exc())


a = 10
b = 'b'
ans = do_something(a, b)
