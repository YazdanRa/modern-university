import curses

from texttable import Texttable

from models import User
from render import draw_menu


def setup():
    table = Texttable().add_rows([
        ['ID', 'First name', 'Last name',  'Student number']
    ])
    for student in User.select().where(User.is_student == True):
        table.add_row([student.id, student.first_name, student.last_name, student.student_number])
    while curses.wrapper(draw_menu, table.draw()) != ord('b'):
        pass
