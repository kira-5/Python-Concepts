# Method Overloading


# Method Overloading (Non-Class Based):
def add(a, b=0):
    return a + b


# Method Overloading (Class Based):
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


if __name__ == "__main__":
    # Calling the overloaded add function
    print(add(5))  # Output: 5 (default parameter b=0)
    print(add(5, 3))  # Output: 8 (b=3)

    print("-" * 50)

    calculator = Calculator()
    # print(calculator.add(2, 3))         # Error: TypeError (second add method is overwritten)
    print(calculator.add(2, 3, 4))


## Concept:
# Method overloading refers to the ability to define multiple methods within the same class, each with the same name but with different parameters.
# in Python, method overloading is not directly supported because Python does not support function or method overloading based on different parameter types or numbers.
# In Python, method overloading is achieved by defining multiple methods with the same name, but differing in the number or type of parameters
# However, only the latest defined method with a particular name is retained.
# Non class based: can be achieved by similar functionality by using default parameter values or variable arguments.
# class based: method overloading can be achieved within a class by defining multiple methods with the same name but different numbers of parameters.

# Python developers often prefer to define a single function with default parameter values or variable-length argument lists, rather than creating multiple overloaded versions of the same function. It leads to cleaner, more concise code with less redundancy.

# In python, method overloading can be achieve by
    # Default Parameter Values
    # Variable-Length Argument Lists - positional (*args) and keyword (**kwargs).
