import logging


def evenCount(lst):
    logger = logging.getLogger('even_count')
    n = len(lst)
    count = 0
    for i in range(n):
        iter_logger = logging.getLogger('even_count.iter')
        iter_logger.info('Current Element: %s', lst[i])
        if lst[i] & 1 == 0:
            count += 1
    logger.info('Even count in list: %s', count)
    return count


# Create logger and assign handler
logger = logging.getLogger("even_count")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger = logging.getLogger("even_count.iter")
logger.setLevel(logging.INFO)


lst = [1, 2, 3, 4, 5, 6]
evenCount(lst)
