
class Calculator:
    """
    A class that performs arithmetic operations on vectors.

    Attributes:
    vector (list): A list that stores the elements of the vector.

    Methods:
    __init__(self, vector): Initializes the Calculatorr.
    __add__(self, number): Adds a given number to each .
    __mul__(self, number): Multiplies each element of .
    __sub__(self, number): Subtracts a given number
    __truediv__(self, number): Divides each element
    """

    vector = []

    def __init__(self, vector):
        """
        Initializes the Calculator object with a given vector.

        Args:
        vector (list): A list of numbers representing the vector.
        """
        self.vector = vector

    def __add__(self, number) -> None:
        """
        Adds a given number to each element of the vector.

        Args:
        number (float): The number to be added to each element of the vector.
        """
        self.vector = Calculator([x + number for x in self.vector])
        print(self.vector.vector)

    def __mul__(self, number) -> None:
        """
        Multiplies each element of the vector by a given number.

        Args:
        number (float): The number to multiply each element of the vector by.
        """
        self.vector = Calculator([x * number for x in self.vector])
        print(self.vector.vector)

    def __sub__(self, number) -> None:
        """
        Subtracts a given number from each element of the vector.

        Args:
        number (float): The number to subtract from each element of the vector.
        """
        self.vector = Calculator([x - number for x in self.vector])
        print(self.vector.vector)

    def __truediv__(self, number) -> None:
        """
        Divides each element of the vector by a given number.

        Args:
        number (float): The number to divide each element of the vector by.
        """
        assert number != 0, "division by zero is undefined"
        for i in range(len(self.vector.vector)):
            self.vector.vector[i] = self.vector.vector[i] / number


v1 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = Calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
