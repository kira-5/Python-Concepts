# Method Decorators
# Discuss method decorators, which are functions that modify the behavior of methods.
# Explain popular method decorators like @property, @classmethod, @staticmethod, and their use cases.


# @property
class Circle:
    class_variable = 50
    
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

    @classmethod
    def class_method(cls):
        return cls.class_variable

    @staticmethod
    def add(x, y):
        return x + y


if __name__ == "__main__":
    circle = Circle(5)
    print(circle.radius)  # Output: 5
    circle.radius = 10
    print(circle.radius)  # Output: 10

    print(Circle.class_method())  # Output: 10

    print(Circle.add(5, 3))  # Output: 8


# @property:
# The @property decorator is used to define getter, setter, and deleter methods for a class attribute.
# It allows you to access, set, and delete an attribute as if it were a property, providing control over attribute access.
# Use cases:
# Encapsulating attribute access to add validation logic.
# Providing read-only or calculated properties.
# Lazily loading data.
# Access Control
# Computed Attributes
# Validation and maintain data integrity


# @classmethod:
# The @classmethod decorator is used to define methods that operate on the class itself rather than instances of the class.
# It receives the class (cls) as the first argument instead of the instance (self).
# Use cases:
# Alternative constructors.
# Factory methods.
# Accessing or modifying class-level attributes.


# @staticmethod:
# The @staticmethod decorator is used to define static methods within a class.
# It does not receive any implicit first argument (neither self nor cls).
# Static methods are similar to regular functions but are defined within a class for better organization.
# Use cases:
# Grouping utility functions related to the class.
# Methods that do not need access to instance or class attributes.


# Data Integrity and validation
# We want to ensure that the age attribute is always positive and the email attribute follows a valid email format. We can achieve this using getter and setter methods with the @property decorator.
import re

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self._age = age  # Private attribute for age
        self._email = email  # Private attribute for email

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be positive")
        self._age = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if not email_pattern.match(value):
            raise ValueError("Invalid email format")
        self._email = value

# Usage
person1 = Person("Alice", 30, "alice@example.com")
print(person1.age)  # Output: 30
person1.age = 35  # Setting age using setter
print(person1.age)  # Output: 35

person2 = Person("Bob", -25, "invalid-email")  # Raises ValueError: Age must be positive

person3 = Person("Charlie", 40, "charlie@example.com")
print(person3.email)  # Output: charlie@example.com
person3.email = "invalid-email"  # Raises ValueError: Invalid email format


# Access Control:
# Getter and setter methods can be used to control access to attributes, implementing read-only or write-only properties.
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

# Usage
account = BankAccount(100)
print(account.balance)  # Output: 100
account.balance = 150  # Setter allows modifying balance
print(account.balance)  # Output: 150
account.balance = -50  # Raises ValueError: Balance cannot be negative


# Lazy Loading:
# Getter methods can be used to load data from external sources only when requested, allowing for lazy initialization of attributes.
class LazyLoadData:
    def __init__(self, filename):
        self.filename = filename
        self._data = None

    @property
    def data(self):
        if self._data is None:
            self._data = self.load_data_from_file(self.filename)
        return self._data

    def load_data_from_file(self, filename):
        # Code to load data from file
        pass

# Usage
data_obj = LazyLoadData("data.txt")
print(data_obj.data)  # Data is loaded from file on first access
