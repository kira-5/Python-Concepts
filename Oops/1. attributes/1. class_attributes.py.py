# Notes: Class attributes


class Scaler:

    # Class attribute
    course = "python"
    course2 = "javascript"
    course3 = "html"


# Class attribute shared by all instances
def accessing_attributes():

    # Accessing the values of the attributes
    print(Scaler.course)

    sc = Scaler
    sc_2 = Scaler

    # Accessing through object instantiation.
    print(sc.course)
    print(sc.course2)
    print(sc.course3)

    # Can be used by all the objects.
    print(sc_2.course)


# When you change a class attribute using the class name, the change affects all instances of that class. However, if you change the attribute using an instance of the class, the change only applies to that specific instance.\


def change_attributes_value():

    # Changing value using Class Name
    Scaler.course = "java"

    sc1 = Scaler
    sc2 = Scaler
    print(sc1.course)
    print(sc2.course)

    # Changing value using Class Instance
    sc1.course = "html"
    print(sc1.course)  # Value will change in this instance only
    print("Using class instance would not reflect the changes to other instances")
    print(Scaler.course)  # Value haven't changed
    print(sc2.course)  # Value haven't changed


if __name__ == "__main__":
    accessing_attributes()
    print("-" * 10)
    change_attributes_value()


# Accessing Class Attributes: Class attributes can be accessed using either the class name or an instance. If not found in the instance, Python looks for it in the class.

# Modifying Class Attributes:
# Changing via the class affects all instances, including new ones.
# Changing via an instance creates a new instance variable, doesn't affect others unless referenced through the class.

# Naming Conflicts: Instance attributes with the same name as class attributes shadow the class attribute for that instance.

# Best Practices: Use class attributes for shared data, instance attributes for unique data.
# Class attribute typically used for attributes that are shared across all instances of the class.
# If an attribute is meant to be unique for each instance, it should be defined in the __init__ method as an instance attribute.

# Classmethods and Staticmethods: These can access/manipulate class attributes, providing controlled modification.

# Immutable vs Mutable: Be cautious with mutable objects as class attributes; they're shared among all instances, so modifications can affect others.  Immutable objects are safer choices for class attributes if they are not meant to be modified.
