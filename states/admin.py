import curses

from texttable import Texttable

from render import draw_menu


def setup(admin):
    table = Texttable().add_rows([
        ["No", "ITEM"],
        ['A', 'teachers'],
        ['B', 'Students'],
        ['C', 'courses'],
        ['D', 'course requests'],
        ['E', 'accept users'],
        ['F', 'Top students'],
    ]).draw()
    message, alter = 'Enter the letter of your target', ''
    status = 'Press G to EDIT INFO | Press H to CHANGE PASSWORD | Press I to LOG OUT | Press Q to Quit |'
    while True:
        choice = curses.wrapper(draw_menu, table, message, alter, status)
        if choice == ord('a'):
            from processors import teachers
            teachers.setup()
        elif choice == ord('b'):
            from processors import students
            students.setup()
        elif choice == ord('c'):
            from processors import courses
            courses.setup()
        elif choice == ord('d'):
            from processors import course_requests
            course_requests.setup()
        elif choice == ord('e'):
            from processors import accept_users
            while not accept_users.setup():
                pass
        elif choice == ord('f'):
            from processors import top_students
            top_students.setup()
        elif choice == ord('g'):
            from processors import edit_info
            edit_info.setup(admin)
        elif choice == ord('h'):
            from processors import change_pass
            change_pass.setup(admin)
        elif choice == ord('q'):
            exit(print("bye"))
        elif choice == ord('i'):
            break
        else:
            alter = 'Enter a valid letter'
