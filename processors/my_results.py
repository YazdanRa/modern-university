import curses

from texttable import Texttable

from models import Mark, Course
from render import draw_menu, show_message


def get_course_name(course):
    course = Course.get(Course.id == course)
    return course.title


def result_mark(course, student):
    mark, created = Mark.get_or_create(course=course, student=student)
    return str(mark.mark) if mark.mark else 'Not recorded!'


def setup(student):
    if not len(student.courses):
        curses.wrapper(show_message, 'List is empty!')
        return
    table = Texttable().add_rows([
        ['Course title', 'Your mark']
    ])
    for course in student.courses:
        table.add_row([course.title, result_mark(course, student)])
    while curses.wrapper(draw_menu, table.draw()) != ord('b'):
        pass
