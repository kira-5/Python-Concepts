from time import time, sleep
import functools

"""
    ! Decorating a Complete Class:

        ? You can also use decorators on a whole class.
        
       * Writing a class decorator is very similar to writing a function decorator.
            ? The only difference is that the decorator will receive a class and not a function as an argument.
            ? Decorating a class does not decorate its methods. It's equivalent to the following:
                * className = decorator(className)
            ? It just adds functionality to the instantiation process of the class.
        
        ? One of the most common examples of using a decorator on a class is @dataclass from the dataclasses module:

"""
from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str
    active: bool


if __name__ == '__main__':
    sheldon = User("sheldon", "fakepassword", True)
    print(sheldon.username)

"""
    ! Explanation:
    
       ? A data class is a class mainly containing data. It comes with basic functionality already implemented. We can instantiate, print, and compare data class instances straight out of the b
     
        ? The username:str syntax is called type hints in Python. Type hints are a special syntax that allows declaring the type of a variable.
        
        ? In the example, we have created a class called User which saves the data related to a user. Then, we created a user and printed its username.
"""


"""
        ! Takeaway:
            * Decorators can be used with the methods of a class or the whole class.
    """
