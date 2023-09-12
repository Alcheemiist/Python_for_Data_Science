from S1E9 import Character


class Baratheon(Character):
    """Represents a character from the Baratheon family. """
    family_name: str
    eyes: str
    hairs: str

    def __init__(self, first_name: str):
        """
        Initializes the attributes of the Baratheon class.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The initial state of the
            character's life. Defaults to True.
        """
        is_alive: bool = True
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def Character_method(self):
        """
        Implements the abstract method Character_method inherited
        from the Character class.
        """
        pass

    def __str__(self) -> str:
        """
        Overrides the __str__ method to return a custom string
        representation of the object.
        Returns:
            str: The string representation of the object.
        """

        return "Vector: " +\
            f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        # return "Vector : " + str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """a class Lannister Familly"""
    family_name: str
    eyes: str
    hairs: str

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
        self.__class__.__name__ = "Lannister"

    def Character_method(self):
        pass

    @classmethod
    def create_lannister(self, name: str, is_alive: bool) -> Character:
        return self(name, is_alive)

    def __str__(self) -> str:
        """

        Overrides the __str__ method to return a custom string
        representation of the object.
        Returns:
            str: The string representation of the object.
        """
        return "Vector: " +\
            f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        # return "Vector : " + str(self.__dict__)

    def __repr__(self):
        return self.__str__()
