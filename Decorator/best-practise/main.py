from decorators.decorator import do_twice


@do_twice
def say_hello():
    print("Hello!")


@do_twice
def say_bye():
    print("Bye!")


if __name__ == '__main__':

    say_hello()
    say_bye()
