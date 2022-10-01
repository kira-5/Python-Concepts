import logging
import sys

formatter = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
log_file = "logs/my_app.log"


# Set up root logger, and add a file handler to root logger
logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode='w')


def custom_logger():
    logging.debug("Debug message")
    logging.info("Informative message")
    logging.error("Error message")


custom_logger()
