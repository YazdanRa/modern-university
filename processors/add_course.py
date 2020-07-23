from texttable import Texttable

from models import Course


def setup(student):
    courses = Course.select().where(Course.is_active == True)
    table = Texttable()
    table.add_row(['ID', 'Course'])
    for course in courses:
        table.add_row([course.id, course.title])
    print(table.draw())
    try:
        course_id = int(input('which course do you want:'))
        course = Course.get(Course.id == course_id)
        if course in student.courses:
            print('you already have this course!')
        else:
            student.courses.add(course)
            print('Course successfully added!')
    except:
        print('Failed :(\nYou should enter a valid number!')
