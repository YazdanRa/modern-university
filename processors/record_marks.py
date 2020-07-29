import curses

from texttable import Texttable

from models import Course, Mark
from processors.my_results import result_mark
from processors.my_students import get_student_name
from render import show_message, get_input


def get_mark_id(course, student):
    mark, created = Mark.get_or_create(course=course, student=student)
    return '{}'.format(mark.id)


def get_mark(id):
    mark = Mark.get(id=id)
    try:
        score = curses.wrapper(get_input, 'Enter the mark you wanna record for this student: ')
        score = int(score)
    except ValueError:
        curses.wrapper(show_message, 'You should enter a number!')
        return False
    if 0 <= score <= 20:
        mark.mark = score
        mark.save()
        curses.wrapper(show_message, 'Your mark successfully recorded!')
        return True
    else:
        curses.wrapper(show_message, 'You should enter a valid number between 0 and 20')
        return False


def setup(teacher, check=False):
    courses = Course.select().where((Course.is_active == True) & (Course.teacher == teacher))
    if not len(courses):
        curses.wrapper(show_message, 'list is empty!')
    t = [['ID', 'Student name', 'Student number', 'Course title', 'Mark'], ]
    for course in courses:
        for student in course.students:
            t.append([
                get_mark_id(course, student),
                get_student_name(student),
                student.student_number,
                course.title,
                result_mark(course, student)
            ])
            check = True

    table = Texttable().add_rows(t).draw()
    if check:
        table += '\n\nEnter the ID of the item you want to record that number, although even if you want to change that.'
        alter = ''
        status = 'Enter 0 to cancel the process and back to the menu'
        while True:
            id = curses.wrapper(get_input, table, alter, status)
            try:
                id = int(id)
                if id == 0:
                    curses.wrapper(show_message, 'The process has been canceled!')
                    return True
                while not get_mark(id):
                    pass
            except:
                alter = 'You should enter a valid number!'
    else:
        curses.wrapper(show_message, 'You don\'t have any student!')
        return True
