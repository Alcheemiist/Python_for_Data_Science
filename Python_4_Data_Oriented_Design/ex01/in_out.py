
def square(x: int | float) -> int | float:
    return x**2


def pow(x: int | float) -> int | float:
    return x**x


def outer(x: int | float, function) -> object:
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
