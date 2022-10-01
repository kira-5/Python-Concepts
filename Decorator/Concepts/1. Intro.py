"""
    ! Python decorators
    
       ? A Decorator is just a function that takes another function as an argument and extends its behavior without explicitly modifying it.
       
       ? A decorator in Python is a function that takes another function as an argument and extends its behavior without explicitly modifying it. It is one of the most powerful features of Python. It has several usages in the real world like logging, debugging, authentication, measuring execution time, and many more.
       
       ?  A decorator function modifies a function by wrapping it in a wrapper function.
       
       * Use Case:
            ? Suppose, you have a set of functions and you only want authenticated users to access them.Therefore, you need to check whether a user is authenticated or not before proceeding with the rest of the code in the function.

           ? One way to do this is by calling a separate function inside all the functions and using conditional statements. But this will require us to change the code for each function.
            *A better solution here would be to use a Decorator.
            
            
        * Syntax:
            ? func = decorator(func)
            ? where func is the function being decorated and decorator is the function used to decorate it.
            
        ? A decorator is just a regular Python function. Hence, we can reuse it to decorate multiple functions
            * View Best Practise folder
"""


def decorator(func):

    def wrapper():
        print('Normal Decorator:')
        print("This is printed before the function is called")
        func()
        print("This is printed after the function is called")
        print('-'*50)

    return wrapper


def say_hello():
    print("Hello! The function is executing")


if __name__ == '__main__':

    say_hello = decorator(say_hello)
    say_hello()

"""
    ! Explanation:
    
       ? wrapper: This is the actual function that does the modification by wrapping the passed function func.
       
       ? say_hello: This is an ordinary function that we need to decorate. Here, all it does is print a simple statement.
       
       * say_hello = decorator(say_hello):
            ? We passed the say_hello function to the decorator function. In effect, the say_hello now points to the wrapper function returned by the decorator.

           ? However, the wrapper function has a reference to the original say_hello() as func, and calls that function between the two calls to print().
"""

"""
    ! Syntactic Decorator:
    
       ? The above decorator pattern got popular in the Python community but it was a little inelegant. We have to write the function name thrice and the decoration gets a bit hidden below the function definition.
       
       ? Therefore, Python introduced a new way to use decorators by providing syntactic sugar with the @ symbol.
       
       * Syntax::
            ? @decorator
                def func(arg1, arg2, ...):
                    pass

        ? Syntactic sugar is syntax within a programming language that is designed to make things easier to read or to express.
           
        ? using @decorator instead of say_hello = decorator(say_hello).
"""


def decorator(func):
    def wrapper():
        print('Syntactic Decorator:')
        print("This is printed before the function is called")
        func()
        print("This is printed after the function is called")

    return wrapper


@decorator
def say_hello():
    print("Hello! The function is executing")


if __name__ == '__main__':

    say_hello()
