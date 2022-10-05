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

        # Need to pass filter else, we have must pass extra arguments in logger.info("message")
        # If doesn't want to pass the filter then we have to modify formatter based on condition, if etra is none then pass this formatter else pass the required one
        # logger.addFilter(SystemLogFilter())

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

        return logger
