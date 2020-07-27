import curses

from texttable import Texttable

from render import draw_menu


def setup(student):
    table = Texttable().add_rows([
        ["#", "ITEM"],
        ['A', 'My Courses'],
        ['B', 'Result'],
        ['C', 'Add Course'],
        ['D', 'Evaluation of Teachers'],
    ]).draw()
    message, alter = 'Enter the letter of your target', ''
    status = 'Press E to EDIT INFO | Press F to CHANGE PASSWORD | Press G to LOG OUT |'
    while True:
        choice = curses.wrapper(draw_menu, table, message, alter, status)
        if choice == ord('a'):
            from processors import my_courses_students
            my_courses_students.setup(student)
        elif choice == ord('b'):
            from processors import my_results
            my_results.setup(student)
        elif choice == ord('c'):
            from processors import add_course
            add_course.setup(student)
        elif choice == ord('d'):
            from processors import evaluation
            evaluation.setup(student)
        elif choice == ord('e'):
            from processors import edit_info
            edit_info.setup(student)
        elif choice == ord('f'):
            from processors import change_pass
            change_pass.setup(student)
        elif choice == ord('g'):
            break
        else:
            alter = 'Enter a valid letter'
