# Chaining Methods
# Demonstrate how methods can be chained together to perform multiple operations in a single line of code.
# Highlight the benefits of method chaining for code readability and expressiveness.


class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, x):
        self.value += x
        return self  # Return self to enable method chaining

    def subtract(self, x):
        self.value -= x
        return self  # Return self to enable method chaining

    def multiply(self, x):
        self.value *= x
        return self  # Return self to enable method chaining

    def divide(self, x):
        self.value /= x
        return self  # Return self to enable method chaining


if __name__ == "__main__":
    result = Calculator(10).add(5).subtract(3).multiply(2).divide(4).value
    print(result)  # Output: 4.5



# Method chaining allows you to call multiple methods on an object in a single line of code, chaining the output of one method call as the input for the next.
# method chaining is a powerful technique for especially when dealing with sequences of operations on objects.
# Purpose: Code Organization, Readability, Maintainability, Reusability
# Use Cases: Mathematical Calculations, API Client Libraries, File Handling, Data Processing