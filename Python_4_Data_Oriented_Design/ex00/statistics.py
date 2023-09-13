
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
    assert len(args) != 0, "no args number given"
    assert len(kwargs) != 0, "no kwargs given"
    check_args(args)

    for key, value in kwargs.items():
        if value == "mean":
            print("mean : ", sum(args) / len(args))
        elif value == "median":
            med = sorted(args)
            print("median : ", med[len(med) // 2])
        elif value == "quartile":
            arg_s = sorted(args)
            print("quartile : ", [float(arg_s[len(arg_s) // 4]),
                  float(arg_s[3 * len(arg_s) // 4])])
        elif value == "std":
            print("std : ", standard_deviation(args))
        elif value == "var":
            print("var : ", variance(args))
        else:
            print("OPERATION NOT FOUND")
    return


# Your tester.py:
ft_statistics(1, 42, 360, 11, 64, tat="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
              ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
