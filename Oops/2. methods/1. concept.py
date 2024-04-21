# Notes: Methods

class Rectangle:
    def __init__(self, width, height):
        # Instance attributes
        self.width = width
        self.height = height
    
    # Instance method to calculate area
    def calculate_area(self):
        return self.width * self.height
    
    # Class method to create a square
    @classmethod
    def create_square(cls, side_length):
        return cls(side_length, side_length)
    
    # Static method to check if a shape is a square
    @staticmethod
    def is_square(shape):
        return shape.width == shape.height


# Explaining Methods
def explaining_methods():
    # Creating an instance of Rectangle
    rectangle = Rectangle(5, 4)
    
    # Calling the instance method to calculate area
    area = rectangle.calculate_area()
    print("Area:", area)
    
    # Calling the class method to create a square
    square = Rectangle.create_square(5)
    print("Is square:", Rectangle.is_square(square))

if __name__ == "__main__":
    explaining_methods()



# Methods: Methods define the behavior of objects in object-oriented programming.

# Types of Methods:
    # Instance Methods: Defined inside a class and operate on instances of that class.
    # Class Methods: Defined using the @classmethod decorator and operate on the class itself.
    # Static Methods: Defined using the @staticmethod decorator and don't access or modify class or instance state.

# Purpose of Methods:
    # Encapsulate behavior: Methods encapsulate the behavior associated with an object, promoting code organization and reusability.
    # Manipulate object state: Methods can manipulate the state (attributes) of an object, allowing for dynamic behavior.

# Example:
    # In the Rectangle class:
        # __init__ method initializes the width and height attributes of a rectangle.
        # calculate_area method calculates the area of the rectangle based on its width and height.
        # create_square class method creates a square with equal width and height.
        # is_square static method checks if a given shape is a square.


# Class methods working
    # When you call Rectangle.create_square(5), it invokes the create_square class method.
    # Inside the method, cls refers to the Rectangle class itself.
    # It then creates a new instance of Rectangle by calling cls(side_length, side_length), passing side_length twice as arguments. This effectively creates a square with both width and height equal to side_length.
    # Finally, this newly created square is returned.


    # @classmethod: This is a Python decorator used to define a class method. Class methods in Python are bound to the class itself rather than to instances of the class.
    # def create_square(cls, side_length): This defines the create_square class method. It takes two parameters: cls (which stands for class) and side_length.
    # return cls(side_length, side_length): This line creates a new instance of the class using the cls parameter (which refers to the class itself) and returns it. It effectively creates a square by instantiating the class with side_length provided twice, making both the width and height of the square equal to side_length.
    

# How to Define and Call Methods:
    # Instance Methods:
    #     How to call: Instance methods are called on instances of a class using dot notation.
    #     Example: rectangle.calculate_area()
    #     Why: Instance methods typically need access to the specific instance's attributes to perform their task, so they are called on instances.
    # Class Methods:
    #     How to call: Class methods can be called either on the class itself or on instances of the class, again using dot notation.
    #     Example: Rectangle.create_square(5) or rectangle.create_square(5)
    #     Why: Class methods are often used for alternative constructors or for operations that need to be performed on the class itself rather than on instances.
    # Static Methods:
    #     How to call: Static methods can also be called on either the class itself or on instances of the class using dot notation.
    #     Example: Rectangle.is_square(square) or rectangle.is_square(square)
    #     Why: Static methods are independent of instance or class state and can be called without needing access to instance or class attributes. They are used for utility functions that don't depend on the instance or class state.

# purpose of  Methods:
    # Use instance methods for operations that involve and manipulate instance attributes.
    # Use class methods for operations that operate on the class itself or have a shared context among all instances.
    # Use static methods for utility functions that are not tied to instances or classes and don't require access to instance or class attributes.


    # Instance Methods:
    #     Purpose: Instance methods are used when the method needs access to or manipulates the instance's state (attributes). They are closely tied to individual instances of a class.
    #     When to use: Use instance methods when you need to perform operations that involve the specific attributes of an instance. For example, calculating properties based on instance attributes, modifying instance attributes, or performing actions specific to that instance.
    
    # Class Methods:
    # classmethod() accepts a single parameter, function that is to be converted into classmethod.
    # The classmethod() returns a class method for a given function passed.
    # Class method is tied to its class rather than the instances created with that class. class methods can access class variables and methods.
    # classmethods can be called from either class itself (or) instance.
    # It receives the class (cls) as the first argument instead of the instance (self).
    #     Purpose: Class methods are used when the method needs to operate on the class itself rather than on instances. They are often used for alternative constructors or for operations that affect the class as a whole.
    #     When to use: Use class methods when the operation is related to the class as a whole rather than to individual instances. For example, creating instances of the class with specific properties, accessing or modifying class variables, or performing operations that don't require instance attributes.
    # Use cases:
    # Alternative constructors.
    # Factory methods.
    # Accessing or modifying class-level attributes.
    
    # Static Methods:
    #     Purpose: Static methods are used when the method does not access or modify instance or class state. They are independent of both instances and classes and are often used for utility functions.
    #     When to use: Use static methods when the operation is not related to any specific instance or class, and does not depend on instance or class attributes. For example, performing general-purpose calculations, formatting data, or implementing helper functions.
    # The @staticmethod decorator is used to define static methods within a class.
    # It does not receive any implicit first argument (neither self nor cls).
    # Use case: 
        # Grouping utility functions related to the class.
        # Methods that do not need access to instance or class attributes.
