from persiantools.jdatetime import JalaliDateTime
from texttable import Texttable

from processors import login, register


def setup():
    header = Texttable()
    header.add_rows([
        ['Welcome to Modern University'],
        [JalaliDateTime.now().strftime("%c")]
    ])
    print(header.draw())
    table = Texttable()
    table.add_rows([
        ["#", "Item"],
        ['L', 'Login'],
        ['R', 'Register'],
        ['E', 'Exit']
    ])
    print(table.draw())
    choice = input('Which one do you want: ').lower()
    if choice == 'l':
        login.setup()
    elif choice == 'r':
        register.setup()
    elif choice == 'e':
        exit(print('Good Bye :)'))
    else:
        print('Enter a valid letter!')
