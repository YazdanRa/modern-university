from models import User


def get_data():
    student_number = input('Enter your student number:\n')
    password = input('Enter your password:\n')
    confirm_password = input('Enter your password again:\n')
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
            print('you successfully registered, now wait to accept by an admin!')

    else:
        print('passwords do not match')
