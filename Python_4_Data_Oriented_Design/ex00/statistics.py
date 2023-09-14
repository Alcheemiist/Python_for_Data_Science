
def variance(lst):
    """
    Calculate the variance of a list of numbers.

    Args:
        lst (list): A list of numbers.

    Returns:
        float: The variance of the input list of numbers.

    Example:
        numbers = [1, 2, 3, 4, 5]
        result = variance(numbers)
        print(result)
        # Output: 2.5
    """
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance


def check_args(args):
    """Check if args are numbers"""
    for arg in args:
        assert isinstance(arg, (int, float)), "not a number given in args"


def standard_deviation(lst):
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        lst (list): A list of numbers.

    Returns:
        float: The standard deviation of the input list of numbers.
    """
    return variance(lst) ** 0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Prints the Mean, Median, Quartile (25% and 75%)
    Standard deviation and Variance of a list of numbers."""
    if len(kwargs) <= 0:
        print("ERROR")
        return
    check_args(args)

    for key, value in kwargs.items():
        if value == "mean":
            if len(args) > 0:
                print("mean : ", sum(args) / len(args))
            else:
                print("ERROR")
        elif value == "median":
            if len(args) > 0:
                med = sorted(args)
                print("median : ", med[len(med) // 2])
            else:
                print("ERROR")
        elif value == "quartile":
            if len(args) > 0:
                arg_s = sorted(args)
                print("quartile : ", [float(arg_s[len(arg_s) // 4]),
                      float(arg_s[3 * len(arg_s) // 4])])
            else:
                print("ERROR")
        elif value == "std":
            if len(args) > 0:
                print("std : ", standard_deviation(args))
            else:
                print("ERROR")
        elif value == "var":
            if len(args) > 0:
                print("var : ", variance(args))
            else:
                print("ERROR")
        else:
            return
    return
