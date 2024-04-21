# Special Methods(Magic Methods)
# Introduce special methods, also known as magic methods or dunder methods, which allow classes to emulate built-in Python behavior.
# Cover common special methods such as __str__, __repr__, __len__, __add__, etc., and how they are used.


class MagicMethods:

    def __init__(self, value):
        print("Initializing MyClass instance...")
        self.value = value

    def __str__(self):
        return f"MagicMethods object with value: {self.value}"

    def __repr__(self):
        return f"MagicMethods: {self.value}"

    def __add__(self, other):
        return MagicMethods(self.value + other.value)

    def __sub__(self, other):
        return MagicMethods(self.value - other.value)

    def __mul__(self, other):
        return MagicMethods(self.value * other.value)

    def __truediv__(self, other):
        return MagicMethods(self.value / other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __len__(self):
        return len(str(self.value))


if __name__ == "__main__":
    # Use case: Performing operations and comparisons with MagicMethods objects
    obj1 = MagicMethods(10)
    obj2 = MagicMethods(5)

    # String Representation
    print(str(obj1))  # Output: MyClass object with value: 10
    print(repr(obj1))  # Output: MyClass(10)

    # Non class Based
    import datetime
    currentDateTime = datetime.datetime.now()
    print(currentDateTime.__str__())

    # Arithmetic operations
    add_result = obj1 + obj2
    sub_result = obj1 - obj2
    mul_result = obj1 * obj2
    div_result = obj1 / obj2

    print("Addition result:", add_result)  # Output: MagicMethods object with value: 15
    print(
        "Subtraction result:", sub_result
    )  # Output: MagicMethods object with value: 5
    print(
        "Multiplication result:", mul_result
    )  # Output: MagicMethods object with value: 50
    print("Division result:", div_result)  # Output: MagicMethods object with value: 2.0

    # Comparisons
    print("obj1 == obj2:", obj1 == obj2)  # Output: False
    print("obj1 < obj2:", obj1 < obj2)  # Output: False
    print("obj1 > obj2:", obj1 > obj2)  # Output: True
    print("obj1 <= obj2:", obj1 <= obj2)  # Output: False
    print("obj1 >= obj2:", obj1 >= obj2)  # Output: True

    # Length (__len__)
    print(len(obj1))


# Special methods, often referred to as magic methods or dunder methods.
# They are denoted by enclosing their names within double underscores (__).

# Initialization (__init__):
# This method is called automatically when you create a new instance of a class.

# String Representation (__str__ and __repr__):
# __str__ is called when you use str() function or print() function on an object.
# __repr__ is called when you use repr() function or when an object is displayed in the interpreter.
# You can see the __str__ as a method for end users and __repr__ as a method for developers.

# Arithmetic Operations (__add__, __sub__, __mul__, __truediv__, etc.):
# These methods are called when you perform arithmetic operations such as addition (+), subtraction (-), multiplication (*), and division (/) on objects.

# Comparisons (__eq__, __lt__, __gt__, __le__, __ge__):
# These methods are called when you perform comparison operations such as equality (==), less than (<), greater than (>), etc., on objects.
# Length (__len__):
# This method is called when you use the len() function on an object.
