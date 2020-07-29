import curses

from texttable import Texttable

from models import User
from render import draw_menu, show_message


def setup():
    students = User.select().where(User.is_student == True)
    if not len(students):
        curses.wrapper(show_message, 'list is empty!')
        return
    t = [['ID', 'First name', 'Last name',  'Student number'], ]
    for student in students:
        t.append([student.id, student.first_name, student.last_name, student.student_number])
    table = Texttable().add_rows(t).draw()
    while curses.wrapper(draw_menu, table) != ord('b'):
        pass
