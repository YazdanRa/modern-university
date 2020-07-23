from texttable import Texttable

from models import Course


def setup(teacher):
    table = Texttable().add_rows([
        ['ID', 'Course title', 'Is_ Active']
    ])
    for course in Course.select().where(Course.teacher == teacher):
        table.add_row([course.id, course.title, course.is_active])
    print(table.draw())
