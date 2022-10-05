import imp
import logging
from my_app import app


def main():
    # logging.basicConfig(level=logging.DEBUG,
    #                     format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s", datefmt='%m/%d/%y %H:%M:%S %p')
    logging.info('Started')
    app.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()
