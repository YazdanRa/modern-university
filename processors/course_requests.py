import curses

from texttable import Texttable

from models import Course, User
from render import show_message, get_input


def get_teacher_name(course):
    teacher = User.get(User.id == course.teacher)
    return '{} {}'.format(teacher.first_name, teacher.last_name)


def setup():
    table = Texttable().add_rows([
        ['ID', 'Course title', 'Teacher']
    ])
    for course in Course.select().where(Course.is_active == False):
        table.add_row([course.id, course.title,  get_teacher_name(course)])
    message = 'Enter the id of the course you want to active!'
    status = 'Enter 0 to Cancel the process and back to the menu'
    try:
        id = curses.wrapper(get_input, table.draw(), message, status)
        id = int(id)
        if id == 0:
            curses.wrapper(show_message, 'The process has been canceled!')
            return True
        course = Course.get(Course.id == id)
        course.is_active = True
        course.save()
        curses.wrapper(show_message, 'course {} successfully activated!'.format(course.title))
        return True
    except ValueError:
        curses.wrapper(show_message, 'You should enter a valid number!')
        return False
