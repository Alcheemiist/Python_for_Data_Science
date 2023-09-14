
def square(x: int | float) -> int | float:
    """
    Returns the square of a given number.

    Args:
        x (int | float): The number to be squared.

    Returns:
        int | float: The square of the input number.
    """
    return x**2


def pow(x: int | float) -> int | float:
    """ Returns the power of a given number."""
    return x**x


def outer(x: int | float, function) -> object:
    """ Returns a function that will apply the given
     function to the given number."""
    count = [x]

    def inner() -> float:
        count[0] = function(count[0])
        return count[0]
    return inner


my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())

# Expected output:
# $> python tester.py
# 9
# 81
# 6561
# ---
# 1.8371173070873836
# 3.056683336818703
# 30.42684786675409
# $>
