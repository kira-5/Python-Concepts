import logging
from monitoring.helpers.logger_filters import EnvPathFilter, PackagePathFilter
from monitoring.helpers.logger_adapter import LoggerAdapter
from monitoring.helpers.logger_handlers import get_debug_handler, get_error_handler

IS_DEBUG_LOGGER = True
IS_ERROR_LOGGER = True


def get_logger(module_name , log_name= None, msg=None):  # type: ignore
    if module_name:
        logger = logging.getLogger(log_name) if log_name else logging.getLogger(module_name)
        logger.setLevel(logging.DEBUG)
        logger.addFilter(EnvPathFilter())
        logger.addFilter(PackagePathFilter())
        if IS_DEBUG_LOGGER:
            logger.addHandler(get_debug_handler())
        if IS_ERROR_LOGGER:
            logger.addHandler(get_error_handler())
        logger_extra_msg = msg or '-'
        logger = LoggerAdapter(logger, logger_extra_msg)
        return logger