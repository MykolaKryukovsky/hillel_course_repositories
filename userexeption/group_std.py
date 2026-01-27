class Human:
    """
    A class that describes a person
    """
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} years old'

class Student(Human):
    """
    A class that inherits a parent class Human
    and processes data
    """
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()} (Record: {self.record_book})'

class GroupLimitError(Exception):

    def __init__(self, message='LIMIT REACHED: MAX 10 STUDENTS!'):
        self.message = message
        super().__init__(self.message)

class Group:
    """
    A class whose instance consists of objects of the Student class
    Implements methods for adding, deleting a student,
    and searching for a student by last name
    """
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError('LIMIT REACHED: MAX 10 STUDENTS!')
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.discard(student_to_delete)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        if not self.group:
            return f'Group Number: {self.number}\nNo students in the group.'
        return f'Group Number: {self.number}\nStudents:\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

