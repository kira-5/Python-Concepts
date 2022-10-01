import logging


FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
LOG_FILE = "my_app.log"
LOG_PATH = f"logs/{LOG_FILE}"


class InfoFilter(logging.Filter):

    # overwrite this method. Only log records for which this
    # function evaluates to True will pass the filter.
    def filter(self, record):
        return record.levelno >= logging.INFO


def get_console_handler():
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(FORMATTER)
    console_handler.addFilter(InfoFilter())
    return console_handler


def get_file_handler():
    file_handler = logging.FileHandler(LOG_PATH)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(FORMATTER)
    file_handler.addFilter(InfoFilter())
    return file_handler


def get_logger(module_name: str = None):
    if module_name:
        logger = logging.getLogger(module_name)

        # set logging level
        level = logging.getLevelName('DEBUG')
        logger.setLevel(level)

        # Add handler to logger
        logger.addHandler(get_console_handler())
        logger.addHandler(get_file_handler())

        logger.propagate = False
        return logger
