import curses

from texttable import Texttable

from render import draw_menu


def setup(teacher):
    table = Texttable().add_rows([
        ["No", "ITEM"],
        ['A', 'My Courses'],
        ['B', 'My Students'],
        ['C', 'Add Course request'],
        ['D', 'Record Marks'],
    ]).draw()
    message, alter = 'Enter the letter of your target', ''
    status = 'Press E to EDIT INFO | Press F to CHANGE PASSWORD | Press G to LOG OUT |'
    while True:
        choice = curses.wrapper(draw_menu, table, message, alter, status)
        if choice == ord('a'):
            from processors import my_courses_teachers
            my_courses_teachers.setup(teacher)
        elif choice == ord('b'):
            from processors import my_students
            my_students.setup(teacher)
        elif choice == ord('c'):
            from processors import add_course_request
            add_course_request.setup(teacher)
        elif choice == ord('d'):
            from processors import record_marks
            while not record_marks.setup(teacher):
                return True
        elif choice == ord('e'):
            from processors import edit_info
            edit_info.setup(teacher)
        elif choice == ord('f'):
            from processors import change_pass
            change_pass.setup(teacher)
        elif choice == ord('g'):
            break
        else:
            alter = 'Enter a valid letter'
