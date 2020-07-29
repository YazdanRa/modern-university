import curses

from texttable import Texttable

from models import Course
from render import show_message, draw_menu


def get_student_name(student):
    return '{} {}'.format(student.first_name, student.last_name)


def setup(teacher):
    courses = Course.select().where((Course.is_active == True) & (Course.teacher == teacher))
    if not len(courses):
        curses.wrapper(show_message, 'list is empty!')
        return
    t = [['ID', 'Student name', 'Student number', 'Course name'], ]
    for course in courses:
        for student in course.students:
            t.append([student.id, get_student_name(student), student.student_number, course.title])
    table = Texttable().add_rows(t).draw()
    while curses.wrapper(draw_menu, table) != ord('b'):
        pass
