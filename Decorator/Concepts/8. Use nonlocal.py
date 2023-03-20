"""
    ! Use nonlocal:

       ? you will often encounter situations where the inner function needs to modify the variables of the outer function.

"""
import functools


def counter(func):
    count = 0

    @functools.wraps(func)
    def decorated(*args, **kwargs):
        count += 1
        print(f"Count: {count}")
        return func(*args, **kwargs)
    return decorated


@counter
def foo():
    pass


"""
    ! Explanation:

       ? When the interpreter executes to count += 1, it does not know that count is a variable defined in the outer scope, it treats count as a local variable and looks it up in the current scope.
       
        * In order to solve this problem, we need to tell the interpreter through the nonlocal keyword :
            ?  "count variable does not belong to the current local scope, go look outside" , the previous error can be solved.
"""


def counter1(func):
    count = 0

    @functools.wraps(func)
    def decorated1(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Count: {count}")
        return func(*args, **kwargs)
    return decorated1


@counter1
def foo1():
    pass


if __name__ == '__main__':
    foo1()

"""
        ! Takeaway:
            * When the inner function modifies the variables of the outer function, you need to use the nonlocal keyword
    """
