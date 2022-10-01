"""
    ! Chaining Decorators:
       
       ? Chaining the decorators means that we can apply multiple decorators to a single function. These are also called nesting decorators.

"""
import functools


def split_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).split()

    return wrapper


def to_upper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


@split_string
@to_upper
def say_hello(name):
    print(f"Hello, {name}!")


if __name__ == '__main__':
    say_hello("Kitty")


"""
    ! Explanation:
    
       ? The order of the decorators' matters in this case. First to_upper is applied to the say_hello function. Then, split_string is applied.
            * @split_string
                @to_upper
            * say_hello = split_string(to_upper(say_hello))
"""

"""
        ! Takeaway:
            * You can apply multiple decorators to a single function by stacking them on top of each other.
    """
