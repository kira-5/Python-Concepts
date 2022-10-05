import logging


class SystemLogFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'user_id'):
            record.user_id = '--'
            record.user_name = '--'
        return True


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
            "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s — [user_id:%(user_id)s]  — [user_name:%(user_name)s]")

        # add formatter to rotating file handler
        handler.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(handler)
        user_info = {
            'user_id': 1,
            'user_name': 'kira'
        }

        # You could use a LoggerAdapter so you don't have to pass the extra info with every logging call:
        logger = logging.LoggerAdapter(logger, extra=user_info)

        return logger
