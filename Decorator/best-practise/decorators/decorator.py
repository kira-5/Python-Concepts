import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper():
        func()

    return wrapper
