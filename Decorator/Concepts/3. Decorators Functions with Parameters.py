"""
    ! Decorators Functions with Parameters:

       * What if the function we are decorating has some parameters?

"""
import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper():
        func()

    return wrapper


@do_twice
def say_hello(name):
    print(f"Hello, {name}!")


if __name__ == '__main__':
    print('Without variable number of parameters:')
    # say_hello("Kitty")
    print('-'*50)


"""
    ! Explanation:
    
       ? We got an error because the wrapper function we defined inside the decorator does not accept any argument.
       
       ? The straightforward way to solve this would be to let the wrapper accept one argument, but then we won't be able to use the do_twice decorator with a function with more than one argument.

        * So, a better solution is to accept a variable number of arguments in the wrapper function and then pass those arguments to the original function func.
"""


def do_twice1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


@do_twice1
def say_hello1(name):
    print(f"Hello, {name}!")


if __name__ == '__main__':
    print('With variable number of parameters:')
    say_hello1("Kitty")

    """
        ! Takeaway:
            * Use a variable number of parameters in the wrapper function to handle any number of arguments in the decorated function.
    """
