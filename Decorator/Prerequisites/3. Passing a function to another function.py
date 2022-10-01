
def do_twice(func):
    func()


def say_hello():
    print("Hello!")


if __name__ == '__main__':
    do_twice(say_hello)
