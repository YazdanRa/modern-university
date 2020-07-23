from models import Course


def setup(teacher):
    title = input('Enter your course title: ')
    Course.insert({
        Course.title: title,
        Course.teacher: teacher,
    }).execute()
    print('your course request successfully saved!')
