from abc import ABC, abstractmethod


class Character(ABC):
    """an abstract class "character" which can take a first_name as
        first parameter,
        is_alive and can change the health state of the character
        with a method die  that passes is_alive from True to False"""
    first_name: str
    is_alive: bool

    def __init__(self, first_name: str, is_alive: bool = True):
        """a constructor __init__ that initializes the attributes
            first_name and is_alive"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def Character_method(self):
        """an abstract method Character_method"""
        pass

    def die(self):
        """a method die that passes is_alive from True to False"""
        self.is_alive = False

    def __str__(self) -> str:
        """an abstract method __str__ that returns a custom string
            representation of the object"""
        return f"Vector: ({self.__class__.__name__}, '{self.eye_color}', '\
                    {self.hair_color}')"

    def __repr__(self):
        return self.__str__()


class Stark(Character):
    """a class Stark that inherits from Character and has a
        method die that passes is_alive from True to False"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """a constructor method __init__ that initializes
             the attributes first_name and is_alive"""
        super().__init__(first_name, is_alive)

    def Character_method(self):
        """a method Character_method that implies that the class Stark inherits
           from Character"""
        pass
