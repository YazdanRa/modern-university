import curses

from texttable import Texttable

from render import show_message


def setup(student):
    table = Texttable().add_rows([[course.id, course.title] for course in student.courses]).draw()
    curses.wrapper(show_message, table)
