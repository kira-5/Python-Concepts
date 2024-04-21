# Method Overriding


# Method Overloading (Class Based):
class Animal:
    def make_sound(self):
        return "Genric animal sound"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print(dog.make_sound())  # Output: Woof
    print(cat.make_sound())  # Output: Meow

    print("-" * 50)

    calculator = Calculator()
    # print(calculator.add(2, 3))         # Error: TypeError (second add method is overwritten)
    print(calculator.add(2, 3, 4))


# Concept:
# Method overriding occurs in the context of inheritance
# Method overriding is the concept of redefining a method in a subclass that was already defined in the superclass.
# This allows the subclass to provide its own implementation of the method.
# is not directly supported in non-class-based contexts.
