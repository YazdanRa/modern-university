import curses

from render import get_input, show_message


def setup(user):
    new_password = curses.wrapper(get_input, 'Enter your new password:')
    user.password = new_password
    user.save()
    curses.wrapper(show_message, 'password successfully changed!')
