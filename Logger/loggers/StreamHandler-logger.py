import logging
from colorama import Fore, Back, Style

logger_name = 'parent'
logger_formatter = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")


# Create logger, set level, and add stream handler
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)
logger_handler = logging.StreamHandler()
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)


# Emit log message with color
logger.debug('Debug message')
logger.info(Fore.GREEN + 'Info message')
logger.warning(Fore.BLUE + 'Warning message')
logger.error(Fore.YELLOW + Style.BRIGHT + 'Error message')
logger.critical(Fore.RED + Back.YELLOW + Style.BRIGHT + 'Critical message')
print(Style.RESET_ALL)
