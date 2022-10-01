
# ?  high order function(HOC) : Function that take function as a argument.
# ? HOC also return another function


def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func


print(greet(greet2))
