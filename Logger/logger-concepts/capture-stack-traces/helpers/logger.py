import logging


def customLogger(module_name: str = None):
    if module_name:
        # create logger
        logger = logging.getLogger(module_name)

        # set logging level
        logger.setLevel(logging.DEBUG)

        # Create the Handler for log messages to a file
        handler = logging.FileHandler(
            'logs/my_log.log')
        handler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter(
            "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")

        # add formatter to rotating file handler
        handler.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(handler)

        return logger
