from models import User


def setup(student):
    for course in student.courses:
        teacher = User.get(User.id == course.teacher)
        msg = """
        ----------------------------------------------------------------------
            Teacher: {} {}, 
            Course: {}
            
            1.Very Bad  2.Bad  3.Normal  4.Good  5.Very Good
            
            Enter a number between from 1 to 5:
        """.format(teacher.first_name, teacher.last_name, course.title)
        try:
            rate = int(input(msg))
            if 1 <= rate <= 5:
                course.rate = (course.rate + rate)/2
                course.save()
                print('your rate successfully saved!')
            else:
                print('You should enter a valid number!')
        except ValueError:
            print('You should Enter a number!')

