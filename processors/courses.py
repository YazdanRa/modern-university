import curses

from texttable import Texttable

from models import Course, User
from render import draw_menu, show_message


def get_teacher(course):
    teacher = User.get(User.id == course.teacher)
    return '{} {}'.format(teacher.first_name, teacher.last_name)


def setup():
    courses = Course.select()
    if not len(courses):
        curses.wrapper(show_message, 'list is empty!')
        return
    t = [['ID', 'Title', 'Teacher', 'Is_Active'], ]
    for course in courses:
        t.append([course.id, course.title, get_teacher(course), course.is_active])
    table = Texttable().add_rows(t).draw()
    while curses.wrapper(draw_menu, table) != ord('b'):
        pass
