from texttable import Texttable

from models import Course


def get_student_name(student):
    return '{} {}'.format(student.first_name, student.last_name)


def setup(teacher):
    table = Texttable().add_rows([
        ['ID', 'Student name', 'Student number', 'Course name']
    ])
    for course in Course.select().where((Course.is_active == True) & (Course.teacher == teacher)):
        for student in course.students:
            table.add_row([student.id, get_student_name(student), student.student_number, course.title])
    print(table.draw())
