
class Calculator:

    vector = []

    def __init__(self, vector):
        self.vector = vector
        
    def __add__(self, number):
        self.vector = Calculator([x + number for x in self.vector])
        print(self.vector.vector)
        return self.vector

    def __mul__(self, number):
        self.vector = Calculator([x * number for x in self.vector])
        print(self.vector.vector)
        return self.vector

    def __sub__(self, number):
        self.vector = Calculator([x - number for x in self.vector])
        print(self.vector.vector)
        return self.vector


    def __truediv__(self, number):
        if number == 0:
            raise ZeroDivisionError("division by zero is undefined")
        # self.vector =  Calculator([x / number for x in self.vector])
        for i in range(len(self.vector.vector)):
            self.vector.vector[i] = self.vector.vector[i] / number

        print(self.vector.vector)
        return self.vector


v1 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = Calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5