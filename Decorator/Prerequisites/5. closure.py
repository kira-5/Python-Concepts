
"""
    ! Closure
    
       ? Inner functions can access variables in the outer scope of the enclosing function. This pattern is known as a Closure.
       
       ? The message is remembered by the inner function even after the outer function has finished executing. This technique by which some data gets attached to the code is called closure in Python.
"""


def outer(message):

    def inner():
        print(f"Message: {message}")

    return inner


if __name__ == '__main__':

    hello_msg = outer('Hello!')
    hello_msg()
    bye_msg = outer('Bye!')
    bye_msg()
