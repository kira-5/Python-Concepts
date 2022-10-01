def foo():
    print('I am foo')


if __name__ == '__main__':
    also_foo = foo

    foo()  # Calling by function
    also_foo()  # Calling by variable
