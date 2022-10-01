"""
    ! Preserving the Original Name and Docstring of the Decorated Function:
    
       ? As the say_hello now points to the wrapper function, it is showing its information instead of the original function.
       
         * Use the functools.wraps decorator to preserve the original name and docstring of the decorated function
            ? @functools.wraps(func)
"""


import functools


def decorator(func):
    def wrapper():

        print("This is printed before the function is called")
        func()
        print("This is printed after the function is called")

    return wrapper


@decorator
def say_hello():
    """This function says hello when called"""
    print("Hello! The function is executing")


if __name__ == '__main__':

    print('say_hello() points to wrapper:')
    print(say_hello.__name__)
    help(say_hello)
    print('-'*50)


"""
    ! Explanation:
    
       ? To fix this, we need to use another decorator called wraps on the wrapper function.
       
       * The wraps decorator is imported from the in-built functools modules.
            ? @functools.wraps(func)
"""


def decorator1(func):
    @functools.wraps(func)
    def wrapper():
        print("This is printed before the function is called")
        func()
        print("This is printed after the function is called")

    return wrapper


@decorator1
def say_hello1():
    """This function says hello when called"""
    print("Hello! The function is executing")


if __name__ == '__main__':

    print('say_hello() points to original func:')
    print(say_hello1.__name__)
    help(say_hello1)


"""
    ! Explanation:
    
       ? This time, we got the correct docstring from the help function and the correct name from the __name__ attribute.
       
       * Use the functools.wraps decorator to preserve the original name and docstring of the decorated function
            ? @functools.wraps(func)
"""
