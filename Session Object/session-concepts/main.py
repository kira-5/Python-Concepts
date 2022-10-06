import requests
from monitoring.custom_logger import get_logger

logger = get_logger(__name__)


def update_header():
    """Update header at session level"""
    s = requests.Session()
    s.headers.update({'accept': 'api'})
    res = s.get('https://httpbin.org/headers', headers={'x_header': 'true'})
    logger.info(res.text)
# Returns:
# {
#   "headers": {
#     "Accept": "api",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.28.1",
#     "X-Amzn-Trace-Id": "Root=1-633e4ab1-3824fe8755033e7c74e038c7",
#     "X-Header": "true"
#   }
# }


def persist_cookies():
    s = requests.Session()
    s.get('https://httpbin.org/cookies/set/sessioncookie/datagyiscool')
    resp = s.get('https://httpbin.org/cookies')
    logger.info(resp.text)
# Returns:
# {
#   "cookies": {
#     "sessioncookie": "datagyiscool"
#   }
# }


def authentication():
    s = requests.Session()
    s.auth = ('user', 'pass')
    s.get('https://httpbin.org/headers')
    logger.info(s)


if __name__ == '__main__':
    update_header()
    persist_cookies()
    authentication()
