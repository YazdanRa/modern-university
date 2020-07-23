from texttable import Texttable

from models import Mark, Course


def get_course_name(course):
    course = Course.get(Course.id == course)
    return course.title


def result_mark(mark):
    return str(mark) if mark else 'Not recorded!'


def setup(student):
    table = Texttable().add_rows([
        ['Course title', 'Your mark']
    ])
    for mark in Mark.select().where(Mark.student == student):
        table.add_row([get_course_name(mark.course), result_mark(mark.mark)])
    print(table.draw())
