from models import User


def get_data():
    student_number = input('Enter your student number:\n')
    password = input('Enter your password:\n')
    return student_number, password


def validate(student_number, password):
    user = User.select().where((User.student_number == student_number) & (User.password == password))
    if not len(user):
        print('User dose not exists!')
        return None
    user = user[0]
    if not user.is_active:
        print('User is not active yet!')
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
