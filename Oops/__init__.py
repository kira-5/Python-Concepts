# __init__() also supports inheritance.

class Car:
    def __init__(self, name):
        self.name = name
        print("I ran first")
 
    def product(self):
        print("I ran second")
        return ("Name: " + self.name)
 
 
C = Car('Audi R8')
print(C.product())


# init with inheritance
class ParentClass:
    def __init__(self):
        print("Parent Class")
 
class Child(ParentClass):
    def __init__(self):
        ParentClass.__init__(self)
        print('Child Class')
 
obj = Child()


# Return Value of init in Python
class Foo:
    def __init__(self, str):
        self.str = str
 
 
obj = Foo('hello')
print(obj.str)
Foo.__init__(obj, 'Python')
print(obj.str)
