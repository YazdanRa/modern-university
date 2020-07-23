from texttable import Texttable


def setup(student):
    table = Texttable()
    table.add_row(["ID", "Course"])
    for course in student.courses:
        table.add_row([course.id, course.title])
    print(table.draw())
