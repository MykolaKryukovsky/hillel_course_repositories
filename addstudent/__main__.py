from student import Student
from group import Group



class main():
    st1 = Student('Male', 475, 'Duncan ', 'MacLeod', 'AN150')
    st2 = Student('Male', 32, 'John', 'Rambo', 'AN170')
    st3 = Student('Female', 32, 'Sarah', 'Connor', 'AN144')

    gr = Group('PD1')

    students_to_add = {st1, st2, st3}

    for student in students_to_add:
        try:
            gr.add_student(student)
            print(student)
        except ValueError as e:
            print(e)

    assert gr.find_student('MacLeod') == st1, "Test1"
    assert gr.find_student('Jobs') is None, "Test2"

    gr.delete_student('Connor')
    print(gr)


if __name__ == "__main__":
    main()