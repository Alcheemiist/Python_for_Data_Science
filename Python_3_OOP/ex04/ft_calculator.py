class calculator:
    """
    A class that provides static methods for performing

    Methods:
    - dotproduct(V1: list[float], V2: list[float]) -> float:
    - add_vec(V1: list[float], V2: list[float]) -> list[float]:.
    - sous_vec(V1: list[float], V2: list[float]) -> list[float]:
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> float:
        """
        Calculates the dot product of two vectors.

        Args:
        - V1: A list of floats representing the first vector.
        - V2: A list of floats representing the second vector.

        Returns:
        - The dot product of the two vectors as a float.
        """
        _sum = sum([v1 * v2 for v1, v2 in zip(V1, V2)])
        print(_sum)
        return _sum

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> list[float]:
        """
        Adds two vectors element-wise.

        Args:
        - V1: A list of floats representing the first vector.
        - V2: A list of floats representing the second vector.

        Returns:
        - A list of floats representing the resulting vector
        """
        add = ([float(v1 + v2) for v1, v2 in zip(V1, V2)])
        print(add)
        return add

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> list[float]:
        """
        Subtracts two vectors element-wise.

        Args:
        - V1: A list of floats representing the first vector.
        - V2: A list of floats representing the second vector.

        Returns:
        - A list of floats representing the resulting vector
        """
        sous = [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        print(sous)
        return sous


# a = [5, 10, 2]
# b = [2, 4, 3]
# calculator.dotproduct(a, b)
# calculator.add_vec(a, b)
# calculator.sous_vec(a, b)
