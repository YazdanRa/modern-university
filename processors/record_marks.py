from texttable import Texttable

from models import Course, Mark
from processors.my_results import result_mark
from processors.my_students import get_student_name


def get_mark_id(course, student):
    mark, created = Mark.get_or_create(course=course, student=student)
    return '{}'.format(mark.id)


def get_mark(id):
    mark = Mark.get(id=id)
    try:
        score = int(input('Enter the mark you wanna record for this student: '))
    except ValueError:
        print('You should enter a number!')
        return False
    if 0 <= score <= 20:
        mark.mark = score
        mark.save()
        print('Your mark successfully recorded!')
        return True
    else:
        print('You should enter a valid number between 0 and 20')
        return False


def setup(teacher, check=False):
    table = Texttable().add_rows([
        ['ID', 'Student name', 'Student number', 'Course title', 'Mark']
    ])
    for course in Course.select().where((Course.is_active == True) & (Course.teacher == teacher)):
        for student in course.students:
            table.add_row([
                get_mark_id(course, student),
                get_student_name(student),
                student.student_number,
                course.title,
                result_mark(course, student)
            ])
            check = True
    if check:
        print(table.draw())
        id = input("""
        Enter the ID of the item you want to record that number, although even if you want to change that.
        Enter 0 to cancel the process and back to the menu
        """)
        try:
            id = int(id)
            if id == 0:
                print('The process has been canceled!')
                return True
            while not get_mark(id):
                pass
        except:
            print('You should enter a valid number!')
            return False
    else:
        print('You don\'t have any student!')
        return True
