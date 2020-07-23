import logging
import os
import sys
import getpass

from models import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def load_environment():
    from dotenv import load_dotenv
    load_dotenv()

    # OR, the same with increased verbosity:
    load_dotenv(verbose=True)

    # OR, explicitly providing path to '.env'
    from pathlib import Path  # python3 only
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)


load_environment()

database.init(os.getenv("DATABASE"))
database.connect()
database.create_tables([
    User,
    Course,
    StudentCourse,
    Mark,
])


def createadmin():
    student_number = input('Enter a Student number for admin: ')
    if User.get_or_none(student_number=student_number):
        print('this student number already exists!')
        return
    password, confirm_password, try_cnt = 1, 2, 0
    while password != confirm_password and try_cnt < 3:
        password = getpass.getpass('Enter your password: ')
        confirm_password = getpass.getpass('Confirm your password: ')
        if password != confirm_password:
            print('Passwords are not match!, Try again!')
        try_cnt += 1
    if password != confirm_password:
        print('Sorry :(')
        return
    User.insert({
        User.student_number: student_number,
        User.password: password,
        User.is_active: True,
        User.is_admin: True,
    }).execute()
    print('Admin successfully created :)')
    return


def main():
    from states import greetings
    while True:
        greetings.setup()


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'createadmin':
            createadmin()
    else:
        main()
