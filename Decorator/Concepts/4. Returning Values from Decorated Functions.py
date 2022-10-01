"""
    ! Returning Values from Decorated Functions:

       * What happens to the returned value from the decorated function?

"""
import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


@do_twice
def add(num1, num2):
    print(f"Adding {num1} and {num2}")
    return num1 + num2


if __name__ == '__main__':
    print("Wrapper func doesn't return anything:")
    print("The sum is:", add(1, 2))
    print('-'*50)


"""
    ! Explanation:
    
       ? The add function was called  as expected but we got None in the return value. This is because the wrapper function does not return any value.

        * To fix this, we need to make sure the wrapper function returns the return value of the decorated function.
"""


def do_twice1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@do_twice1
def add(num1, num2):
    print(f"Adding {num1} and {num2}")
    return num1 + num2


if __name__ == '__main__':

    print("Wrapper func return anything:")
    print("The sum is:", add(1, 2))

"""
        ! Takeaway:
            * The wrapper function should return the return value of the decorated function, otherwise, it would be lost.
    """
