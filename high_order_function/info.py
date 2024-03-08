# A higher-order function is a function that does at least one of the following:

    # Takes one or more functions as arguments (i.e., it treats functions as first-class citizens).
    # Returns a function as its result.

    
# Here's an explanation of each:

    # Takes Functions as Arguments:

        # In languages that support functions as first-class citizens (like Python), functions can be passed as arguments to other functions.
        # Higher-order functions take advantage of this by accepting functions as parameters.
        # This allows for abstraction and flexibility in writing code.


# What if we have to implement same in traditional way
print('Using traditional way:')
def apply_operation(operation, x, y):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y

result_add = apply_operation('add', 5, 3)  # Passing add function as an argument
result_subtract = apply_operation('subtract', 5, 3)  # Passing subtract function as an argument
print(result_add)
print(result_subtract)

print('#'*50)
print('Using HOF:')
# Insetead of doing in this way, we can use HOF
def apply_operation(operation, x, y):
    return operation(x, y)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

result_add = apply_operation(add, 5, 3)  # Passing add function as an argument
result_subtract = apply_operation(subtract, 5, 3)  # Passing subtract function as an argument
print(result_add)
print(result_subtract)