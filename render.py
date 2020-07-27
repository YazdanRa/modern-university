import curses
from time import sleep

from persiantools.jdatetime import JalaliDateTime
from texttable import Texttable


def draw_menu(stdscr, table, msg='----', alter='', status=''):
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Initialization
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Declaration of strings
    title = JalaliDateTime.now().strftime("%A %d %B %Y %H:%M")[:width - 1]
    Table = table[:width - 1]
    Alter = alter[:width - 1]
    message = msg[:width - 1]
    statusbarstr = "Modern University | {}".format(status)

    # Centering calculations
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_x_keystr = int((width // 2) - (len(Alter) // 2) - len(Alter) % 2)
    start_y = int((height // 2) - 2)

    # Render status bar
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(height - 1, 0, statusbarstr)
    stdscr.addstr(height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
    stdscr.attroff(curses.color_pair(3))

    # Turning on attributes for title
    stdscr.attron(curses.color_pair(2))
    stdscr.attron(curses.A_BOLD)

    # Rendering title
    stdscr.addstr(start_y, start_x_title, title)

    # Turning off attributes for title
    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BOLD)

    # Print rest of text
    stdscr.addstr(start_y + 1, 0, Table)
    stdscr.addstr(start_y + 1, (width // 2) - 2, message)
    stdscr.addstr(start_y + 2, start_x_keystr, Alter)

    # Refresh the screen
    stdscr.refresh()

    # Wait for next input
    k = stdscr.getch()
    return k


def get_input(stdscr, msg='', alter='', status='Enter b to back |'):
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Initialization
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Declaration of strings
    title = JalaliDateTime.now().strftime("%A %d %B %Y %H:%M")[:width - 1]
    message = msg[:width - 1]
    keystr = alter[:width - 1]
    statusbarstr = "Modern University | {}".format(status)

    # Centering calculations
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
    start_y = int((height // 2) - 2)

    # Render status bar
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(height - 1, 0, statusbarstr)
    stdscr.addstr(height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
    stdscr.attroff(curses.color_pair(3))

    # Turning on attributes for title
    stdscr.attron(curses.color_pair(2))
    stdscr.attron(curses.A_BOLD)

    # Rendering title
    stdscr.addstr(start_y, start_x_title, title)

    # Turning off attributes for title
    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BOLD)

    # Print rest of text
    stdscr.addstr(start_y + 1, 0, message)
    stdscr.addstr(start_y + 5, start_x_keystr, keystr)

    # Refresh the screen
    stdscr.refresh()

    # Wait for next input

    k = stdscr.getstr()

    return k.decode('utf-8')


def show_message(stdscr, msg):
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Initialization
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Declaration of strings
    title = JalaliDateTime.now().strftime("%A %d %B %Y %H:%M")[:width - 1]
    message = msg[:width - 1]
    statusbarstr = "Modern University |"

    # Centering calculations
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_y = int((height // 2) - 2)

    # Render status bar
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(height - 1, 0, statusbarstr)
    stdscr.addstr(height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
    stdscr.attroff(curses.color_pair(3))

    # Turning on attributes for title
    stdscr.attron(curses.color_pair(2))
    stdscr.attron(curses.A_BOLD)

    # Rendering title
    stdscr.addstr(start_y, start_x_title, title)

    # Turning off attributes for title
    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BOLD)

    # Print rest of text
    stdscr.addstr(start_y + 1, 0, message)

    # Refresh the screen
    stdscr.refresh()
    sleep(1)


def setup(table):
    while True:
        k = curses.wrapper(draw_menu, table)
        print(k)


if __name__ == '__main__':
    table = Texttable().add_rows([
        ['0', 'test', 'test'],
        ['1', 'test', 'test'],
        ['2', 'test', 'test'],
        ['3', 'test', 'test'],
        ['4', 'test', 'test'],
        ['5', 'test', 'test'],
        ['6', 'test', 'test'],
        ['7', 'test', 'test'],
        ['8', 'test', 'test'],
        ['9', 'test', 'test'],
    ]).draw()
    setup(table)
