from texttable import Texttable


def setup(admin):
    print(Texttable().add_rows([
        ["No", "ITEM"],
        ['A', 'teachers'],
        ['B', 'Students'],
        ['C', 'courses'],
        ['D', 'course requests'],
        ['E', 'accept users'],
        ['F', 'Top students'],
        ['G', 'Edit Information'],
        ['H', 'Change Password'],
        ['I', 'Log out'],
    ]).draw())
    choice = input('Which one do you want: ').lower()
    if choice == 'a':
        from processors import teachers
        teachers.setup()
    elif choice == 'b':
        from processors import students
        students.setup()
    elif choice == 'c':
        from processors import courses
        courses.setup()
    elif choice == 'd':
        from processors import course_requests
        course_requests.setup()
    elif choice == 'e':
        from processors import accept_users
        while not accept_users.setup():
            pass
    elif choice == 'f':
        from processors import top_students
        top_students.setup()
    elif choice == 'g':
        from processors import edit_info
        edit_info.setup(admin)
    elif choice == 'h':
        from processors import change_pass
        change_pass.setup(admin)
    elif choice == 'i':
        return False
    else:
        print('Enter a valid letter')
    return True
