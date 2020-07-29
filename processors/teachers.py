import curses

from texttable import Texttable

from models import User
from render import draw_menu, show_message


def setup():
    teachers = User.select().where(User.is_teacher == True)
    if not len(teachers):
        curses.wrapper(show_message, 'list is empty!')
        return
    t = [['ID', 'First name', 'Last name',  'Teacher number'], ]
    for teacher in teachers:
        t.append([teacher.id, teacher.first_name, teacher.last_name, teacher.student_number])
    table = Texttable().add_rows(t).draw()
    while curses.wrapper(draw_menu, table) != ord('b'):
        pass
