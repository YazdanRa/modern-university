import curses

from models import Course
from render import get_input, show_message


def setup(teacher):
    title = curses.wrapper(get_input, 'Enter your course title: ')
    Course.insert({
        Course.title: title,
        Course.teacher: teacher,
    }).execute()
    curses.wrapper(show_message, 'your course request successfully saved!')
