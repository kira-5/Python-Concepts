""
import functools
from time import time, sleep


def measure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        execution_time = time() - t
        print(f"{func.__name__} took {execution_time}")
    return wrapper


@measure
def sleepy_function(sleep_time):
    sleep(sleep_time)


if __name__ == '__main__':
    sleepy_function(0.3)
