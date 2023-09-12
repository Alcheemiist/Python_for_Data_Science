class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        _sum =  sum([v1 * v2 for v1, v2 in zip(V1, V2)])
        print(_sum)
        return _sum

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        add = ([float(v1 + v2) for v1, v2 in zip(V1, V2)])
        print(add)
        return add

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        sous = [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        print(sous)
        return sous


a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)