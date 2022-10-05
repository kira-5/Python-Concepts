from monitoring.custom_logger import get_logger

logger = get_logger(__name__)


def solve():
    logger.debug("Hello")
    
    
if __name__ == '__main__':
    solve()