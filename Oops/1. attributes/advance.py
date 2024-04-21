# What is Namespace in Python and How it is Related to Attributes in Python?
# The namespace is nothing but a dictionary that contains the keys as objects of the class and values as the attributes of the class. A namespace is divided into two categories i.e. class namespace or object namespace. So whenever we try to access any attribute, it is first searched in the object namespace, and then it is searched in the class namespace.

# Now, the accessing time of the object attribute is lower than the time of accessing the class attribute since first the object namespace is searched. Now, when the Python interpreter cannot find the attribute in the class namespace, it throws an error.

# Different Methods to Access Attributes in Python

# getattr() – As the name suggests, the getattr() function is used to access the attributes of an object. This function takes two arguments i.e. object name and the name of the attribute that we want to get.
# hasattr() – The function hasattr() is used to check if an attribute exists in the class or not. This function also takes two arguments i.e. object name and the name of the attribute that we want to check.
# setattr() – The function setattr() is used to set the value(s) of any attribute.Now if the attribute does not exist, then it will create the attribute for us. This function takes three arguments i.e. object name, attribute name, and the value of the attribute that we want to set.
# delattr() – As the name suggests, the delattr() function is used to delete an attribute. If we try to access the attribute after deleting it, the Python interpreter raises an error called: class has no attribute. This function also takes two arguments i.e. object name and the name of the attribute that we want to delete.


class Student:
    # defining some class attributes.
    name = "Sushant"
    roll = 1


# creating an object of Student class.
student1 = Student()

# using the getattr() function to get the attributes of the class.
print(getattr(student1, "name"))

# using the hasattr() function to check the attributes of the class.
print(hasattr(student1, "name"))

# using the setattr() function to set the attributes of the class.
setattr(student1, "college", "LNCT")

# printing the latest attributes.
print(getattr(student1, "name"))

# using the delattr() function to delete the attributes of the class.
delattr(student1, "name")


# printing the latest attributes.
print(getattr(student1, "name")) # Error will be shown as name got deleted now.


# access the attributes of one class in another class. ?
# We can access the attributes of one class into another class by passing the object of one class to another.

class A():
    def __init__(self):
        self.variable1 = 10
        self.variable2 = 20

    def testMethod(self):
        self.variable1 = self.variable1 + self.variable2
        return self.variable1


class B(A):
    def __init__(self, class_a):
        self.variable1 = class_a.variable1
        self.variable2 = class_a.variable2


# creating an object.
object1 = A()

# updating the value of variable1.
sum = object1.testMethod()

# returning the value of variable1.
print(sum)

# passing object of A in class B.
object2 = B(object1)

# return the values carried by variable1 and variable2.
print(object2.variable1)
print(object2.variable2)
