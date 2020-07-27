import curses

from models import User

from render import get_input, show_message


def get_data():
    student_number = curses.wrapper(get_input, 'Enter your student number:')
    password = curses.wrapper(get_input, 'Enter your password:')
    return student_number, password


def validate(student_number, password):
    user = User.select().where((User.student_number == student_number) & (User.password == password))
    if not len(user):
        curses.wrapper(show_message, 'User dose not exists!')
        return None
    user = user[0]
    if not user.is_active:
        curses.wrapper(show_message, 'User is not active yet!')
        return None

    return user


def navigate(user):
    if user.is_student:
        from states.student import setup
        while setup(user):
            pass

    if user.is_teacher:
        from states.teacher import setup
        while setup(user):
            pass

    if user.is_admin:
        from states.admin import setup
        while setup(user):
            pass


def setup():
    student_number, password = get_data()
    user = validate(student_number, password)
    if user:
        navigate(user)
