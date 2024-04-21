# Access Control
# Discuss access control in methods, including public, private, and protected methods.


# Non-class based methods
def public_method():
    print("This is a public method")


def _private_method():
    print("This is a private method")


# Class-based methods
class MyClass:
    def __init__(self):
        self._protected_attr = 10

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

    def call_private_method(self):
        self.__private_method()  # Name mangling used here


class MySubclass(MyClass):
    def call_protected(self):
        self._protected_method()


if __name__ == "__main__":
    public_method()  # Output: This is a public method
    _private_method()  # Output: This is a private method

    obj = MyClass()
    obj.call_private_method()  # Output: This is a private method
    obj._protected_method()  # This is technically valid but against convention
    print(obj._protected_attr)  # Output: 10



# Public Methods
# Purpose: Provide a well-defined interface for external code to interact with the class.
# When to Use: Expose functionalities of the class to external code, promoting encapsulation and abstraction.


# Private Methods
# Private methods are indicated by prefixing the method name with a single underscore (__).
# this convention signals to other developers that the method should not be accessed directly from outside the current module.
# Purpose: Hide internal implementation details and helper functions from external code.
# When to Use: Encapsulate internal logic or helper functions that are only relevant within the class itself.


# Protected Methods
# Protected methods are indicated by prefixing the method name with a single underscore (_), similar to private methods.
# Protected methods are accessible within the class itself and its subclasses.
# However, protected methods are intended for use within subclasses or related classes.
# Protected methods are often used to indicate that a method should only be overridden by subclasses and not directly called from outside.
# Purpose: Allow subclasses to access and potentially override certain behaviors while still restricting direct access from external code.
# When to Use: Indicate methods designed for internal use within the class hierarchy, allowing subclasses to customize or extend behavior while maintaining encapsulation.
# Use Case: User Authentication System, Bank Account Management System, Medical Records and Personal Data, File and Resource Managemen, User Permissions in Web Applications