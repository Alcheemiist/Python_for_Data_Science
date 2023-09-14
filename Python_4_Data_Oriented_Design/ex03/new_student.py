import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random id for student."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class representing student."""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(default="")
    id: str = field(default="")

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.active = True
        self.login = self.name[0].upper() + self.surname.lower()
        self.id = generate_id()


student = Student(name="Edward", surname="agle")
print(student)
