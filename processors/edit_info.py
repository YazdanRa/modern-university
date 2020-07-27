import curses

from render import get_input, show_message


def setup(user):
    user.first_name = curses.wrapper(get_input, 'Enter your first name: ')
    user.last_name = curses.wrapper(get_input, 'Enter your last name: ')
    user.hometown = curses.wrapper(get_input, 'Enter your hometown: ')
    user.national_id = curses.wrapper(get_input, 'Enter your National ID: ')
    user.save()
    curses.wrapper(show_message, 'your information successfully updated!')
