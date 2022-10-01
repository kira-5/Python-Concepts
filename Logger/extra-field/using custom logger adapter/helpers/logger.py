import logging


class LoggerAdapter(logging.LoggerAdapter):
    def __init__(self, logger, prefix):
        super(LoggerAdapter, self).__init__(logger, {})
        self.prefix = prefix

    def process(self, msg, kwargs):
        # return '[%s] %s' % (self.prefix, msg), kwargs
        return f'{msg} [{self.prefix}]', kwargs


def customLogger(module_name: str = None):

    if module_name:
        # create logger
        logger = logging.getLogger(module_name)

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

        # add ch to logger
        logger.addHandler(handler)
        user_info = None

        # You could use a LoggerAdapter so you don't have to pass the extra info with every logging call:
        logger = LoggerAdapter(logger, user_info)

        return logger
