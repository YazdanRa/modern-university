import curses

from texttable import Texttable

from render import show_message, draw_menu


def setup(student):
    if not len(student.courses):
        curses.wrapper(show_message, 'list is empty!')
        return
    table = Texttable().add_rows([[course.id, course.title] for course in student.courses]).draw()
    while curses.wrapper(draw_menu, table) != ord('b'):
        pass
