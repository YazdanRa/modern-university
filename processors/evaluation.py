import curses

from models import User
from render import get_input, show_message


def setup(student):
    for course in student.courses:
        teacher = User.get(User.id == course.teacher)
        msg = """
        ----------------------------------------------------------------------
            Teacher: {} {}, 
            Course: {}
            
            1.Very Bad   2.Bad   3.Normal   4.Good   5.Very Good
            
            Enter a number between from 1 to 5:
        """.format(teacher.first_name, teacher.last_name, course.title)
        try:
            rate = curses.wrapper(get_input, msg)
            if 1 <= rate <= 5:
                course.rate = (course.rate + rate)/2
                course.save()
                curses.wrapper(show_message, 'your rate successfully saved!')
            else:
                curses.wrapper(show_message, 'You should enter a valid number!')
        except ValueError:
            curses.wrapper(show_message, 'You should Enter a number!')

