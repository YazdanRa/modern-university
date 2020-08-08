import curses

from texttable import Texttable

from models import User, Mark
from processors.my_students import get_student_name
from render import draw_menu, show_message


def setup(is_empty=True):
    table = Texttable().add_rows([
        ['Student name', 'Student number', 'Grade']
    ])
    for student in User.select().where((User.is_active == True) & (User.is_student == True)):
        sum, cnt, check = 0, 0, False
        for mark in Mark.select().where(Mark.student == student):
            if mark.mark:
                sum += mark.mark
                cnt += 1
                check = True
        if check:
            student.grade = sum/cnt
            student.save()
            table.add_row([get_student_name(student), student.student_number, student.grade])
            is_empty = False
    if is_empty:
        curses.wrapper(show_message,'Nothing to show! :)')
    else:
        # TODO: sort the table before draw that!
        curses.wrapper(draw_menu, table.draw())
