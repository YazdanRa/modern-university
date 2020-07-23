from texttable import Texttable


def setup(teacher):
    print(Texttable().add_rows([
        ["No", "ITEM"],
        ['A', 'My Courses'],
        ['B', 'My Students'],
        ['C', 'Add Course request'],
        ['D', 'Record Marks'],
        ['E', 'Edit Info'],
        ['F', 'Change Password'],
        ['G', 'Log out'],
    ]).draw())
    choice = input('Which one do you want: ').lower()
    if choice == 'a':
        from processors import my_courses_teachers
        my_courses_teachers.setup(teacher)
    elif choice == 'b':
        from processors import my_students
        my_students.setup(teacher)
    elif choice == 'c':
        from processors import add_course_request
        add_course_request.setup(teacher)
    elif choice == 'd':
        from processors import record_marks
        record_marks.setup(teacher)
    elif choice == 'e':
        from processors import edit_info
        edit_info.setup(teacher)
    elif choice == 'f':
        from processors import change_pass
        change_pass.setup(teacher)
    elif choice == 'g':
        return False
    else:
        print('Enter a valid letter')
    return True
