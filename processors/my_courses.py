def setup(student):
    msg = """
    {} {} courses
    No {}
    """.format(student.first_name, student.last_name, student.student_number)
    for course in student.courses:
        msg += '| {} |\n'.format(course.title)
    print(msg)
