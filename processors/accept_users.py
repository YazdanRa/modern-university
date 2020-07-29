import curses

from texttable import Texttable

from models import User
from render import draw_menu, show_message, get_input


def set_role(user):
    table = Texttable().add_rows([
        ['#', 'role'],
        ['A', 'Admin'],
        ['T', 'Teacher'],
        ['S', 'Student'],
    ]).draw()
    message = 'Now Enter the tole of the user you wanna active they!'
    alter = ''
    status = 'Enter C for cancel the process and back to the menu'
    while True:
        role = curses.wrapper(draw_menu, table, message, alter, status)
        if role == ord('a'):
            user.is_admin = True
            user.is_active = True
            user.save()
            curses.wrapper(show_message, 'Admin successfully activated!')
            return True
        elif role == ord('t'):
            user.is_teacher = True
            user.is_active = True
            user.save()
            curses.wrapper(show_message, 'Teacher successfully activated!')
            return True
        elif role == ord('s'):
            user.is_student = True
            user.is_active = True
            user.save()
            curses.wrapper(show_message, 'Student successfully activated!')
            return True
        elif role == ord('c'):
            curses.wrapper(show_message, 'The process has been canceled!')
            return False
        else:
            alter = 'Enter a valid letter!'


def setup():
    users = User.select().where(User.is_active == False)
    if not len(users):
        curses.wrapper(show_message, 'List is empty')
        return True
    table = Texttable()
    t = [['ID', 'Student number']]
    for user in users:
        t.append([user.id, user.student_number])
    table.add_rows(t)
    message = 'Now send the ID of target you want to active it!'
    status = 'send 0 to cancel the process and back to menu'
    try:
        id = curses.wrapper(get_input, table.draw(), message, status)
        id = int(id)
        if id == 0:
            curses.wrapper(show_message, 'The process has been canceled!')
            return True
        user = User.get(User.id == id)
        if user:
            while not set_role(user):
                pass
        else:
            curses.wrapper(show_message, 'You should enter a valid number!')
            return False
    except:
        curses.wrapper(show_message, 'You should enter a number!')
        return False
