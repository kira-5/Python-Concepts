
"""
    ! Inner Functions
    
       ? We can define a function inside other functions. Such functions are called inner functions or nested functions. Decorators in Python also use inner functions.
       
       ? The inner functions are locally scoped to the parent. They are not available outside of the parent function. If you try calling the first_child outside of the parent body, you will get a NameError.
       
       ? Inner functions can access variables in the outer scope of the enclosing function. This pattern is known as a Closure i.e. variable value pass to outer function.
"""


def parent():
    print("I am the parent function")

    def first_child():
        print("I am the first child function")

    def second_child():
        print("I am the second child function")

    first_child()
    second_child()


if __name__ == '__main__':
    parent()
