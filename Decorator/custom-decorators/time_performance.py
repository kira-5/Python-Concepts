
from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        time_taken = 0
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        time_taken = t2-t1
        print(f'Took {time_taken} ms')
        return result
    return wrapper


@performance
def long_time():
    # sourcery skip: inline-immediately-returned-variable, sum-comprehension

    ans = 0
    for i in range(100000000):
        ans += i*5
    return ans


long_time()
