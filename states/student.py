def setup(student):
    msg = """
        A - My Courses
        B - Result
        C - Add Course
        D - Evaluation of Teachers
        E - Edit Info
        F - Change Password
        G - Log out
    """
    print(msg)
    choice = input('Which one do you want: ').lower()
    if choice == 'a':
        from processors import my_courses
        my_courses.setup(student)
    elif choice == 'b':
        pass
    elif choice == 'c':
        from processors import add_course
        add_course.setup(student)
    elif choice == 'd':
        from processors import evaluation
        evaluation.setup(student)
    elif choice == 'e':
        pass
    elif choice == 'f':
        from processors import change_pass
        change_pass.setup(student)
    elif choice == 'g':
        return False
    else:
        print('Enter a valid letter')
    return True
