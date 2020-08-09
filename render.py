import curses
from threading import Thread
from time import sleep

from persiantools.jdatetime import JalaliDateTime
from texttable import Texttable


def refresh(args):
    while True:
        args.refresh()
        sleep(60)


def select_menu(stdscr, table, message='----', alter='', status='Enter Q to Quit |'):
    key = ""
    row = 0
    while True:
        table_list = table.split("\n")

        table_list[(row * 2 + 1) % 4] += " <- "
        table1 = "\n".join(table_list)

        key = draw_menu(stdscr, table1, message, alter, status)
        if key == 259:  # up
            row -= 1
        elif key == 258:  # down
            row += 1
        elif key == 10:
            if row & 1:
                return "r"
            else:
                return "l"

        elif key == ord('q'):
            exit(print('Good Bye :)'))
        else:
            alter = 'Enter a valid letter!'


def draw_menu(stdscr, table, message='----', alter='', status='Enter b to back |'):
    # start thread
    thread = Thread(target=refresh, args=stdscr)
    thread.start()
    thread.join()

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # Initialization
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Declaration of strings
    title = JalaliDateTime.now().strftime("%A %d %B %Y %H:%M")
    statusbarstr = "Modern University | {}".format(status)

    # Centering calculations
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_x_keystr = int((width // 2) - (len(alter) // 2) - len(alter) % 2)
    start_y = int((height // 2) - 2)

    # Render status bar
    stdscr.attron(curses.color_pair(3))
    try:
        stdscr.addstr(height - 1, 0, statusbarstr)
        stdscr.addstr(height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
    except curses.error:
        pass
    stdscr.attroff(curses.color_pair(3))

    # Turning on attributes for title
    stdscr.attron(curses.color_pair(2))
    stdscr.attron(curses.A_BOLD)

    # Rendering title
    try:
        stdscr.addstr(start_y, start_x_title, title)
    except curses.error:
        pass

    # Turning off attributes for title
    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BOLD)

    # Print rest of text
    stdscr.attron(curses.color_pair(4))

    try:
        stdscr.addstr(int(start_y / 2) + 1, 0, table)
        stdscr.attroff(curses.color_pair(4))
        stdscr.addstr(int(start_y / 2) + 1, (width // 2) - 2, message)
        stdscr.addstr(int(start_y / 2) + 2, start_x_keystr, alter)
    except curses.error:
        pass
    stdscr.attroff(curses.color_pair(4))

    # Refresh the screen
    stdscr.refresh()

    # Wait for next input
    k = stdscr.getch()
    return k


def get_input(stdscr, message, alter='', status=''):
    # start thread
    thread = Thread(target=refresh, args=stdscr)
    thread.start()
    thread.join()

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()
    curses.echo()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Initialization
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Declaration of strings
    title = JalaliDateTime.now().strftime("%A %d %B %Y %H:%M")
    statusbarstr = "Modern University | {}".format(status)

    # Centering calculations
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_x_keystr = int((width // 2) - (len(alter) // 2) - len(alter) % 2)
    start_y = int((height // 2) - 2)

    # Render status bar
    stdscr.attron(curses.color_pair(3))
    try:
        stdscr.addstr(height - 1, 0, statusbarstr)
        stdscr.addstr(height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
    except curses.error:
        pass
    stdscr.attroff(curses.color_pair(3))

    # Turning on attributes for title
    stdscr.attron(curses.color_pair(2))
    stdscr.attron(curses.A_BOLD)

    # Rendering title
    try:
        stdscr.addstr(start_y, start_x_title, title)
    except curses.error:
        pass

    # Turning off attributes for title
    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BOLD)
    # Print rest of text
    try:
        stdscr.addstr(start_y + 1, 0, message)
        stdscr.addstr(start_y + 5, start_x_keystr, alter)
    except curses.error:
        pass

    # Refresh the screen
    stdscr.refresh()

    # Wait for next input

    k = stdscr.getstr()
    curses.noecho()
    return k.decode('utf-8')


def show_message(stdscr, msg):
    # start thread
    thread = Thread(target=refresh, args=stdscr)
    thread.start()
    thread.join()

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
    try:
        stdscr.addstr(height - 1, 0, statusbarstr)
        stdscr.addstr(height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
    except curses.error:
        pass
    stdscr.attroff(curses.color_pair(3))

    # Turning on attributes for title
    stdscr.attron(curses.color_pair(2))
    stdscr.attron(curses.A_BOLD)

    # Rendering title
    try:
        stdscr.addstr(start_y, start_x_title, title)
    except curses.error:
        pass

    # Turning off attributes for title
    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BOLD)

    stdscr.attron(curses.color_pair(2))

    # Print rest of text
    stdscr.addstr(start_y + 1, 0, message)
    stdscr.attroff(curses.color_pair(2))

    # Refresh the screen
    stdscr.refresh()
    sleep(2)


def setup(table):
    while True:
        k = curses.wrapper(draw_menu, table)
        print(k)
        exit(0)


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
