import curses

from texttable import Texttable

from render import select_menu


def setup():
    table = Texttable()
    table.add_rows([
        ['Login'],
        ['Register'],
    ])
    while True:
        choice = curses.wrapper(select_menu, table.draw())
        if choice == 'l':
            from processors import login
            login.setup()
        elif choice == 'r':
            from processors import register
            register.setup()

