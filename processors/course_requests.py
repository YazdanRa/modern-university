from texttable import Texttable

from models import Course, User


def get_teacher_name(course):
    teacher = User.get(User.id == course.teacher)
    return '{} {}'.format(teacher.first_name, teacher.last_name)


def setup():
    table = Texttable().add_rows([
        ['ID', 'Course title', 'Teacher']
    ])
    for course in Course.select().where(Course.is_active == False):
        table.add_row([course.id, course.title,  get_teacher_name(course)])
    print(table.draw())
    choise = input("""
        Enter the id of the course you want to active:
        Enter 0 to Cancel the process and back to the menu
    """)
    try:
        id = int(choise)
        if id == 0:
            print('The process has been canceled!')
            return True
        course = Course.get(Course.id == id)
        course.is_active = True
        course.save()
        print('course {} successfully activated!'.format(course.title))
        return True
    except ValueError:
        print('You should enter a valid number!')
        return False
