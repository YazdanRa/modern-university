import curses

from texttable import Texttable

from render import draw_menu


def setup():
    table = Texttable()
    table.add_rows([
        ["#", "Item"],
        ['L', 'Login'],
        ['R', 'Register'],
    ])
    message, alter, status = '', '', 'Press E to EXIT | '
    while True:
        choice = curses.wrapper(draw_menu, table.draw(), message, alter, status)
        if choice == ord('l'):
            from processors import login
            login.setup()
        elif choice == ord('r'):
            from processors import register
            register.setup()
        elif choice == ord('e'):
            exit(print('Good Bye :)'))
        else:
            alter = 'Enter a valid letter!'
