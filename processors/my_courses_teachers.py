import curses

from texttable import Texttable

from models import Course
from render import show_message, draw_menu


def setup(teacher):
    courses = Course.select().where(Course.teacher == teacher)
    if not len(courses):
        curses.wrapper(show_message, 'List is empty!')
        return
    table = Texttable().add_rows([
        ['ID', 'Course title', 'Is_ Active']
    ])
    for course in courses:
        table.add_row([course.id, course.title, course.is_active])
    while curses.wrapper(draw_menu, table.draw()) != ord('b'):
        pass
