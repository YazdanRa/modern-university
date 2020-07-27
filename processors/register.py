import curses

from models import User
from render import get_input, show_message


def get_data():
    student_number = curses.wrapper(get_input, 'Enter your student number:')
    password = curses.wrapper(get_input, 'Enter your password:')
    confirm_password = curses.wrapper(get_input, 'Enter your password again:\n')
    return (student_number, password) if password == confirm_password else (None, None)


def validate(student_number):
    user = User.select().where(User.student_number == student_number)
    return False if len(user) else True


def save_data(student_number, password):
    User.insert({
        User.student_number: student_number,
        User.password: password,
    }).execute()


def setup():
    student_number, password = get_data()
    if student_number:
        if validate(student_number):
            save_data(student_number, password)
            curses.wrapper(show_message, 'you successfully registered, now wait to accept by an admin!')
        else:
            curses.wrapper(show_message, 'This student number already exists!')

    else:
        curses.wrapper(show_message, 'passwords do not match')
