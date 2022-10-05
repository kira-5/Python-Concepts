from monitoring.custom_logger import get_logger

logger = get_logger(__name__)


def solve():
    logger.info("info")
    logger.debug("debug")
    logger.warning("warning")
    logger.error("Error")
    logger.critical("critical")
    
    
if __name__ == '__main__':
    solve()