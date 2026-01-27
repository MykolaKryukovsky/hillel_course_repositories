
class Student:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} years old, {self.record_book}'

    def __eg__(self, other):
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))