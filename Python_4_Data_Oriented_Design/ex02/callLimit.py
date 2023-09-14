def callLimit(limit: int):
    """ Decorator that limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter


@callLimit(3)
def f():
    """ Function that prints f()"""""
    print("f()")


@callLimit(1)
def g():
    """ Function that prints g()"""""
    print("g()")


for i in range(3):
    f()
    g()
