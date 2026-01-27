from group_std import gr, Student

st3 = Student('Female', 20, 'Inga', 'Bergström', 'AN144')
st4 = Student('Male', 475, 'Duncan ', 'MacLeod', 'AN150')
st5 = Student('Female', 32, 'Sarah', 'Connor', 'AN144')
st6 = Student('Male', 16, 'Harry', 'Potter', 'AN150')
st7 = Student('Female', 40, 'Jane', 'Eyre', 'AN144')
st8 = Student('Male', 78, 'Arnold', 'Schwarzenegger', 'AN150')
st9 = Student('Female', 16, 'Hermione', 'Granger', 'AN144')
st10 = Student('Male', 79, 'Sylvester', 'Stallone', 'AN150')
st11 = Student('Female', 30, 'Ellen', 'Ripley', 'AN144')
st12 = Student('Male', 32, 'John', 'Rambo', 'AN170')
students_to_add = {st3, st4, st5, st6, st7, st8, st9, st10, st11, st12}

for student in students_to_add:
    try:
        gr.add_student(student)
        print(student)
    except ValueError as e:
        print(e)
