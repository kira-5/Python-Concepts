from time import time, sleep
import functools

"""
    ! Classes as Decorators:

        ? We can also use a class as a decorator. 
        
        ? Classes are the best option to store the state of some data, so let's understand how to implement a stateful decorator with a class that will record the number of calls made for a function.
        
       * There are two requirements to make a class as a decorator:
            ? The __init__ function needs to take a function as an argument.

            ? The class needs to implement the __call__ method. This is required because the class will be used as a decorator and a decorator must be a callable object.
        
        ? Also note that we use functools.update_wrapper instead of functools.wraps in case of a class as a decorator.
"""

import functools


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello!")


if __name__ == '__main__':
    say_hello()

"""
    ! Explanation:
    
       ? After decoration, the __call__ method of the class is called instead of the say_hello method.
"""


"""
        ! Takeaway:
            * Classes can also be used as decorators by implementing the __call__ method and passing the function to __init__ as an argument.
    """


# LIMITER FAST API EXAMPLE

from fastapi import FastAPI, Request
from functools import wraps
from datetime import datetime, timedelta

app = FastAPI()

class RateLimiter:
    def __init__(self, limit, period):
        self.limit = limit
        self.period = period
        self.requests = {}

    def __call__(self, func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            user_id = 4
            now = datetime.now()
            endpoint = request.url.path
            print(endpoint)
            key = (user_id, endpoint)
            if key not in self.requests:
                self.requests[key] = [now]
            else:
                self.requests[key] = [r for r in self.requests[key] if now - r < self.period]
                if len(self.requests[key]) >= self.limit:
                    return {"error": "Rate limit exceeded"}
                else:
                    self.requests[key].append(now)
            return await func(request, *args, **kwargs)
        return wrapper

limiter = RateLimiter(limit=5, period=timedelta(minutes=1))

@app.get("/")
@limiter
async def hello_world(request: Request):
    return {"message": "Hello World"}

@app.get("/get")
@limiter
async def another_endpoint(request: Request):
    return {"message": "Another Endpoint"}


# Function-based Decorators:

# Use function-based decorators when:

# You need a simple decorator without much internal state or complex logic.
# You want to keep the decorator implementation concise and straightforward.
# You don't need to maintain state across multiple invocations.
# Example Use Case:

# Logging: You want to log the input arguments and return values of certain API endpoints.

# Class-based Decorators:

# Use class-based decorators when:

# You need to maintain internal state or configuration across multiple invocations of the decorator.
# You want to encapsulate more complex behavior within the decorator.
# You need to perform additional setup or teardown logic during initialization or cleanup.
# Example Use Case:

# Rate Limiting: You want to limit the rate at which certain API endpoints can be accessed.

# Maintaining state in the context of decorators refers to preserving some form of information or data across multiple invocations of the decorator. In simpler terms, it's about keeping track of something between calls to the decorated function or method.

# Here's a more detailed explanation:

# Statelessness:

# In many cases, decorators are stateless, meaning they do not retain any information about previous invocations.
# When a function-based decorator is applied to a function or method, it executes its logic each time the function is called, without remembering anything about previous calls.
# Maintaining State:

# However, in some scenarios, you might need to maintain state within a decorator.
# This means storing and updating information across multiple invocations of the decorated function or method.
# The state could include things like counters, lists, dictionaries, configuration settings, or any other data relevant to the decorator's behavior.
# Class-based Decorators for State Management:

# Class-based decorators are often used when you need to maintain state.
# Since classes can have attributes that persist between calls (instance attributes), they are well-suited for storing and updating state information.
# Each instance of the class effectively represents a separate "stateful" decorator, allowing you to maintain different states for different instances.
# Example:

# For instance, in a rate-limiting decorator, you might need to keep track of the number of requests made within a certain time window.
# This information constitutes the state of the rate limiter, and it needs to be updated and checked each time a request is made.
# By using a class-based approach, you can keep track of this state within the class instance, ensuring that it persists between invocations of the decorated function.