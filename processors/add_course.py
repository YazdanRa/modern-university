import curses

from texttable import Texttable

from models import Course
from render import show_message, get_input


def setup(student):
    courses = Course.select().where(Course.is_active == True)
    if not len(courses):
        curses.wrapper(show_message, 'List is empty!')
        return
    t = [['ID', 'Course Title'], ]
    for course in courses:
        t.append([course.id, course.title])
    table = Texttable().add_rows(t).draw()
    try:
        course_id = curses.wrapper(get_input, table)
        course_id = int(course_id)
        course = Course.get(Course.id == course_id)
        if course in student.courses:
            curses.wrapper(show_message, 'you already have this course!')
        else:
            student.courses.add(course)
            curses.wrapper(show_message, 'Course successfully added!')
    except:
        curses.wrapper(show_message, 'Failed :(\nYou should enter a valid number!')
