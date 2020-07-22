from models import Course


def setup(student):
    courses = Course.select().where(Course.is_active == True)
    msg = ''
    for course in courses:
        msg += '| {} | {} |\n'.format(course.id, course.title)
    print(msg)
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
