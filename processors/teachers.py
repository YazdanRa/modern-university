from texttable import Texttable

from models import User


def setup():
    table = Texttable().add_rows([
        ['ID', 'First name', 'Last name',  'Teacher number']
    ])
    for teacher in User.select().where(User.is_teacher == True):
        table.add_row([teacher.id, teacher.first_name, teacher.last_name, teacher.student_number])
    print(table.draw())
