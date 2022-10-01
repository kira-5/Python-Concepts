import logging
import sys

logger_name = 'parent'
logger_formatter = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
log_file = "logs/my_app.log"

# Set up root logger, and add a file handler to root logger
logging.basicConfig(filename=log_file, level=logging.WARNING,
                    format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")

# Create logger, set level, and add stream handler
logger = logging.getLogger(logger_name)
logger.setLevel(logging.INFO)
logger_handler = logging.FileHandler('logs/parent.log')
logger_handler.setLevel(logging.WARNING)
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)


# Log message of severity INFO or above will be handled
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')
