# Notes: Instance attributes

class Person:
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

# Accessing Instance Attributes
def accessing_attributes():
    # Creating an instance
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)
    
    # Accessing instance attributes
    print(person1.name)
    print(person1.age)
    print(person2.name)
    print(person2.age)

# Modifying Instance Attributes
def modify_attributes():
    # Creating an instance
    person = Person("Alice", 30)
    
    # Modifying instance attributes
    person.name = "Eve"
    person.age = 35
    print(person.name)
    print(person.age)

if __name__ == "__main__":
    accessing_attributes()
    print("-" * 10)
    modify_attributes()

# Accessing Instance Attributes: Instance attributes are accessed using dot notation on instances of the class.

# Modifying Instance Attributes: Instance attributes can be modified directly using dot notation on instances of the class.

# Naming Conflicts: If an instance attribute has the same name as a class attribute, the instance attribute will shadow the class attribute for that instance.

# Best Practices: Define instance attributes within the __init__ method to ensure they are properly initialized when creating instances of the class.

# Immutable vs Mutable: Instance attributes can be either immutable or mutable, depending on their type. Immutable objects, like strings and tuples, cannot be changed after creation, while mutable objects, like lists and dictionaries, can be modified.
