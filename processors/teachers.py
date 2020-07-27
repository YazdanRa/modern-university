import curses

from texttable import Texttable

from models import User
from render import draw_menu


def setup():
    table = Texttable().add_rows([
        ['ID', 'First name', 'Last name',  'Teacher number']
    ])
    for teacher in User.select().where(User.is_teacher == True):
        table.add_row([teacher.id, teacher.first_name, teacher.last_name, teacher.student_number])
    while curses.wrapper(draw_menu, table.draw()) != ord('b'):
        pass
