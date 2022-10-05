import logging


class InfoFilter(logging.Filter):

    # overwrite this method. Only log records for which this
    # function evaluates to True will pass the filter.
    def filter(self, record):
        return record.levelno == logging.INFO


def customLogger(module_name: str = None):
    if module_name:
        # create logger
        logger = logging.getLogger(module_name)
        logger.propagate = False
        # set logging level
        logger.setLevel(logging.DEBUG)

        # sends log messages over HTTP
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter(
            "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")

        # add formatter to rotating file handler
        handler.setFormatter(formatter)

        # Now only INFO level messages will be logged
        handler.addFilter(InfoFilter())

        # add ch to logger
        logger.addHandler(handler)

        return logger
