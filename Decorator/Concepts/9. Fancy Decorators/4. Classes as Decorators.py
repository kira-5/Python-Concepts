from time import time, sleep
import functools

"""
    ! Classes as Decorators:

        ? We can also use a class as a decorator. 
        
        ? Classes are the best option to store the state of some data, so let's understand how to implement a stateful decorator with a class that will record the number of calls made for a function.
        
       * There are two requirements to make a class as a decorator:
            ? The __init__ function needs to take a function as an argument.

            ? The class needs to implement the __call__ method. This is required because the class will be used as a decorator and a decorator must be a callable object.
        
        ? Also note that we use functools.update_wrapper instead of functools.wraps in case of a class as a decorator.
"""

import functools


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello!")


if __name__ == '__main__':
    say_hello()

"""
    ! Explanation:
    
       ? After decoration, the __call__ method of the class is called instead of the say_hello method.
"""


"""
        ! Takeaway:
            * Classes can also be used as decorators by implementing the __call__ method and passing the function to __init__ as an argument.
    """
