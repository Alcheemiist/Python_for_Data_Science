import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random id for student."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass(init=True, repr=True)
class Student:
    """Class representing student."""
    name: str
    surname: str
    active: bool = field(default=False)
    login: str = field(default="")
    id: str = field(default="")

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.active = True
        self.login = self.name[0].upper() + self.surname.lower()
        self.id = generate_id()
