import curses

from texttable import Texttable

from models import Course, User
from render import draw_menu


def get_teacher(course):
    teacher = User.get(User.id == course.teacher)
    return '{} {}'.format(teacher.first_name, teacher.last_name)


def setup():
    table = Texttable().add_rows([
        ['ID', 'Title', 'Teacher', 'Is_Active']
    ])
    for course in Course.select():
        table.add_row([course.id, course.title, get_teacher(course), course.is_active])
    while curses.wrapper(draw_menu, table.draw()) != ord('b'):
        pass
