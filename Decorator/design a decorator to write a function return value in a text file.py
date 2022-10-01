def log_message(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('test.txt', 'w') as f:
            for row in result:
                f.write(f"{str(row)}")
            return result
    return wrapper


@log_message
def a_function_that_returns_a_string():
    return "a string"


@log_message
def a_function_that_returns_a_strings_with_a_newline(s):
    return "{}\n".format(s)


a_function_that_returns_a_string()
a_function_that_returns_a_strings_with_a_newline('abc')
