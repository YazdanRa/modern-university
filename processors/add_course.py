import curses

from texttable import Texttable

from models import Course
from render import draw_menu, show_message


def setup(student):
    courses = Course.select().where(Course.is_active == True)
    table = Texttable().add_rows([[course.id, course.title] for course in courses]).draw()

    message = 'which course do you want:'
    alter = ''
    status = ''
    try:
        course_id = curses.wrapper(draw_menu, table, message, alter, status)
        course = Course.get(ord(Course.id) == course_id)
        if course in student.courses:
            curses.wrapper(show_message, 'you already have this course!')
        else:
            student.courses.add(course)
            curses.wrapper(show_message, 'Course successfully added!')
    except:
        curses.wrapper(show_message, 'Failed :(\nYou should enter a valid number!')
